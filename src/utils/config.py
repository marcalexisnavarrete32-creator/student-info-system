"""Configuration management: loads config/config.json with safe defaults."""
import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULTS = {
    "data_file": "data/students.json",
    "log_file": "logs/app.log",
    "log_level": "INFO",
}


def load_config(path=None):
    """Load config, falling back to defaults. Relative paths resolve from project root."""
    path = path or os.path.join(ROOT_DIR, "config", "config.json")
    config = dict(DEFAULTS)
    try:
        with open(path, "r") as f:
            config.update(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    for key in ("data_file", "log_file"):
        if not os.path.isabs(config[key]):
            config[key] = os.path.join(ROOT_DIR, config[key])
    return config
