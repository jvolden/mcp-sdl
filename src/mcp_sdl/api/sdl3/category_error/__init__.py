"""SDL3 error handling functions."""
import importlib
from pathlib import Path

WIKI_URL = "https://wiki.libsdl.org/SDL3/CategoryError"

OVERVIEW = """Simple error message routines for SDL.

Most apps will interface with these APIs in exactly one function: when almost any SDL function call reports failure, you can get a human-readable string of the problem from SDL_GetError().

These strings are maintained per-thread, and apps are welcome to set their own errors, which is popular when building libraries on top of SDL for other apps to consume. These strings are set by calling SDL_SetError().

A common usage pattern is to have a function that returns true for success and false for failure, and do this when something fails:

```
if (something_went_wrong) {
   return SDL_SetError("The thing broke in this specific way: %d", errcode);
}
```

It's also common to just return `false` in this case if the failing thing is known to call SDL_SetError(), so errors simply propagate through."""

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

CATEGORY = "error"
FUNCTION_NAMES = list(FUNCTIONS.keys())
ENUM_NAMES = list(ENUMS.keys())
DATATYPE_NAMES = list(DATATYPES.keys())
MACRO_NAMES = list(MACROS.keys())
