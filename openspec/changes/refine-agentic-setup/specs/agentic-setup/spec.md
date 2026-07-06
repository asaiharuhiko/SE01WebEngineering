## ADDED Requirements

### Requirement: Project conventions are documented in AGENTS.md
The project SHALL maintain an AGENTS.md file at the repository root that accurately describes the current project scope, stack, conventions, commands, and constraints.

#### Scenario: AGENTS.md reflects actual project structure
- **WHEN** an AI agent reads AGENTS.md
- **THEN** all referenced patterns, apps, and tools SHALL exist in the project or be concretely planned

#### Scenario: AGENTS.md includes test commands
- **WHEN** an AI agent needs to run tests
- **THEN** AGENTS.md SHALL provide the exact command: `pytest`

#### Scenario: AGENTS.md includes grading awareness
- **WHEN** an AI agent reviews code or plans features
- **THEN** AGENTS.md SHALL reference GRADING.md as a constraint

### Requirement: openspec/config.yaml provides project context
The openspec/config.yaml file SHALL include a populated `context` field describing the project's tech stack, conventions, and domain.

#### Scenario: Context is populated
- **WHEN** a tool reads openspec/config.yaml
- **THEN** the `context` field SHALL contain accurate information about the Django + HTMX stack, Python >=3.13, uv packaging, and the shared blog space domain

### Requirement: Specs are the canonical source of truth
The openspec/specs/ directory SHALL contain the canonical technical and runtime documentation for the project.

#### Scenario: Specs exist for project conventions
- **WHEN** an AI agent needs to understand project conventions
- **THEN** it SHALL consult openspec/specs/agentic-setup/spec.md as the authoritative source

### Requirement: Configuration files are consistent
The opencode.json, AGENTS.md, and openspec/config.yaml files SHALL not contradict each other.

#### Scenario: Stack references match
- **WHEN** comparing AGENTS.md and openspec/config.yaml
- **THEN** both SHALL reference the same tech stack (Django, HTMX, Python >=3.13, uv, Ruff, coverage.py, pytest)
