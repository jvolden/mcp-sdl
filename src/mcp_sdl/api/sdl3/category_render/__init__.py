"""SDL3 2D rendering functions."""
import importlib
from pathlib import Path

WIKI_URL = "https://wiki.libsdl.org/SDL3/CategoryRender"

OVERVIEW = """Header file for SDL 2D rendering functions.

This API supports the following features:
- single pixel points
- single pixel lines
- filled rectangles
- texture images
- 2D polygons

The primitives may be drawn in opaque, blended, or additive modes.

The texture images may be drawn in opaque, blended, or additive modes. They can have an additional color tint or alpha modulation applied to them, and may also be stretched with linear interpolation.

This API is designed to accelerate simple 2D operations. You may want more functionality such as 3D polygons and particle effects, and in that case you should use SDL's OpenGL/Direct3D support, the SDL3 GPU API, or one of the many good 3D engines.

These functions must be called from the main thread."""

# Dynamically import all modules in this directory
current_dir = Path(__file__).parent
module_files = [f.stem for f in current_dir.glob("*.py") if f.stem != "__init__"]

FUNCTIONS = {}
ENUMS = {}
DATATYPES = {}
MACROS = {}

for module_name in module_files:
    module = importlib.import_module(f".{module_name}", package=__name__)

    if hasattr(module, "FUNCTION"):
        FUNCTIONS.update(module.FUNCTION)
    if hasattr(module, "ENUM"):
        ENUMS.update(module.ENUM)
    if hasattr(module, "DATATYPE"):
        DATATYPES.update(module.DATATYPE)
    if hasattr(module, "MACRO"):
        MACROS.update(module.MACRO)

CATEGORY = "render"
FUNCTION_NAMES = list(FUNCTIONS.keys())
ENUM_NAMES = list(ENUMS.keys())
DATATYPE_NAMES = list(DATATYPES.keys())
MACRO_NAMES = list(MACROS.keys())
