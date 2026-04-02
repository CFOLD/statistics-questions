#!/usr/bin/env python3
"""
Daily Statistics Question Email Sender

Fetches a random question from generated_questions/, parses Markdown,
converts to HTML with HTML math entities (no JS), and sends via SMTP.

Email-optimized design:
- No JavaScript (works in all email clients)
- Inline CSS for maximum compatibility
- Custom table parser for reliable rendering
- Large spacing between question and explanation
"""

import os
import re
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from datetime import datetime
from html import escape

# Configuration - use working directory (repo root)
QUESTIONS_DIR = Path.cwd() / 'generated_questions'
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
EMAIL_RECIPIENTS = os.getenv('EMAIL_RECIPIENTS', '').split(',')


def get_random_question() -> dict:
    """Get a random question from the generated_questions directory."""
    md_files = list(QUESTIONS_DIR.glob('*.md'))
    if not md_files:
        raise FileNotFoundError("No question files found")

    selected_file = random.choice(md_files)
    content = selected_file.read_text(encoding='utf-8')
    return {'file': selected_file.name, 'content': content}


def parse_markdown_question(content: str) -> dict:
    """Parse markdown question into sections (question, explanation, purpose)."""
    sections = {
        'question': '',
        'explanation': '',
        'purpose': '',
        'date': ''
    }

    # Split by '---' delimiter (flexible newlines)
    parts = re.split(r'\n\s*---\s*\n', content)

    for part in parts:
        part = part.strip()
        if part.startswith('## 문항'):
            sections['question'] = part.replace('## 문항', '').strip()
        elif part.startswith('## 해설'):
            sections['explanation'] = part.replace('## 해설', '').strip()
        elif part.startswith('## 출제 의도'):
            sections['purpose'] = part.replace('## 출제 의도', '').strip()
        elif 'Generated on:' in part:
            sections['date'] = part.strip()

    return sections


def latex_to_html(latex: str) -> str:
    """Convert LaTeX math to HTML entities."""
    result = latex

    # Greek letters and symbols (single backslash)
    replacements = {
        # Greek lowercase
        '\\alpha': '&alpha;', '\\beta': '&beta;', '\\gamma': '&gamma;',
        '\\delta': '&delta;', '\\epsilon': '&epsilon;', '\\zeta': '&zeta;',
        '\\eta': '&eta;', '\\theta': '&theta;', '\\lambda': '&lambda;',
        '\\mu': '&mu;', '\\xi': '&xi;', '\\pi': '&pi;', '\\rho': '&rho;',
        '\\sigma': '&sigma;', '\\tau': '&tau;', '\\phi': '&phi;',
        '\\chi': '&chi;', '\\psi': '&psi;', '\\omega': '&omega;',
        # Greek uppercase
        '\\Delta': '&Delta;', '\\Gamma': '&Gamma;', '\\Lambda': '&Lambda;',
        '\\Sigma': '&Sigma;', '\\Pi': '&Pi;', '\\Phi': '&Phi;', '\\Omega': '&Omega;',
        # Math symbols
        '\\times': '&times;', '\\div': '&divide;', '\\pm': '&plusmn;',
        '\\approx': '&approx;', '\\leq': '&le;', '\\le': '&le;',
        '\\geq': '&ge;', '\\ge': '&ge;',
        '\\neq': '&ne;', '\\ne': '&ne;',
        '\\infty': '&infin;',
        '\\sum': '&sum;', '\\prod': '&prod;', '\\int': '&int;',
        '\\partial': '&part;', '\\prime': '&prime;',
        '\\rightarrow': '&rarr;', '\\to': '&rarr;',
        '\\leftarrow': '&larr;',
        '\\Rightarrow': '&rarr;',
        '\\Leftrightarrow': '&harr;',
        '\\equiv': '&equiv;',
        '\\in': '&isin;', '\\subset': '&sub;', '\\supset': '&sup;',
        '\\cup': '&cup;', '\\cap': '&cap;', '\\emptyset': '&empty;',
        '\\sqrt': '&radic;',
    }

    # Apply all replacements (longer patterns first to avoid partial matches)
    sorted_items = sorted(replacements.items(), key=lambda x: -len(x[0]))
    for key, value in sorted_items:
        result = result.replace(key, value)

    # Handle \frac{a}{b} - process numerator/denominator first, then wrap
    def process_frac_inner(inner: str) -> str:
        """Process ^ and _ inside frac numerator/denominator."""
        # Handle ^{...} and ^...
        inner = re.sub(r'\^\{([^}]*)\}', r'<sup>\1</sup>', inner)
        inner = re.sub(r'\^(&[a-z]+;|[a-zA-Z0-9])', r'<sup>\1</sup>', inner)
        # Handle _{...} and _...
        inner = re.sub(r'_{([^}]*)\}', r'<sub>\1</sub>', inner)
        inner = re.sub(r'_(&[a-z]+;|[a-zA-Z0-9])', r'<sub>\1</sub>', inner)
        return inner

    def replace_frac(match):
        num = process_frac_inner(match.group(1))
        den = process_frac_inner(match.group(2))
        return f'<sup>{num}</sup>/<sub>{den}</sub>'
    result = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', replace_frac, result)

    # Superscripts: ^{...} or ^... (outside of frac)
    result = re.sub(r'\^\{([^}]*)\}', r'<sup>\1</sup>', result)
    result = re.sub(r'\^(&[a-z]+;|[a-zA-Z0-9])', r'<sup>\1</sup>', result)

    # Subscripts: _{...} or _... (outside of frac)
    result = re.sub(r'_{([^}]*)\}', r'<sub>\1</sub>', result)
    result = re.sub(r'_(&[a-z]+;|[a-zA-Z0-9])', r'<sub>\1</sub>', result)

    # Remove remaining braces
    result = result.replace('{', '').replace('}', '')

    return result


