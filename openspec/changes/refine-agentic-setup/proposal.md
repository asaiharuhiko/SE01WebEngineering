## Why

The current agentic setup (AGENTS.md, OpenSpec config, conventions) is aspirational rather than grounded: it references patterns (`apps/api`, `apps/accounts`, Celery) that don't exist, while the OpenSpec specs directory is empty and the `config.yaml` lacks context. This creates confusion — agents receive instructions about patterns they can't apply, and have no canonical source of truth for the project's actual state and conventions. Refining the setup now, before building features, ensures agents give accurate, useful guidance throughout development.

## What Changes

- Audit and rewrite AGENTS.md to reflect only patterns that actually exist or are concretely planned
- Add `context` section to `openspec/config.yaml` with actual project stack and conventions
- Remove Celery reference from AGENTS.md (not in stack)
- Add GRADING.md reference to AGENTS.md (it's loaded by opencode.json but unused by agent)
- Rephrase "apps/api" and "apps/accounts" patterns — the project doesn't use a multi-app layout
- Create initial spec files under `openspec/specs/` for intended capabilities (blog-posts, user-auth)
- Ensure consistency between AGENTS.md, opencode.json, and config.yaml

## Capabilities

### New Capabilities
- `agentic-setup`: Project conventions, agent instructions, and documentation standards for this repo

### Modified Capabilities
- *(none — no specs exist yet)*

## Impact

- AGENTS.md: rewritten to reflect actual project structure
- openspec/config.yaml: context field populated
- openspec/specs/agentic-setup/spec.md: created as the canonical source for agent configuration
- No application code affected
