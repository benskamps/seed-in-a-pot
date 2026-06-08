from datetime import datetime, timezone

from . import state as state_mod
from .paths import GARDEN_PATH, ensure_home


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>seed-in-a-pot</title>
<style>
  body {{
    margin: 0; padding: 0; min-height: 100vh;
    background: linear-gradient(180deg, #f0e7d8 0%, #e8d9bf 60%, #d6c0a2 100%);
    font-family: 'Iowan Old Style', Georgia, serif;
    display: flex; align-items: center; justify-content: center;
    color: #3a2e21;
  }}
  .windowsill {{
    width: 480px; padding: 32px; text-align: center;
  }}
  svg {{ display: block; margin: 0 auto; }}
  .label {{
    margin-top: 18px; font-size: 14px; letter-spacing: 0.04em; opacity: 0.6;
  }}
  .meta {{
    margin-top: 4px; font-size: 11px; letter-spacing: 0.06em; opacity: 0.4;
  }}
</style>
</head>
<body>
<div class="windowsill">
  <svg viewBox="0 0 200 200" width="240" height="240" aria-label="a clay pot with a seed">
    <!-- soil -->
    <ellipse cx="100" cy="125" rx="58" ry="8" fill="#5a3a23" opacity="0.9"/>
    <rect x="42" y="120" width="116" height="8" fill="#6b4527"/>
    <!-- pot body -->
    <path d="M 50 125 L 60 180 Q 100 188 140 180 L 150 125 Z" fill="#b4805a" stroke="#7a4e2f" stroke-width="1.2"/>
    <!-- pot rim -->
    <ellipse cx="100" cy="125" rx="50" ry="6" fill="#c89878" stroke="#7a4e2f" stroke-width="1.2"/>
    <ellipse cx="100" cy="125" rx="42" ry="4" fill="#3d2817"/>
    <!-- the seed (a tiny mark in the soil — Ember will replace this in M02) -->
    <circle cx="100" cy="124" r="1.5" fill="#1a1208" opacity="0.9"/>
  </svg>
  <div class="label">{stage}</div>
  <div class="meta">age: {age_ticks} ticks · water: {water_level:.2f} · sun today: {sun_today_h:.1f}h · visits: {visit_count}</div>
  <div class="meta">rendered {now}</div>
</div>
</body>
</html>
"""


def render() -> str:
    """Render the current state to ~/.seed/garden.html and return the path."""
    s = state_mod.load()
    s.visit_count += 1
    state_mod.save(s)

    html = HTML_TEMPLATE.format(
        stage=s.stage,
        age_ticks=s.age_ticks,
        water_level=s.water_level,
        sun_today_h=s.sun_today_h,
        visit_count=s.visit_count,
        now=datetime.now(timezone.utc).isoformat(timespec="seconds"),
    )
    ensure_home()
    GARDEN_PATH.write_text(html)
    return str(GARDEN_PATH)
