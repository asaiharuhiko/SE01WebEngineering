## Context

The project is a fresh Django 6.0 scaffold (no apps created yet) intended for a shared blog space. The current agentic setup in AGENTS.md describes patterns (`apps/api`, `apps/accounts`, Celery) that don't exist, and the OpenSpec specs directory is empty. Since no application code has been written, this is the ideal time to align the agent configuration with reality before feature development begins.

## Goals / Non-Goals

**Goals:**
- AGENTS.md accurately reflects the current project state and available patterns
- OpenSpec config.yaml provides project context for AI tools
- Initial spec files define the project's intended capabilities
- All agent-facing configuration files are consistent with each other
- GRADING.md is wired into the agent's awareness

**Non-Goals:**
- Creating application code (models, views, templates)
- Defining database schema or user interface design
- Setting up CI/CD or deployment infrastructure

## Decisions

1. **Keep a single flat structure** — The project currently has one Django project config dir (`blog_prj/`). Rather than inventing `apps/api` and `apps/accounts` directories, AGENTS.md should describe the actual layout and where future apps will go when created.

2. **Remove Celery reference** — Celery is not a project dependency, not in `pyproject.toml`, and not needed for this project's scope. Keeping it creates noise.

3. **Create canonical spec for agentic-setup** — This single spec captures all conventions, agent instructions, configuration, and standards in one authoritative place. Future feature specs (blog-posts, user-auth) can be added alongside it.

4. **Populate `openspec/config.yaml` context** — Using AGENTS.md style guide and GRADING.md rubric as content, so AI tools have project-awareness without needing to read those files separately.

5. **Wire GRADING.md into AGENTS.md** — It's already loaded by `opencode.json` but AGENTS.md doesn't mention it. Adding a reference ensures the grading rubric is naturally considered.

## Risks / Trade-offs

- **[Scope creep] →** Limiting non-goals explicitly. This change touches only config/docs files, not application code.
- **[Spec drift] →** The agentic-setup spec will need maintenance as the project evolves. Flag this in tasks.
- **[Over-documenting too early] →** Keeping specs minimal — one spec file with only what's necessary for agent guidance.