def parse_table_row(line: str, expected_cols: int) -> list:
    """Parse a table row, handling | inside cells (e.g., Pr(>|z|))."""
    line = line.strip()

    # Remove leading and trailing |
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]

    # Split by |
    parts = [p.strip() for p in line.split('|')]

    # If we have exactly the right number of columns, return as-is
    if len(parts) == expected_cols:
        return parts

    # If we have too many parts, | was inside a cell
    # Rejoin parts from the right until we have the right count
    while len(parts) > expected_cols:
        # Remove empty parts at the end
        if parts and not parts[-1]:
            parts.pop()
            continue
        # Rejoin last two parts with |
        if len(parts) >= 2:
            parts[-2] = parts[-2] + ' | ' + parts[-1]
            parts.pop()
        else:
            break

    return parts[:expected_cols]


def parse_markdown_table(lines: list) -> str:
    """Parse a markdown table and return HTML with inline styles."""
    if len(lines) < 2:
        return '\n'.join(lines)

    # Parse separator to get column count first
    sep_line = lines[1].strip()
    if sep_line.startswith('|'):
        sep_line = sep_line[1:]
    if sep_line.endswith('|'):
        sep_line = sep_line[:-1]
    col_count = len(sep_line.split('|'))

    # Parse header with correct column count
    header_cells = parse_table_row(lines[0], col_count)

    # Build HTML table
    html = ['<table role="presentation" border="0" cellpadding="4" cellspacing="0" style="border-collapse: collapse; width: 100%; border: 1px solid #ccc; margin: 16px 0;">']

    # Header row
    html.append('  <tr style="background-color: #f0f4f8;">')
    for cell in header_cells:
        math_html = convert_math_to_html(cell)
        html.append(f'    <th style="border: 1px solid #cbd5e0; padding: 10px 12px; text-align: left; font-weight: 600; font-size: 14px; color: #1e293b;">{math_html}</th>')
    html.append('  </tr>')

    # Data rows (skip separator line)
    for i, row_line in enumerate(lines[2:], 1):
        if not row_line.strip():
            continue
        cells = parse_table_row(row_line, col_count)
        html.append('  <tr>')
        for j, cell in enumerate(cells):
            math_html = convert_math_to_html(cell)
            bg = 'white' if i % 2 == 1 else '#fafafa'
            html.append(f'    <td style="border: 1px solid #cbd5e0; padding: 10px 12px; text-align: left; font-size: 14px; color: #334155; background-color: {bg};">{math_html}</td>')
        html.append('  </tr>')

    html.append('</table>')
    return '\n'.join(html)


