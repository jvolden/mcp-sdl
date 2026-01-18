"""SDL3 examples from examples.libsdl.org."""

import importlib
from pathlib import Path

# Example categories
CATEGORIES = {
    "renderer": "2D rendering examples",
    "input": "Input handling examples (joystick, gamepad)",
    "audio": "Audio playback examples",
    "camera": "Camera capture examples",
    "asyncio": "Asynchronous I/O examples",
    "pen": "Pen/stylus input examples",
    "misc": "Miscellaneous examples (power, clipboard, locale)",
    "demo": "Full game and application demos"
}

# Dynamically load all example modules
current_dir = Path(__file__).parent
category_dirs = [d for d in current_dir.iterdir() if d.is_dir() and not d.name.startswith('_')]

EXAMPLES = {}

for cat_dir in category_dirs:
    category = cat_dir.name
    try:
        cat_module = importlib.import_module(f".{category}", package=__name__)
        if hasattr(cat_module, "EXAMPLES"):
            EXAMPLES[category] = cat_module.EXAMPLES
    except ImportError:
        pass

__all__ = ["CATEGORIES", "EXAMPLES"]
