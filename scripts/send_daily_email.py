#!/usr/bin/env python3
"""Daily email sender.

Loads `templates/daily_email.html`, renders question markdown to HTML,
and sends via SMTP. Uses `markdown-it-py` and `beautifulsoup4` when
available, with safe fallbacks.

Usage: python scripts/send_daily_email.py [--file PATH] [--dry-run]
"""
from __future__ import annotations

import os
import re
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template
import smtplib

# Optional dependencies
try:
    from markdown_it import MarkdownIt
except Exception:
    MarkdownIt = None

try:
    from mdit_py_plugins.table import table_plugin
except Exception:
    table_plugin = None

try:
    from bs4 import BeautifulSoup
except Exception:
    BeautifulSoup = None

BASE = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = BASE / "templates" / "daily_email.html"
QUESTIONS_DIR = BASE / "questions"

# Visual defaults for Statistics
DEFAULTS = {
    "title": "통계분석 일일 문제",
    "headline": "📊 통계분석 일일 문제",
    "badge": "Daily Statistics Question",
    "page_bg": "#edf3f8",
    "accent": "#2f5d73",
    "badge_bg": "#e3edf3",
    "header_subtle": "#dbe7ee",
    "preheader": "오늘의 통계 문제와 해설이 도착했습니다.",
    "font_sans": "'Noto Sans KR', Arial, sans-serif",
}


def find_question() -> Path | None:
    today = datetime.now().strftime("%Y%m%d")
    today_matches = sorted(QUESTIONS_DIR.glob(f"*{today}*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    return today_matches[0] if today_matches else None


SECTION_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.I | re.M)


def parse_sections(content: str) -> dict:
    """Find headings and take content under question/explanation sections, preserving subheadings."""
    lines = content.splitlines()
    sections = {"question": "", "explanation": "", "date": ""}
    current = None
    for ln in lines:
        stripped = ln.strip()
        m = SECTION_RE.match(stripped)
        if m:
            title = re.sub(r"\s+", " ", m.group(2)).strip().lower()
            if title in ("문항", "문제", "problem"):
                current = "question"
                continue
            if title in ("해설", "정답 및 해설", "정답", "solution", "answers"):
                current = "explanation"
                continue
            if current:
                sections[current] += ln + "\n"
            continue
        if re.match(r"^\s*---\s*$", ln):
            continue
        gen = re.match(r"^\*?generated on:\s*(.+?)\*?\s*$", stripped, re.I)
        if gen:
            sections["date"] = gen.group(1)
            continue
        if current:
            sections[current] += ln + "\n"
    if not sections["question"] and not sections["explanation"]:
        sections["question"] = content
    for k in ("question", "explanation"):
        sections[k] = sections[k].strip()
    return sections


def extract_md_tables(md: str) -> tuple[str, dict[str, str]]:
    lines = md.splitlines()
    out: list[str] = []
    tables: dict[str, str] = {}
    i = 0
    table_idx = 0

    def is_table_row(line: str) -> bool:
        s = line.strip()
        return s.startswith("|") and s.endswith("|") and s.count("|") >= 2

    def is_delim_row(line: str) -> bool:
        s = line.strip().strip("|")
        parts = [p.strip() for p in s.split("|")]
        return bool(parts) and all(re.fullmatch(r":?-{3,}:?", p or "") for p in parts)

    def split_row(line: str) -> list[str]:
        s = line.strip().strip("|")
        return [c.strip() for c in s.split("|")]

    while i < len(lines):
        if i + 1 < len(lines) and is_table_row(lines[i]) and is_delim_row(lines[i + 1]):
            header = split_row(lines[i])
            align_parts = split_row(lines[i + 1])
            aligns = []
            for part in align_parts:
                left = part.startswith(":")
                right = part.endswith(":")
                if left and right:
                    aligns.append("center")
                elif right:
                    aligns.append("right")
                else:
                    aligns.append("left")
            rows = []
            i += 2
            while i < len(lines) and is_table_row(lines[i]):
                rows.append(split_row(lines[i]))
                i += 1
            thead = "<thead><tr>" + "".join(
                f'<th style="text-align:{aligns[idx] if idx < len(aligns) else "left"};">{cell}</th>'
                for idx, cell in enumerate(header)
            ) + "</tr></thead>"
            body_rows = []
            for row in rows:
                body_rows.append("<tr>" + "".join(
                    f'<td style="text-align:{aligns[idx] if idx < len(aligns) else "left"};">{cell}</td>'
                    for idx, cell in enumerate(row)
                ) + "</tr>")
            tbody = "<tbody>" + "".join(body_rows) + "</tbody>"
            key = f"TABLE_PLACEHOLDER_{table_idx}"
            tables[key] = f"<table>{thead}{tbody}</table>"
            out.append(key)
            table_idx += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), tables


