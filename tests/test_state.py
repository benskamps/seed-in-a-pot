import json
import os
import tempfile
from pathlib import Path
from unittest import mock

from seed import state as state_mod


def test_default_seed_state():
    s = state_mod.SeedState()
    assert s.stage == "seed"
    assert s.age_ticks == 0
    assert s.water_level == 0.0
    assert s.offerings == []


def test_save_then_load_roundtrip(tmp_path):
    fake_state = tmp_path / "state.json"
    with mock.patch.object(state_mod, "STATE_PATH", fake_state), \
         mock.patch("seed.state.ensure_home", return_value=tmp_path):
        s = state_mod.SeedState(age_ticks=42, water_level=0.7, stage="sprout")
        state_mod.save(s)
        loaded = state_mod.load()
        assert loaded.age_ticks == 42
        assert loaded.water_level == 0.7
        assert loaded.stage == "sprout"


def test_load_returns_default_when_missing(tmp_path):
    fake_state = tmp_path / "does-not-exist.json"
    with mock.patch.object(state_mod, "STATE_PATH", fake_state):
        s = state_mod.load()
        assert s.age_ticks == 0
        assert s.stage == "seed"
