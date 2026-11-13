# Contributing

## Setup

```bash
python -m venv .venv && . .venv/bin/activate
make install
make check           # lint, strict types, tests with coverage (must stay >= 90%)
```

## The rules for changes

1. **Deterministic rendering.** The same recipe must always produce the same bytes.
2. **Invalid input is named.** A bad part or recipe is rejected with a specific reason,
   never silently fixed.
3. **Original content only.** Parts, characters and posts are written for this project.
4. **Every bug gets a regression test first**, in `tests/regression/`, named after it.
5. **Keep the public API typed.** `mypy --strict` must pass.

## Pull requests

- One topic per PR, with a test that fails before the change and passes after.
- Update `CHANGELOG.md` and tick the phase in `ROADMAP.md` when it is complete.
