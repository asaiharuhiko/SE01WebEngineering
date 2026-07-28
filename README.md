# SE01WebEngineering

2026/Q2 in UoA

## Overview

The Blogs application is a Django web application that allows users to create and share blog posts in a shared blog space.

### Main Features

- Display all blog posts sorted by date (most recent first)
- Display list of all authors
- Show blog posts written by a selected author
- Select a date in the calendar and display posts from that day
- Register with a unique username and password to create blog posts
- Search blog posts by title keyword

## Specification

Full specification is available at [openspec/specs/blogs/spec.md](openspec/specs/blogs/spec.md).

## Project Structure

```
├── account/          # User authentication app
│   ├── models.py
│   ├── views.py
│   └── forms.py
├── post/             # Blog posts app
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   ├── selectors.py
│   └── templates/
├── templates/        # Global templates
├── blog_prj/         # Django project settings
└── openspec/         # Specifications
```

## Setup

### Prerequisites

- Python >= 3.13
- uv (package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/asaiharuhiko/SE01WebEngineering.git
cd SE01WebEngineering

# Install dependencies
uv sync

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### Run

```bash
python manage.py runserver
```

Access at http://127.0.0.1:8000/

## Testing

```bash
# Run all tests
pytest

# Run with coverage
coverage run -m pytest
coverage report
```

## Code Quality

```bash
# Lint
ruff check

# Format
ruff format
```

## environment

- **Django**: web application framework
- **HTMX**: Async interface for dynamic updates

## Tools

| Tool | Purpose |
| --- | --- |
| uv | Package management |
| Ruff | Formatting and linting |
| coverage.py | Test coverage |
| pytest | Testing |
| git | Version control |
