"""The Gallery: a wall of rendered avatars. Declared in phase 0, built in phase 1."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path


def gallery(recipes: Sequence[Path], out: Path) -> Path:
    """Render each recipe and lay the avatars out on one viewable wall. Phase 1."""
    raise NotImplementedError("the Gallery lands in phase 1 (walking skeleton)")
