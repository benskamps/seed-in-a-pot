import time

from . import state as state_mod


def tick() -> state_mod.SeedState:
    """One heartbeat. M03+M04 wire real signals in here."""
    s = state_mod.load()
    s.age_ticks += 1
    s.last_tick_at = time.time()
    state_mod.save(s)
    return s
