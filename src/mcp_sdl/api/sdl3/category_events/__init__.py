"""SDL3 event handling functions."""
import importlib
from pathlib import Path

WIKI_URL = "https://wiki.libsdl.org/SDL3/CategoryEvents"

OVERVIEW = """Event queue management.

It's extremely common--often required--that an app deal with SDL's event queue. Almost all useful information about interactions with the real world flow through here: the user interacting with the computer and app, hardware coming and going, the system changing in some way, etc.

An app generally takes a moment, perhaps at the start of a new frame, to examine any events that have occurred since the last time and process or ignore them. This is generally done by calling SDL_PollEvent() in a loop until it returns false (or, if using the main callbacks, events are provided one at a time in calls to SDL_AppEvent() before the next call to SDL_AppIterate(); in this scenario, the app does not call SDL_PollEvent() at all).

There is other forms of control, too: SDL_PeepEvents() has more functionality at the cost of more complexity, and SDL_WaitEvent() can block the process until something interesting happens, which might be beneficial for certain types of programs on low-power hardware. One may also call SDL_AddEventWatch() to set a callback when new events arrive.

The app is free to generate their own events, too: SDL_PushEvent allows the app to put events onto the queue for later retrieval; SDL_RegisterEvents can guarantee that these events have a type that isn't in use by other parts of the system."""

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

CATEGORY = "events"
FUNCTION_NAMES = list(FUNCTIONS.keys())
ENUM_NAMES = list(ENUMS.keys())
DATATYPE_NAMES = list(DATATYPES.keys())
MACRO_NAMES = list(MACROS.keys())
