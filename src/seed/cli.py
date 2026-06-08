import sys
import webbrowser

from . import tick as tick_mod
from . import render as render_mod
from .paths import GARDEN_PATH


HELP = """seed — a single seed in a pot on your windowsill.

Usage:
  seed              render the garden and open it in your browser
  seed tick         one heartbeat (advances age, updates state)
  seed render       re-render without opening the browser
  seed help         show this message

State lives at ~/.seed/state.json — read or write it from anything.
"""


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    cmd = args[0] if args else "open"

    if cmd in ("help", "-h", "--help"):
        print(HELP)
        return 0

    if cmd == "tick":
        s = tick_mod.tick()
        print(f"tick #{s.age_ticks} · stage={s.stage}")
        return 0

    if cmd == "render":
        path = render_mod.render()
        print(path)
        return 0

    if cmd == "open":
        path = render_mod.render()
        webbrowser.open(f"file://{path}")
        print(path)
        return 0

    print(f"unknown command: {cmd!r}\n", file=sys.stderr)
    print(HELP, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
