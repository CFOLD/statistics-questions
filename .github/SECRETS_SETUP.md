# GitHub Secrets Setup Guide

Set GitHub Actions secrets so this repository can send daily emails.

## Setup steps

1. Open the GitHub repository
2. Go to `Settings` → `Secrets and variables` → `Actions`
3. Click `New repository secret`
4. Add the secrets listed below

## Required secrets

| Secret name | Description | Example |
|-------------|-------------|---------|
| `SMTP_HOST` | SMTP server address | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP port | `587` |
| `SMTP_USERNAME` | SMTP username / sender email | `your-email@gmail.com` |
| `SMTP_PASSWORD` | SMTP password / app password | `xxxx xxxx xxxx xxxx` |
| `EMAIL_RECIPIENTS` | Recipient email(s), comma-separated | `you@example.com, friend@example.com` |

## Gmail usage

1. Open Google Account → App Passwords
2. Create an app password for this mailer
3. Store the generated 16-character password in `SMTP_PASSWORD`

## Manual test

After setting secrets:

1. Open the Actions tab
2. Select `Daily Statistics Question Email`
3. Click `Run workflow`
4. Confirm email delivery manually

## Schedule

- Runs daily at UTC 00:00 (`09:00` Asia/Seoul)
- `workflow_dispatch` is enabled for manual runs
