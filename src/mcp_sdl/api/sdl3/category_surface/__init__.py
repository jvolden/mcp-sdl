"""SDL3 surface functions (image loading and manipulation)."""
import importlib
from pathlib import Path

WIKI_URL = "https://wiki.libsdl.org/SDL3/CategorySurface"

OVERVIEW = """SDL surfaces are buffers of pixels in system RAM. These are useful for passing around and manipulating images that are not stored in GPU memory.

SDL_Surface makes serious efforts to manage images in various formats, and provides a reasonable toolbox for transforming the data, including copying between surfaces, filling rectangles in the image data, etc.

There is also a simple .bmp loader, SDL_LoadBMP(), and a simple .png loader, SDL_LoadPNG(). SDL itself does not provide loaders for other file formats, but there are several excellent external libraries that do, including its own satellite library, SDL_image.

In general these functions are thread-safe in that they can be called on different threads with different surfaces. You should not try to modify any surface from two threads simultaneously."""

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

CATEGORY = "surface"
FUNCTION_NAMES = list(FUNCTIONS.keys())
ENUM_NAMES = list(ENUMS.keys())
DATATYPE_NAMES = list(DATATYPES.keys())
MACRO_NAMES = list(MACROS.keys())
