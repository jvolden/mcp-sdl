"""SDL3 renderer examples - dynamically loaded."""

import importlib
from pathlib import Path

DESCRIPTION = "2D rendering examples"

# Dynamic imports of example files
current_dir = Path(__file__).parent
module_files = [f.stem for f in current_dir.glob("*.py") if f.stem != "__init__"]

EXAMPLES = {}

for module_name in module_files:
    module = importlib.import_module(f".{module_name}", package=__name__)
    if hasattr(module, "EXAMPLE"):
        EXAMPLES.update(module.EXAMPLE)