def md_to_html(md: str) -> str:
    if not md:
        return ""
    md, table_map = extract_md_tables(md)
    if MarkdownIt:
        md_renderer = MarkdownIt("commonmark", {"html": False, "breaks": True, "linkify": True})
        if table_plugin:
            md_renderer.use(table_plugin)
        html = md_renderer.render(md)
    else:
        parts = [p.strip() for p in md.split('\n\n') if p.strip()]
        html = ''.join("<p>" + p.replace("\n", "<br/>") + "</p>" for p in parts)
    for key, table_html in table_map.items():
        html = html.replace(f"<p>{key}</p>", table_html).replace(key, table_html)
    if BeautifulSoup:
        soup = BeautifulSoup(f"<div>{html}</div>", "html.parser")
        for p in soup.find_all():
            if not p.get_text(strip=True) and not p.find(True):
                p.decompose()
        for table in soup.find_all("table"):
            table["role"] = "presentation"
            table["style"] = (
                "width:100%; border-collapse:collapse; margin:16px 0; "
                "font-size:14px; line-height:1.6; border:1px solid #d9e2ec;"
            )
            for th in table.find_all("th"):
                base = th.get("style", "")
                th["style"] = (
                    base + ("; " if base else "") +
                    "border:1px solid #d9e2ec; padding:10px 12px; background:#f8fafc; font-weight:700;"
                )
            for td in table.find_all("td"):
                base = td.get("style", "")
                td["style"] = base + ("; " if base else "") + "border:1px solid #d9e2ec; padding:10px 12px; vertical-align:top;"
            for thead in table.find_all("thead"):
                thead["style"] = "display:table-header-group;"
            for tbody in table.find_all("tbody"):
                tbody["style"] = "display:table-row-group;"
        for code in soup.find_all("code"):
            code["style"] = "background:#f3f4f6; padding:2px 5px; border-radius:4px; font-family:Consolas, Monaco, monospace;"
        for pre in soup.find_all("pre"):
            pre["style"] = "background:#0f172a; color:#e5e7eb; padding:14px; border-radius:8px; overflow:auto;"
        for ul in soup.find_all("ul"):
            ul["style"] = "margin:12px 0; padding-left:22px;"
        for ol in soup.find_all("ol"):
            ol["style"] = "margin:12px 0; padding-left:22px;"
        for blockquote in soup.find_all("blockquote"):
            blockquote["style"] = "margin:16px 0; padding:8px 16px; border-left:4px solid #cbd5e1; color:#475569;"
        return ''.join(str(c) for c in soup.div.contents)
    return html


def load_template() -> Template:
    txt = TEMPLATE_PATH.read_text(encoding="utf-8")
    return Template(txt)


def open_smtp():
    port = int(os.getenv("SMTP_PORT", 587))
    host = os.getenv("SMTP_HOST")
    if not host:
        raise RuntimeError("SMTP_HOST not set")
    if port == 465:
        return smtplib.SMTP_SSL(host, port)
    return smtplib.SMTP(host, port)


def send_email(html: str, subject: str):
    username = os.getenv("SMTP_USERNAME")
    password = os.getenv("SMTP_PASSWORD")
    recipients = [e.strip() for e in os.getenv("EMAIL_RECIPIENTS", "").split(",") if e.strip()]
    if not recipients:
        raise RuntimeError("EMAIL_RECIPIENTS not set")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = username or "noreply@example.com"
    msg["To"] = ", ".join(recipients)
    msg.attach(MIMEText(html, "html", "utf-8"))

    with open_smtp() as s:
        if int(os.getenv("SMTP_PORT", 587)) != 465:
            s.starttls()
        if username and password:
            s.login(username, password)
        s.send_message(msg)


def build_blocks(question_html: str, explanation_html: str, accent: str) -> str:
    return f"""
    <table role="presentation" width="100%" style="border-collapse:collapse; margin-bottom:24px; background:#eaf4f7; border:1px solid #c8dde5;">
      <tr><td style="padding:0;">
        <div style="height:5px; background:{accent}; line-height:5px; font-size:5px;">&nbsp;</div>
        <div style="padding:22px;">{question_html}</div>
      </td></tr>
    </table>

    <table role="presentation" width="100%" style="border-collapse:collapse;">
      <tr><td height="360" style="text-align:center; color:#6b7c93;">&nbsp;</td></tr>
    </table>

    <table role="presentation" width="100%" style="border-collapse:collapse; margin-top:14px; background:#f2f7ff; border:1px solid #d6e4ff;">
      <tr><td style="padding:0;">
        <div style="height:5px; background:#335c9b; line-height:5px; font-size:5px;">&nbsp;</div>
        <div style="padding:22px;">{explanation_html}</div>
      </td></tr>
    </table>
    """


def main(argv: list[str]):
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--file", help="Markdown file to send")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)

    tpl = load_template()
    qfile = Path(args.file) if args.file else find_question()
    if qfile is None:
        print("No question file found for today; skipping send.")
        return
    content = qfile.read_text(encoding="utf-8")
    secs = parse_sections(content)
    q_html = md_to_html(secs["question"])
    a_html = md_to_html(secs["explanation"])

    mail_date = datetime.now().strftime("%Y-%m-%d")
    vars = DEFAULTS.copy()
    vars.update({
        "content_blocks": build_blocks(q_html, a_html, DEFAULTS["accent"]),
        "subhead": secs.get("date") or mail_date,
    })

    tpl_html = tpl.safe_substitute(vars)

    if args.dry_run:
        out = Path.home() / "email_preview_statistics.html"
        out.write_text(tpl_html, encoding="utf-8")
        print("Wrote preview to", out)
        return

    subject = f"{DEFAULTS['title']} ({mail_date})"
    send_email(tpl_html, subject)
    print("Sent email")


if __name__ == "__main__":
    main(sys.argv[1:])
