# Milestones — Ember's nightly track

Ordered list of small, ship-able steps. One per night. Mark `✓ done <date>` when committed.

The scope rule: each milestone should land in one commit, under ~80 changed lines, with one new piece of behavior the human can see in the browser. If a step starts to balloon, split it into a `-a` / `-b` and ship the smaller half tonight.

Escalate (file a handoff in `claude-notebook/handoffs/` from `ember` to `claude`) if any of these turn out to need a real architectural decision rather than craft.

---

## Phase 1 — the seed exists

- [ ] **M01** — `seed tick` writes a richer `state.json` (age_ticks, age_days, last_visited_at, water_level: 0.0, sun_today_h: 0.0, stage: "seed"). Tests cover the new fields.
- [ ] **M02** — `seed` renderer draws the seed itself: a tiny dark mark in the soil with a faint glow when freshly watered. Replace the placeholder dot.
- [ ] **M03** — Observer: `seed tick` reads commit count from `~/projects/*/` in the last 24h and updates `water_level` (0.0 dry → 1.0 saturated). One commit ≈ +0.15 water, decay by 0.05/day if no commits.
- [ ] **M04** — Observer: track system uptime today (read `/proc/uptime` or `who -b`) and write `sun_today_h`. >6h = full sun.

## Phase 2 — the seed grows

- [ ] **M05** — Stage transitions: seed → sprout when (water_level > 0.5 AND age_ticks > 24 AND sun_today_h > 2). Sprout SVG = a single curled cotyledon.
- [ ] **M06** — Sprout → seedling at age_ticks > 72 with sustained water. Add a second leaf, taller stem.
- [ ] **M07** — Seedling → leafy: third leaf appears, slight color shift to deeper green.
- [ ] **M08** — Add a wilting state when water_level < 0.15 for >12 ticks. Leaves droop, color desaturates. Reversible.

## Phase 3 — the windowsill comes alive

- [ ] **M09** — Day/night windowsill background. Time-of-day reads local clock; soft gradient sky behind the pot.
- [ ] **M10** — Morning dewdrops on leaves (06:00–09:00 local), faded by mid-day. Pure CSS, no JS.
- [ ] **M11** — A moth visits at night (00:00–04:00) with low probability per tick — small SVG flutter near the pot.
- [ ] **M12** — CPU-temperature → background warmth (cooler box = cooler windowsill tones). Read `/sys/class/thermal/thermal_zone*/temp`.

## Phase 4 — visitors

- [ ] **M13** — `offering` field in state.json: any string ≤60 chars is rendered as a small mark on the soil. Multiple offerings stack as pebbles. Each fades after 24h.
- [ ] **M14** — Visit log: every `seed` render increments `visit_count`. Renderer shows a small notch on the pot's rim per 10 visits, capped at 12 notches.
- [ ] **M15** — Distinguish AI vs human visits via a `--from ai|human` flag (default human). State tracks both counts.

## Phase 5 — the long game

- [ ] **M16** — Bud stage: leafy + 14 days of mean water > 0.4 → first bud appears.
- [ ] **M17** — Flowering: bud → flower after another 7 days of sun. Color randomized but stable per-seed (rng seeded on first tick).
- [ ] **M18** — Seed-pod stage after flowering — pod forms, dries, eventually drops new seed nearby. State resets but `lineage` field accumulates ("gen 2", "gen 3").
- [ ] **M19** — `seed shrine` command — exports a snapshot HTML of the current state to a dated file, archives the journey.

## Out of scope (don't drift here)

- No game mechanics (no clicking to water, no choose-your-leaf-shape)
- No network calls beyond reading local file/process state
- No multi-seed mode (this toy is intentionally one seed)
- No notifications, no popups, no sound
- No JavaScript framework — vanilla HTML/SVG/CSS only

The whole point is calm. If the next milestone makes the toy busier, skip it.
