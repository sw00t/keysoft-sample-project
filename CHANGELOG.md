# Changelog

> Note: no tags exist in this repository (locally or on the remote), so this summarizes the full commit history instead of commits since a tag.

## Added
- Initial project scaffolding: `.gitignore`, `LICENSE`, `README.md` (778d2b6).
- Orders module (API, models, service, store), tests, `pyproject.toml`, `requirements.txt`, `TASKS.md` (349b458).
- Devcontainer configuration for the Python project (a29d9a5).
- Claude review workflow for pull requests (fb39244).
- `.claude` skills/rules, `.mcp.json`, and dependency reports (e19c938).
- CI workflow to generate a dependency report via `deps.yml` (6743603).

## Changed
- Simplified `src/orders` modules and README (c8d5092).
- Adjusted MCP configuration (682732a, 231003b).
- Reworked and simplified dependency report generation (6d290f8).
- Pinned dependency versions in `pyproject.toml` and the devcontainer, removing the lockfile in favor of pinned versions (6743603).
- Pinned the `claude-code` CLI version used in the deps workflow (007d3fa).
- Removed the GitHub review workflow added earlier (ed7316c).

## Fixed
- Fixed an MCP configuration regression (231003b).
