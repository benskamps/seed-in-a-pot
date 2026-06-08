import json
import time
from dataclasses import dataclass, asdict, field
from typing import List

from .paths import STATE_PATH, ensure_home


@dataclass
class SeedState:
    seeded_at: float = field(default_factory=time.time)
    last_tick_at: float = field(default_factory=time.time)
    age_ticks: int = 0
    stage: str = "seed"
    water_level: float = 0.0
    sun_today_h: float = 0.0
    offerings: List[str] = field(default_factory=list)
    visit_count: int = 0


def load() -> SeedState:
    if not STATE_PATH.exists():
        return SeedState()
    raw = json.loads(STATE_PATH.read_text())
    return SeedState(**{k: v for k, v in raw.items() if k in SeedState.__dataclass_fields__})


def save(state: SeedState) -> None:
    ensure_home()
    STATE_PATH.write_text(json.dumps(asdict(state), indent=2))
