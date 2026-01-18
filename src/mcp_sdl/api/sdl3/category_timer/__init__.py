"""SDL3 timer and delay functions."""
import importlib
from pathlib import Path

WIKI_URL = "https://wiki.libsdl.org/SDL3/CategoryTimer"

OVERVIEW = """SDL provides time management functionality. It is useful for dealing with (usually) small durations of time.

This is not to be confused with calendar time management, which is provided by CategoryTime.

This category covers measuring time elapsed (SDL_GetTicks(), SDL_GetPerformanceCounter()), putting a thread to sleep for a certain amount of time (SDL_Delay(), SDL_DelayNS(), SDL_DelayPrecise()), and firing a callback function after a certain amount of time has elapsed (SDL_AddTimer(), etc).

There are also useful macros to convert between time units, like SDL_SECONDS_TO_NS() and such."""

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

CATEGORY = "timer"
FUNCTION_NAMES = list(FUNCTIONS.keys())
ENUM_NAMES = list(ENUMS.keys())
DATATYPE_NAMES = list(DATATYPES.keys())
MACRO_NAMES = list(MACROS.keys())
