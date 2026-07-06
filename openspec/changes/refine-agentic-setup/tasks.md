## 1. Rewrite AGENTS.md

- [x] 1.1 Remove Celery task pattern reference (not in project stack)
- [x] 1.2 Replace `apps/api` and `apps/accounts` patterns with single flat project structure
- [x] 1.3 Add `services.py` and `selectors.py` pattern (these are planned, not yet existing)
- [x] 1.4 Add reference to GRADING.md as a constraint
- [x] 1.5 Review and verify all commands listed match actual project commands
- [x] 1.6 Verify `opencode.json` instructions reference is consistent with AGENTS.md changes

## 2. Populate openspec/config.yaml

- [x] 2.1 Add `context` field describing tech stack (Django 6.0, HTMX, Python >=3.13, uv, Ruff, coverage.py, pytest)
- [x] 2.2 Add domain description: shared blog space web application
- [x] 2.3 Add convention references: services.py for business logic, selectors.py for queries

## 3. Create initial spec for agentic-setup

- [x] 3.1 Ensure spec exists at openspec/specs/agentic-setup/spec.md (created in this change)
- [x] 3.2 Sync spec from change artifacts to main openspec/specs/ directory

## 4. Verify consistency

- [x] 4.1 Confirm AGENTS.md, opencode.json, and config.yaml all reference the same stack
- [x] 4.2 Run `ruff check` on any modified .py files (none expected)
- [x] 4.3 Run `python manage.py check` to ensure project integrity
