# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio site built with Django 6. Single app (`portifolio`) rendering skills, projects, and a contact form with email delivery via Gmail SMTP and reCAPTCHA v2 validation.

## Environment Setup

Requires a `.env` file in the project root with these variables (read via `python-decouple`):

```
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
RECAPTCHA_PUBLIC_KEY=
RECAPTCHA_PRIVATE_KEY=
```

The `venv/` directory is already present. Activate it before running any command:

```bash
source venv/bin/activate
```

## Common Commands

```bash
# Run development server
python manage.py runserver

# Apply migrations
python manage.py migrate

# Create/apply new migration after model changes
python manage.py makemigrations && python manage.py migrate

# Run tests
python manage.py test portifolio

# Open Django shell
python manage.py shell

# Create superuser for admin panel
python manage.py createsuperuser
```

## Architecture

### Request Flow

```
URL (core/urls.py) → portifolio/urls.py → views.py → template
```

All routes are handled by the single `portifolio` app. `core/urls.py` includes `portifolio.urls` at the root path.

### Data Layer

Two models in [portifolio/models.py](portifolio/models.py):
- `Habilidade` — skill with name, icon, category, and optional description
- `Projeto` — project with title, description, image, GitHub URL, and a M2M relation to `Habilidade` via `tecnologia`

Data is stored in SQLite (`db.sqlite3`) and managed via Django admin.

### Contact Form Flow

1. `home` view renders `ContatoForm` (with reCAPTCHA) inside a modal
2. Form submits POST to `send_email_view` (`/send-email/`)
3. View validates form (including captcha), constructs `EmailMessage`, sends via Gmail SMTP
4. SMTP errors (auth, connection, timeout, network) are caught individually and surfaced as Django messages
5. Always redirects back to `home` after POST (PRG pattern)

### Templates

- `base.html` — base layout with static assets
- `home.html`, `projetos.html`, `detalhes_projeto.html` — main pages
- `components/email_modal.html` — contact form modal (rendered inside `home.html`)
- `components/email_msg_modal.html` — success/error message modal shown after form submission
- `*_old.html` files are unused backups

### Static Assets

All static files live under `portifolio/static/`:
- `css/modal.css` — styles for the contact form modal
- `js/modal.js` — modal open/close logic

### Key Settings

- `EMAIL_TIMEOUT = 15` — SMTP connection timeout in seconds
- `MEDIA_ROOT` — uploaded project images stored under `media/projetos/`
- reCAPTCHA keys loaded from `.env` via `python-decouple`
