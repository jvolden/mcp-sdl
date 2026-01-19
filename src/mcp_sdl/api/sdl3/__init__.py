"""SDL3 API reference - aggregates all SDL3 function categories."""

import importlib
from pathlib import Path
from types import ModuleType

# Dynamically discover and load category modules
current_dir = Path(__file__).parent
category_dirs = [
    d.name for d in current_dir.iterdir()
    if d.is_dir() and d.name.startswith("category_") and not d.name.startswith('_')
]

CATEGORY_MODULES: dict[str, ModuleType] = {}
SDL3_FUNCTIONS = {}
SDL3_CATEGORIES = {}

for category_dir in sorted(category_dirs):
    # Extract category name from "category_name" -> "name"
    category_name = category_dir.replace("category_", "")
    try:
        module = importlib.import_module(f".{category_dir}", package=__name__)
        CATEGORY_MODULES[category_name] = module

        # Aggregate functions from this category
        if hasattr(module, "FUNCTIONS"):
            SDL3_FUNCTIONS.update(module.FUNCTIONS)

        # Add category organization
        if hasattr(module, "FUNCTION_NAMES"):
            SDL3_CATEGORIES[category_name] = module.FUNCTION_NAMES
    except ImportError:
        pass  # Skip categories that fail to import

# Export for easy access
__all__ = ["SDL3_FUNCTIONS", "SDL3_CATEGORIES", "CATEGORY_MODULES"]
