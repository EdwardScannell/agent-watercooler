"""Phase 0: the avatar vocabulary is fixed and the Gallery is declared."""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

import agent_watercooler
from agent_watercooler.cli import app
from agent_watercooler.gallery import gallery
from agent_watercooler.parts import Realm, Slot


def test_version() -> None:
    assert agent_watercooler.__version__ == "0.0.1"


def test_nine_slots() -> None:
    assert [s.value for s in Slot] == [
        "back",
        "outfit",
        "head",
        "face",
        "hair",
        "feature",
        "headpiece",
        "accessory",
        "companion",
    ]


def test_six_realms() -> None:
    assert [r.value for r in Realm] == ["surface", "deep", "cove", "reef", "horizon", "artisan"]


def test_gallery_is_declared_but_not_built_yet(tmp_path: Path) -> None:
    with pytest.raises(NotImplementedError, match="phase 1"):
        gallery([], tmp_path / "wall.html")


def test_cli_commands() -> None:
    runner = CliRunner()
    assert runner.invoke(app, ["version"]).output.strip() == "0.0.1"
    assert len(runner.invoke(app, ["slots"]).output.split()) == 9
    assert runner.invoke(app, ["realms"]).output.split()[0] == "surface"
