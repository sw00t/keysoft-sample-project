# Dependency Report

**Verdict: FAIL** (1 High-severity finding)

## Findings

| # | Dependency | Manifest | Declared constraint | Issue | Severity |
|---|---|---|---|---|---|
| 1 | `@anthropic-ai/claude-code` (npm) | `.devcontainer/devcontainer.json` (`postCreateCommand`: `npm install -g @anthropic-ai/claude-code`) | none — bare `npm install -g` | Globally installed with no version pin and no lockfile anywhere in the repo. Every container build silently pulls whatever is newest on npm at that moment, for a tool with broad code-execution capability. Not reproducible, not auditable. | **High** |
| 2 | `pytest` | `pyproject.toml` (`dev = ["pytest"]`) | unpinned | No version specifier and no lockfile (`requirements.txt` just does `-e .[dev]`). A breaking pytest release can silently change dev/CI behavior. | Medium |
| 3 | `mcr.microsoft.com/devcontainers/python` base image | `.devcontainer/devcontainer.json` | `:3.11` (floating tag) | Only a major.minor tag, no patch/digest pin, no lock. Rebuilds can pick up a different underlying image over time. | Medium |
| 4 | `ghcr.io/devcontainers/features/node` | `.devcontainer/devcontainer.json` | `{}` (no version key — fully open) | Source declaration is completely unpinned; only mitigated by `.devcontainer/devcontainer-lock.json`, which does resolve it to `1.7.1` with a SHA-256 digest. Lower risk because the lock file exists, but the intent isn't pinned at the source. | Low |
| 5 | `setuptools` | `pyproject.toml` (`[build-system] requires`) | `>=61` | Open-ended lower bound only, no upper bound. Standard practice for a build backend and low practical risk, but technically unpinned. | Low |

## Notes

- `pyproject.toml` declares **zero runtime dependencies** (`dependencies = []`); the project only imports its own `orders` package and the stdlib, confirmed via `grep` on `src/orders/api.py` and related modules.
- No `package.json`, `poetry.lock`, `Pipfile.lock`, or Python requirements lockfile exists anywhere in the repo — the only reproducibility anchor at all is `.devcontainer/devcontainer-lock.json`, which covers just the Node devcontainer feature.
- Installed versions in `.venv` at time of scan: `pytest 9.1.1`, `setuptools 79.0.1`, `pip 26.2.1`, plus pytest's transitive deps `iniconfig 2.3.0`, `packaging 26.3`, `pluggy 1.6.0`, `Pygments 2.20.0` — all currently up to date, but none are pinned or locked, so this snapshot isn't guaranteed to reproduce on a future install.

## Why FAIL

Finding #1 (`@anthropic-ai/claude-code` installed globally, unpinned, unlocked, via `npm install -g` in `postCreateCommand`) is rated High: it is a privileged, code-executing tool installed with no version control whatsoever, on every container build. Per the verdict rule (FAIL if anything is high), this alone fails the report.
