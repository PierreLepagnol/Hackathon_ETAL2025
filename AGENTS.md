# Repository Guidelines

## Project Structure & Module Organization
- Root: `README.md` explains goals and roadmap.
- Assets: `assets/` stores images and static files (e.g., slides).
- Proposed (when code is added): `src/` for implementation, `tests/` for test suites, `data/` for sample inputs. Mirror module paths in `tests/`.

## Build, Test, and Development Commands
- No build system yet. Keep contributions runnable with plain tools.
- Examples (use if you introduce them):
  - Make: `make lint` (format/lint), `make test` (run tests), `make dev` (start local app/notebook).
  - Python: `python -m venv .venv && source .venv/bin/activate`, `pip install -r requirements.txt`, `pytest -q`.
  - Node: `npm ci`, `npm test`, `npm run dev`.

## Coding Style & Naming Conventions
- Markdown: 80–100c wrap; headings use `#`, lists use `-`.
- Filenames: kebab-case for documents/assets (e.g., `breton-slides-intro.md`).
- Python (if used): 4-space indent, `snake_case` for functions/vars, `PascalCase` for classes; run `ruff`/`black` if configured.
- TypeScript/JS (if used): Prettier defaults; `camelCase` for members, `PascalCase` for components.

## Testing Guidelines
- Place tests in `tests/` mirroring `src/` (e.g., `src/parser.py` → `tests/test_parser.py`).
- Prefer small, deterministic tests; add sample inputs under `data/`.
- Aim for meaningful coverage on new code paths; add fixtures where needed.

## Commit & Pull Request Guidelines
- Commits: short, imperative mood; capitalize first word (e.g., `Update README.md`, `Add slide templating`).
- Prefer focused commits over large batches; reference issues (`#12`) when applicable.
- PRs: include purpose, brief implementation notes, screenshots of UI/assets changes, and testing/validation steps.

## Security & Configuration Tips
- Do not commit secrets or private data; use environment variables or `.env` (git-ignored).
- Respect content licensing and obtain explicit consent for sourced texts.
- Large files: store in `assets/`; consider links or LFS if files exceed repo limits.

## Agent-Specific Notes
- Keep structure stable; avoid renaming `assets/` without updating references.
- Before opening a PR, run formatters/linters used by your chosen stack.
