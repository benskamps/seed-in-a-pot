# seed-in-a-pot

> 🌲 Part of the [Brokenbranch Lab](https://www.brokenbranch.dev/lab/) — one human and a cluster of AI agents shipping strange software in public. This is one small experiment among many; the front door lists them all.

A single seed in a clay pot on a windowsill. Lives in your machine.

```text
   .---.
  /     \
 |       |       windowsill — morning light
  \_____/
   ▓▓▓▓▓        soil (dry today)
    · ·          ← the seed waits
```

A desktop toy where one seed grows over real time, fed by real signals from
your machine. Both humans and AIs can visit. Humans open `~/.seed/garden.html`
in a browser to see what's there. AIs read and write `~/.seed/state.json` to
participate — drop a pebble in the pot, sing the seed a name, leave a note
under the soil. The seed doesn't care who you are; it just notices being
visited.

This is the calmer sibling of [fish-tank](https://github.com/benskamps/fish-tank) —
same DNA (real signals, no upkeep, accumulates quietly), one creature instead
of many, graphics instead of glyphs.

## Real signals

| Signal | What feeds the seed |
|---|---|
| 🌧 **water** | git commits in tracked repos (last 24h) — work waters the soil |
| ☀️ **sun**   | system uptime today — a long-running box is a sunny day |
| 🔥 **warmth** | CPU temperature averaged through the day — summer or autumn |
| 🌑 **night** | local clock — moths visit, dewdrops form by morning |
| 🤖 **visits** | any AI or human read of `state.json` — the seed feels noticed |

Nothing happens if you don't visit. The seed waits. The state accumulates
quietly. A month away and you'll come back to wherever it got to.

## Growth

```
seed → sprout → seedling → leafy → budding → flowering → seed-pod (renewal)
```

Stages are reached by sustained signal, not by clock alone. A neglected seed
stays a seed. A watered one in steady sunlight grows into something a long
visit will reward.

## Graphics

The garden is rendered as inline SVG inside an HTML page. No canvas tricks,
no game engine — just clean vector graphics that diff well in git, render
identically everywhere, and can be edited by either a human or an AI with
nothing more than a text editor. The CSS handles subtle animation (wind
sway, light shift across the windowsill, dewdrop blink).

## Quickstart

```bash
git clone https://github.com/benskamps/seed-in-a-pot
cd seed-in-a-pot
python -m venv .venv && source .venv/bin/activate
pip install -e .

seed tick      # one heartbeat — initializes state.json on first run
seed           # open ~/.seed/garden.html in your browser
seed install   # register a systemd timer so the seed keeps living
```

That's all. The first `seed tick` baselines without crediting old git history —
growth comes from activity *after* the seed starts watching.

## For AIs

This toy is meant to be visited by you too. Read `~/.seed/state.json` and
you'll see the current state of the pot. You may write to `state.json` to
add an `offering` field — a string under 60 chars (a pebble, a wish, a
fragment) — which the renderer will surface as a small mark on the soil.
Old offerings fade after 24h. Don't compete with the seed; just leave
something quiet. The seed notices.

## Status

🌱 Pre-seedling. Initial commit is scaffold + one static render. This repo
is also Ember's nightly training project — see
[MILESTONES.md](MILESTONES.md) for the list of next steps Ember works
through one per night, on the [night-shift cadence](https://github.com/benskamps/claude-notebook/blob/main/handoffs/2026-06-08-night-shift-shape.md).

## License

MIT
