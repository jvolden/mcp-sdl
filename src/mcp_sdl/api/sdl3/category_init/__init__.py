"""SDL3 initialization and shutdown functions."""
import importlib
from pathlib import Path

WIKI_URL = "https://wiki.libsdl.org/SDL3/CategoryInit"

# Category overview from SDL3 wiki
OVERVIEW = """All SDL programs need to initialize the library before starting to work with it.

Almost everything can simply call SDL_Init() near startup, with a handful of flags to specify subsystems to touch. These are here to make sure SDL does not even attempt to touch low-level pieces of the operating system that you don't intend to use. For example, you might be using SDL for video and input but chose an external library for audio, and in this case you would just need to leave off the SDL_INIT_AUDIO flag to make sure that external library has complete control.

Most apps, when terminating, should call SDL_Quit(). This will clean up (nearly) everything that SDL might have allocated, and crucially, it'll make sure that the display's resolution is back to what the user expects if you had previously changed it for your game.

SDL3 apps are strongly encouraged to call SDL_SetAppMetadata() at startup to fill in details about the program. This is completely optional, but it helps in small ways (we can provide an About dialog box for the macOS menu, we can name the app in the system's audio mixer, etc)."""

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

CATEGORY = "init"
FUNCTION_NAMES = list(FUNCTIONS.keys())
ENUM_NAMES = list(ENUMS.keys())
DATATYPE_NAMES = list(DATATYPES.keys())
MACRO_NAMES = list(MACROS.keys())
