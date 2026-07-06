# AGENTS.md — SE01WebEngineering

## Project scope

This is a Django app for creating blog posts in a shared blog space. See `GRADING.md` for grading rubric constraints.

## Stack (per README)
- **Django** + **HTMX** 
- **Python ≥3.13**
- **uv** for package management
- **Ruff** for linting & formatting
- **coverage.py** for test coverage

## Important project conventions

- Put business workflow logic in `services.py`, not in views or serializers (convention for future apps).
- Put reusable read/query logic in `selectors.py` (convention for future apps).

## Commands

- Run server: `python manage.py runserver`
- Run tests: `pytest`
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Lint: `ruff check`
- Format: `ruff format`

## Things that are easy to break

- View logic mixed into templates
- URL pattern ordering

## Change coupling

If you change:

- a model → also check serializers, factories, and admin
- permissions → also check both web views and API endpoints (future)

## Constraints

- Do not edit old migrations; create a new one instead.
- Do not rename API fields or URL names unless explicitly asked.
- Prefer small, targeted changes over broad refactors.

## Documentation use

- Use `openspec/specs/*` as the canonical source for technical/runtime documentation.
- For project-level conventions, examine the `context` section of `openspec/config.yaml`.
- For system-specific tasks, read the relevant capability spec under `openspec/specs/<capability>/spec.md`.
- Use `openspec/notes/*` as supplemental context only for non-normative ideas and backlog notes.
- Keep technical/runtime truth in `openspec/specs/*`; promote accepted ideas from notes into specs.
- Keep documentation up to date. If inconsistency between code and documentation is detected, report it to the user and suggest a fix.
- When a new feature is implemented or a certain fact about the system is discovered, suggest reflecting it in documentation.

## Testing expectations

Add or update tests for:

- permission changes
- view response changes

## Grading

This project is for SE01WebEngineering. 
When reviewing project code, always check `GRADING.md` for the rubric.
