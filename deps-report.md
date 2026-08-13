# Dependency Report

Repo: `keysoft-sample-project` — scanned path: `.`
Generated: 2026-08-13

## 1. Python — declared dependencies

Source: `pyproject.toml`, `requirements.txt`

| Dependency | Manifest / constraint | Installed (`.venv`) | Latest on PyPI | Status |
|---|---|---|---|---|
| `pytest` | `pyproject.toml` `[project.optional-dependencies] dev = ["pytest"]`, unpinned | 9.1.1 | 9.1.1 | Up to date |
| `setuptools` | `pyproject.toml` `[build-system] requires = ["setuptools>=61"]` | 79.0.1 | 84.0.0 | **Outdated** — 5 major versions behind |

`pyproject.toml` declares **zero runtime dependencies** (`dependencies = []`). Import scan of `src/orders` and `tests` confirms only the local `orders` package and stdlib (`dataclasses`, `copy`, `logging`) plus `pytest` are actually used.

## 2. Python — installed but undeclared

The following packages are present in `.venv` but appear in no manifest (`pyproject.toml`, `requirements.txt`) and are not imported anywhere in `src/` or `tests/`:

| Package | Installed | Latest on PyPI | Status |
|---|---|---|---|
| `GitPython` | 3.1.59 | 3.1.59 | Up to date, but undeclared/unused |
| `python-dotenv` | 1.2.2 | 1.2.2 | Up to date, but undeclared/unused |
| `gitdb` (GitPython dep) | 4.0.12 | 4.0.12 | Up to date, but undeclared/unused |
| `smmap` (gitdb dep) | 5.0.3 | 5.0.3 | Up to date, but undeclared/unused |

## 3. Python — transitive (pytest) dependencies

| Package | Installed | Latest on PyPI | Status |
|---|---|---|---|
| `iniconfig` | 2.3.0 | 2.3.0 | Up to date |
| `packaging` | 26.3 | 26.3 | Up to date |
| `pluggy` | 1.6.0 | 1.6.0 | Up to date |
| `Pygments` | 2.20.0 | 2.20.0 | Up to date |
| `pip` | 26.2.1 | 26.2.1 | Up to date |

## 4. Node / devcontainer

Source: `.devcontainer/devcontainer.json`, `.devcontainer/devcontainer-lock.json`

| Dependency | Declared constraint | Resolved / installed | Latest available | Status |
|---|---|---|---|---|
| `@anthropic-ai/claude-code` (npm, global) | none — bare `npm install -g @anthropic-ai/claude-code` in `postCreateCommand` | 2.1.229 | 2.1.229 | Up to date, but unpinned (no lockfile) |
| `mcr.microsoft.com/devcontainers/python` base image | `:3.11` (floating major.minor tag) | Python 3.11.15 | image line offers up to `3.14` | **Outdated** — pinned 3 minors behind the newest supported line |
| `ghcr.io/devcontainers/features/node` | `:1` (major-only, config `{}`) | locked to `1.7.1` via `devcontainer-lock.json` | `2.1.0` | **Outdated** — pinned to major `1`, current major is `2` |

## Summary

- 2 dependencies flagged outdated: `setuptools` (build backend, 79.0.1 → 84.0.0 available) and the devcontainer's Python base image (`:3.11` → `3.14` available).
- 1 devcontainer feature pinned to a stale major version: `ghcr.io/devcontainers/features/node:1` (→ `2.1.0` available).
- 4 packages installed in `.venv` (`GitPython`, `python-dotenv`, `gitdb`, `smmap`) are not referenced by any manifest or import — worth removing or declaring explicitly if intentional.
- No lockfile exists for Python dependencies; `requirements.txt` only does `-e .[dev]`, so installed versions are not pinned/reproducible beyond this snapshot.
- `@anthropic-ai/claude-code` is installed globally with no version pin in `postCreateCommand`, so container rebuilds always pull the latest npm release.
