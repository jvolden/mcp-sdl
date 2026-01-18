"""SDL3 video subsystem functions (windows, displays)."""
import importlib
from pathlib import Path

WIKI_URL = "https://wiki.libsdl.org/SDL3/CategoryVideo"

OVERVIEW = """SDL's video subsystem is largely interested in abstracting window management from the underlying operating system. You can create windows, manage them in various ways, set them fullscreen, and get events when interesting things happen with them, such as the mouse or keyboard interacting with a window.

The video subsystem is also interested in abstracting away some platform-specific differences in OpenGL: context creation, swapping buffers, etc. This may be crucial to your app, but also you are not required to use OpenGL at all. In fact, SDL can provide rendering to those windows as well, either with an easy-to-use 2D API or with a more-powerful GPU API. Of course, it can simply get out of your way and give you the window handles you need to use Vulkan, Direct3D, Metal, or whatever else you like directly, too.

The video subsystem covers a lot of functionality, out of necessity, so it is worth perusing the list of functions just to see what's available, but most apps can get by with simply creating a window and listening for events, so start with SDL_CreateWindow() and SDL_PollEvent()."""

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

CATEGORY = "video"
FUNCTION_NAMES = list(FUNCTIONS.keys())
ENUM_NAMES = list(ENUMS.keys())
DATATYPE_NAMES = list(DATATYPES.keys())
MACRO_NAMES = list(MACROS.keys())
