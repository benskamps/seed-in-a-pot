from pathlib import Path

SEED_HOME = Path.home() / ".seed"
STATE_PATH = SEED_HOME / "state.json"
GARDEN_PATH = SEED_HOME / "garden.html"


def ensure_home() -> Path:
    SEED_HOME.mkdir(parents=True, exist_ok=True)
    return SEED_HOME