def convert_math_to_html(content: str) -> str:
    """Convert LaTeX math expressions to HTML with LaTeX reference."""
    # Store math expressions with their type (display or inline)
    math_storage = []

    def store_display(match):
        latex = match.group(1)
        idx = len(math_storage)
        math_storage.append(('display', latex))
        return f'__MATH_{idx}__'

    def store_inline(match):
        latex = match.group(1)
        idx = len(math_storage)
        math_storage.append(('inline', latex))
        return f'__MATH_{idx}__'

    # First, extract display math $$...$$
    temp = re.sub(r'\$\$(.+?)\$\$', store_display, content, flags=re.DOTALL)
    # Then extract inline math $...$
    temp = re.sub(r'\$([^$]+?)\$', store_inline, temp)

    # Convert each stored math expression
    def convert_inline(idx):
        _, latex = math_storage[idx]
        html = latex_to_html(latex)
        escaped_latex = escape(latex.strip())
        return f'<span style="font-family: Georgia, &quot;Times New Roman&quot;, serif; font-size: 15px; color: #0f172a; background: #f1f5f9; padding: 2px 6px; border-radius: 3px;">{html}<span style="font-size: 10px; color: #64748b;"> (${escaped_latex})</span></span>'

    def convert_display(idx):
        _, latex = math_storage[idx]
        html = latex_to_html(latex)
        escaped_latex = escape(latex.strip())
        return f'<div style="text-align: center; margin: 16px 0; padding: 12px; background: #f8fafc; border-radius: 6px;"><span style="font-family: Georgia, &quot;Times New Roman&quot;, serif; font-size: 18px; color: #1e293b;">{html}</span><br><span style="font-size: 11px; color: #64748b;">${{${escaped_latex}$}}</span></div>'

    # Restore math
    result = temp
    for idx, (mtype, latex) in enumerate(math_storage):
        placeholder = f'__MATH_{idx}__'
        if mtype == 'display':
            result = result.replace(placeholder, convert_display(idx))
        else:
            result = result.replace(placeholder, convert_inline(idx))

    return result


def markdown_to_html(md_content: str) -> str:
    """Convert Markdown to HTML with custom table and math handling."""
    lines = md_content.split('\n')
    html_parts = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for table (markdown table starts with | and has |---| separator)
        if line.strip().startswith('|') and i + 1 < len(lines) and '|---' in lines[i + 1]:
            table_lines = [line]
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith('|'):
                table_lines.append(lines[j])
                j += 1
            html_parts.append(parse_markdown_table(table_lines))
            i = j
            continue

        # Check for code block
        if line.strip().startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(escape(lines[i]))
                i += 1
            code_content = '\n'.join(code_lines)
            html_parts.append(f'<pre style="background-color: #1e293b; color: #e2e8f0; padding: 16px; border-radius: 6px; overflow-x: auto; font-family: &quot;Courier New&quot;, monospace; font-size: 13px; margin: 16px 0; line-height: 1.6;"><code>{code_content}</code></pre>')
            i += 1
            continue

        # Check for horizontal rule
        if line.strip() in ['---', '***', '___'] or (line.strip().startswith('-') and len(line.strip()) >= 3 and line.strip().replace('-', '') == ''):
            html_parts.append('<hr style="border: 0; border-top: 2px solid #e2e8f0; margin: 24px 0;" />')
            i += 1
            continue

        # Check for heading
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2)
            size = ['24px', '22px', '20px', '18px', '16px', '14px'][level - 1]
            math_html = convert_math_to_html(text)
            html_parts.append(f'<h{level} style="font-size: {size}; font-weight: 600; color: #1e293b; margin: 16px 0 12px; line-height: 1.4;">{math_html}</h{level}>')
            i += 1
            continue

        # Check for bold/italic
        if line.strip():
            text = line
            # Bold
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong style="font-weight: 600; color: #1e293b;">\1</strong>', text)
            # Italic
            text = re.sub(r'\*(.+?)\*', r'<em style="font-style: italic;">\1</em>', text)
            # Convert math
            text = convert_math_to_html(text)
            html_parts.append(f'<p style="margin: 8px 0; line-height: 1.8; color: #334155;">{text}</p>')
        else:
            html_parts.append('<br />')

        i += 1

    return '\n'.join(html_parts)


def create_email_html(question: dict) -> str:
    """Create HTML email optimized for email clients."""
    date_str = datetime.now().strftime('%Y-%m-%d')
    sections = parse_markdown_question(question['content'])

    # Convert markdown to HTML with math conversion
    question_html = markdown_to_html(sections['question'])
    explanation_html = markdown_to_html(sections['explanation'])
    purpose_html = markdown_to_html(sections['purpose'])

    # Gothic font family for Korean
    font_sans = "'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', 'Helvetica Neue', Arial, sans-serif"

    return f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="x-apple-disable-message-reformatting" />
  <title>통계분석 일일 문제</title>
  <style type="text/css">
    body, table, td, p, a, li, blockquote {{
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
      margin: 0;
      padding: 0;
    }}
    table, td {{
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }}
    table {{
      border-collapse: collapse !important;
    }}
    img {{
      -ms-interpolation-mode: bicubic;
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
    }}
    p {{
      margin: 0 0 16px 0;
    }}
    /* Table styles */
    table.data-table, table.data-table td, table.data-table th {{
      border: 1px solid #cbd5e0 !important;
      border-collapse: collapse !important;
    }}
    table.data-table {{
      width: 100% !important;
      mso-table-lspace: 0pt !important;
      mso-table-rspace: 0pt !important;
    }}
    table.data-table th {{
      background-color: #e2e8f0 !important;
      font-weight: bold !important;
      text-align: left !important;
      padding: 8px 12px !important;
    }}
    table.data-table td {{
      padding: 8px 12px !important;
    }}
    a {{
      color: #2563eb;
    }}
    u+[b] a {{
      color: inherit;
      text-decoration: none;
    }}
    @media screen and (max-width: 600px) {{
      .email-container {{
        width: 100% !important;
      }}
      .content-padding {{
        padding-left: 20px !important;
        padding-right: 20px !important;
      }}
    }}
  </style>
