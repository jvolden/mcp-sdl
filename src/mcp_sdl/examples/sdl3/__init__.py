"""SDL3 examples from examples.libsdl.org."""

import importlib
from pathlib import Path

# Dynamically load all example modules
current_dir = Path(__file__).parent
category_dirs = [d for d in current_dir.iterdir() if d.is_dir() and not d.name.startswith('_')]

CATEGORIES = {}
EXAMPLES = {}

for cat_dir in sorted(category_dirs):
    category = cat_dir.name
    try:
        cat_module = importlib.import_module(f".{category}", package=__name__)
        
        # Get category description from module
        if hasattr(cat_module, "DESCRIPTION"):
            CATEGORIES[category] = cat_module.DESCRIPTION
        else:
            # Fallback to generic description
            CATEGORIES[category] = f"{category.title()} examples"
        
        # Get examples from module
        if hasattr(cat_module, "EXAMPLES"):
            EXAMPLES[category] = cat_module.EXAMPLES
    except ImportError:
        pass

__all__ = ["CATEGORIES", "EXAMPLES"]
