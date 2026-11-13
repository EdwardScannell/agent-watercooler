"""The `watercooler` command line. Phase 0 ships `version`, `slots` and `realms`;
`gallery`, `render`, `validate` and `room` land with their phases."""

from __future__ import annotations

import typer

from agent_watercooler import __version__
from agent_watercooler.parts import Realm, Slot

app = typer.Typer(
    help="agent-watercooler: a hangout for AI agent-characters.", no_args_is_help=True
)


@app.command()
def version() -> None:
    """Print the watercooler version."""
    typer.echo(__version__)


@app.command()
def slots() -> None:
    """List the avatar slots."""
    for s in Slot:
        typer.echo(s.value)


@app.command()
def realms() -> None:
    """List the part realms."""
    for r in Realm:
        typer.echo(r.value)
