"""SDL examples package."""

import importlib
from pathlib import Path

# Discover all example libraries
current_dir = Path(__file__).parent
library_dirs = [d for d in current_dir.iterdir() if d.is_dir() and not d.name.startswith('_')]

EXAMPLES = {}

for lib_dir in library_dirs:
    lib_name = lib_dir.name
    try:
        lib_module = importlib.import_module(f".{lib_name}", package=__name__)
        if hasattr(lib_module, "EXAMPLES"):
            EXAMPLES[lib_name] = lib_module.EXAMPLES
    except ImportError:
        pass

__all__ = ["EXAMPLES"]
