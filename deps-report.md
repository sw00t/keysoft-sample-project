# Dependency Report

Generated: 2026-08-07
Scope: `.` (repo root, `keysoft-sample-project`)

## Summary

This is a small Python project (`src/orders`) with **no runtime dependencies**
declared, one **dev dependency** (`pytest`, unpinned), and a devcontainer that
pulls a Node.js feature. Everything currently installed is up to date except
`setuptools`, which is behind upstream. No JavaScript/`package.json`
dependencies exist in this repo.

## Manifests found

| File | Role |
|---|---|
| `pyproject.toml` | Project metadata, build system, `dev` extra (pytest) |
| `requirements.txt` | Installs the project editable (`-e .[dev]`) |
| `.devcontainer/devcontainer.json` | Dev environment image + features |
| `.devcontainer/devcontainer-lock.json` | Locked feature version |

No `poetry.lock`, `Pipfile.lock`, or `package.json` present — the project has
no lockfile for Python deps, and no JS dependencies at all.

## Python dependencies

### Direct (declared in `pyproject.toml`)

| Package | Declared constraint | Installed | Latest (PyPI) | Status |
|---|---|---|---|---|
| *(runtime)* | `dependencies = []` | — | — | none declared |
| pytest | `dev` extra, unpinned | 9.1.1 | 9.1.1 | up to date |

### Transitive (pulled in by pytest, resolved in `.venv`)

| Package | Installed | Latest (PyPI) | Status |
|---|---|---|---|
| iniconfig | 2.3.0 | 2.3.0 | up to date |
| packaging | 26.3 | 26.3 | up to date |
| pluggy | 1.6.0 | 1.6.0 | up to date |
| Pygments | 2.20.0 | 2.20.0 | up to date |

### Build/tooling

| Package | Installed | Latest (PyPI) | Status |
|---|---|---|---|
| setuptools | 79.0.1 | 83.0.0 | **outdated** (build-system requires `>=61`, constraint still satisfied, but 4 minor releases behind) |
| pip | 26.2.1 | 26.2.1 | up to date |

**Flag:** `pyproject.toml`'s `dependencies` list is empty and `pytest` has no
version pin (`dev = ["pytest"]`). That means every fresh install picks up
whatever the latest pytest is at install time, with no lockfile to make
installs reproducible — worth pinning (e.g. `pytest>=9,<10`) or adding a
lockfile if reproducible CI/dev environments matter.

## Devcontainer dependencies

| Item | Declared | Resolved/Locked | Notes |
|---|---|---|---|
| Base image | `mcr.microsoft.com/devcontainers/python:3.11` | tag `3.11` (floating) | Not pinned to a digest — rebuilds can silently pick up a newer image. Python 3.10 (the project's minimum per `requires-python = ">=3.10"`) reaches end-of-life 2026-10-31, a few months out. |
| Feature: `ghcr.io/devcontainers/features/node` | `:1` (major-version floating) | locked to `1.7.1` | **Outdated major line available**: upstream `devcontainer-features/node` is now at `2.1.0` on its main branch. Staying on `1.7.1` is fine if intentional, but the major bump hasn't been evaluated/adopted. |
| `@anthropic-ai/claude-code` (npm, via `postCreateCommand`) | installed unpinned (`npm install -g`) | n/a — not locked anywhere | Every container rebuild grabs whatever is newest on npm at that moment; no version is recorded, so this isn't reproducible and can't be "flagged outdated" from the repo alone. |

## Recommendations

1. Pin `pytest` (and ideally generate a lockfile, e.g. via `pip-compile` or
   `uv pip compile`) so dev environments are reproducible.
2. Bump `setuptools` in the venv/build environment (79.0.1 → 83.0.0); the
   `>=61` constraint is loose enough that this is just a routine update.
3. Decide whether to move the devcontainer's Node feature from the `1.x`
   line (`1.7.1`) to `2.1.0`, or pin explicitly to `1.7.1` to make the
   "floating major version" intentional rather than implicit.
4. Consider pinning the devcontainer base image to a digest (or at least a
   more specific tag) instead of the floating `python:3.11` tag, and note
   that the project's Python 3.10 floor is approaching EOL (2026-10-31).
5. Pin `@anthropic-ai/claude-code`'s version in `postCreateCommand` if
   reproducible container builds matter.

## Method

- Enumerated manifests via filesystem search for common Python/JS
  dependency files.
- Read `pyproject.toml` / `requirements.txt` directly for declared deps.
- Compared installed versions (`pip show`, `pip list`) against latest
  releases (`pip index versions <pkg>`, which queries PyPI) for every
  installed package.
- Checked devcontainer feature/image pins against the upstream
  `devcontainers/features` source repo.