</head>
<body style="margin: 0; padding: 0; background-color: #f5f5f5; font-family: {font_sans};">

  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f5f5f5;">
    <tr>
      <td align="center" style="padding: 20px 0;">

        <table class="email-container" role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="background: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1); max-width: 600px; width: 100%;">

          <!-- Header -->
          <tr>
            <td style="background: linear-gradient(135deg, #4A90A4 0%, #357A9A 100%); padding: 32px 28px; text-align: left;">
              <h1 style="margin: 0; font-family: {font_sans}; font-size: 26px; font-weight: 600; color: #ffffff; line-height: 1.3;">📊 통계분석 일일 문제</h1>
              <p style="margin: 10px 0 0 0; font-family: {font_sans}; font-size: 14px; color: rgba(255,255,255,0.9);">{date_str}</p>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td class="content-padding" style="padding: 36px 32px; background-color: #ffffff;">

              <!-- Question Section -->
              <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8fafb; border: 1px solid #e1e8ed; border-radius: 8px; margin-bottom: 40px;">
                <tr>
                  <td style="padding: 28px 24px;">
                    <h2 style="margin: 0 0 20px 0; font-family: {font_sans}; font-size: 18px; font-weight: 600; color: #2c5282; padding-bottom: 14px; border-bottom: 2px solid #bed6e6;">문항</h2>
                    <div style="font-family: {font_sans}; font-size: 16px; line-height: 1.8; color: #334155;">
                      {question_html}
                    </div>
                  </td>
                </tr>
              </table>

              <!-- Large spacer (1000px) -->
              <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" height="1000" style="background: linear-gradient(to bottom, #f5f5f5, rgba(245,245,245,0.3)); margin: 40px 0;">
                <tr>
                  <td align="center" valign="middle" style="color: #94a3b8; font-size: 15px; font-family: {font_sans};">
                    <p style="margin: 0 0 10px 0; font-size: 16px; font-weight: 600;">📝 아래로 스크롤하여 해설 확인</p>
                    <p style="margin: 0; font-size: 13px; color: #64748b;">(먼저 문제를 풀어보세요!)</p>
                  </td>
                </tr>
              </table>

              <!-- Explanation Section -->
              <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f0f7ff; border: 1px solid #d1e8ff; border-radius: 8px; margin-bottom: 16px;">
                <tr>
                  <td style="padding: 28px 24px;">
                    <h2 style="margin: 0 0 20px 0; font-family: {font_sans}; font-size: 18px; font-weight: 600; color: #2b6cb0; padding-bottom: 14px; border-bottom: 2px solid #93c5fd;">해설</h2>
                    <div style="font-family: {font_sans}; font-size: 15px; line-height: 1.8; color: #334155;">
                      {explanation_html}
                    </div>
                  </td>
                </tr>
              </table>

              <!-- Purpose Section -->
              <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f9fbf5; border: 1px solid #e8f0d8; border-radius: 8px;">
                <tr>
                  <td style="padding: 28px 24px;">
                    <h2 style="margin: 0 0 20px 0; font-family: {font_sans}; font-size: 18px; font-weight: 600; color: #276749; padding-bottom: 14px; border-bottom: 2px solid #9ae6b4;">출제 의도</h2>
                    <div style="font-family: {font_sans}; font-size: 14px; line-height: 1.8; color: #4a5568;">
                      {purpose_html}
                    </div>
                  </td>
                </tr>
              </table>

            </td>
          </tr>

        </table>

      </td>
    </tr>
  </table>

</body>
</html>"""


def send_email(question: dict) -> None:
    """Send email with the question via SMTP."""
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'통계분석 일일 문제 ({datetime.now().strftime("%Y-%m-%d")})'
    msg['From'] = f'Statistics Questions <{SMTP_USERNAME}>'
    msg['To'] = ', '.join(EMAIL_RECIPIENTS)

    html_content = create_email_html(question)
    part = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(part)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)

    print(f"✓ Email sent to {', '.join(EMAIL_RECIPIENTS)}")
    print(f"  Question: {question['file']}")


def main():
    """Main entry point."""
    print("📧 Starting daily question email...")

    question = get_random_question()
    print(f"📝 Selected: {question['file']}")

    send_email(question)
    print("✅ Done!")


if __name__ == '__main__':
    main()
