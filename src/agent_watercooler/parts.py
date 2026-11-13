"""The avatar vocabulary for The Rigging Room.

Phase 0 fixes the slots an avatar is assembled from and the realms parts belong to.
The parts catalog itself lands in phase 2 (see ROADMAP.md).
"""

from __future__ import annotations

from enum import StrEnum


class Slot(StrEnum):
    """Assembly points. A character fills at most one part per slot."""

    BACK = "back"
    OUTFIT = "outfit"
    HEAD = "head"
    FACE = "face"
    HAIR = "hair"
    FEATURE = "feature"
    HEADPIECE = "headpiece"
    ACCESSORY = "accessory"
    COMPANION = "companion"


class Realm(StrEnum):
    """Thematic families a part belongs to."""

    SURFACE = "surface"
    DEEP = "deep"
    COVE = "cove"
    REEF = "reef"
    HORIZON = "horizon"
    ARTISAN = "artisan"
