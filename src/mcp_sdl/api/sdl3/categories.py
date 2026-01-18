"""Complete list of SDL3 categories with descriptions.

This module provides a comprehensive listing of all SDL3 API categories,
including those not yet implemented in this server. Used for discovery
and navigation when functions are not found.
"""

# Categories currently implemented in this server
IMPLEMENTED_CATEGORIES = {
    "init",
    "video",
    "render",
    "events",
    "keyboard",
    "mouse",
    "error",
    "surface",
    "timer",
}

# Complete SDL3 category catalog from wiki
SDL3_CATEGORY_CATALOG = {
    # === BASICS ===
    "main": {
        "name": "Application Entry Points",
        "description": "Main function and application entry points for SDL programs",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryMain",
        "implemented": False,
    },
    "init": {
        "name": "Initialization and Shutdown",
        "description": "Initialize and shut down SDL subsystems",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryInit",
        "implemented": True,
    },
    "hints": {
        "name": "Configuration Variables",
        "description": "Configuration hints to control SDL behavior",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryHints",
        "implemented": False,
    },
    "properties": {
        "name": "Object Properties",
        "description": "Generic property system for SDL objects",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryProperties",
        "implemented": False,
    },
    "error": {
        "name": "Error Handling",
        "description": "Error message management and retrieval",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryError",
        "implemented": True,
    },
    "log": {
        "name": "Log Handling",
        "description": "Logging and debug output functions",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryLog",
        "implemented": False,
    },
    "assert": {
        "name": "Assertions",
        "description": "Runtime assertion macros for debugging",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryAssert",
        "implemented": False,
    },
    "version": {
        "name": "Querying SDL Version",
        "description": "Query SDL library version information",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryVersion",
        "implemented": False,
    },

    # === VIDEO ===
    "video": {
        "name": "Display and Window Management",
        "description": "Window creation, display management, and video modes",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryVideo",
        "implemented": True,
    },
    "render": {
        "name": "2D Accelerated Rendering",
        "description": "Hardware-accelerated 2D rendering API",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryRender",
        "implemented": True,
    },
    "pixels": {
        "name": "Pixel Formats and Conversion",
        "description": "Pixel format definitions and conversion routines",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryPixels",
        "implemented": False,
    },
    "blendmode": {
        "name": "Blend Modes",
        "description": "Blend mode definitions for rendering",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryBlendMode",
        "implemented": False,
    },
    "rect": {
        "name": "Rectangle Functions",
        "description": "Rectangle manipulation and intersection functions",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryRect",
        "implemented": False,
    },
    "surface": {
        "name": "Surface Creation and Drawing",
        "description": "Software surface creation and manipulation",
        "wiki": "https://wiki.libsdl.org/SDL3/CategorySurface",
        "implemented": True,
    },
    "clipboard": {
        "name": "Clipboard Handling",
        "description": "System clipboard text and data access",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryClipboard",
        "implemented": False,
    },
    "vulkan": {
        "name": "Vulkan Support",
        "description": "Vulkan API integration and window support",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryVulkan",
        "implemented": False,
    },
    "metal": {
        "name": "Metal Support",
        "description": "Apple Metal API integration",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryMetal",
        "implemented": False,
    },
    "camera": {
        "name": "Camera Support",
        "description": "Camera device access and video capture",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryCamera",
        "implemented": False,
    },

    # === INPUT EVENTS ===
    "events": {
        "name": "Event Handling",
        "description": "Event queue management and polling",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryEvents",
        "implemented": True,
    },
    "keyboard": {
        "name": "Keyboard Support",
        "description": "Keyboard input and text input management",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryKeyboard",
        "implemented": True,
    },
    "keycode": {
        "name": "Keyboard Keycodes",
        "description": "Virtual key codes for keyboard input",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryKeycode",
        "implemented": False,
    },
    "scancode": {
        "name": "Keyboard Scancodes",
        "description": "Physical key scancodes for keyboard layout",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryScancode",
        "implemented": False,
    },
    "mouse": {
        "name": "Mouse Support",
        "description": "Mouse input, cursor, and button state",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryMouse",
        "implemented": True,
    },
    "joystick": {
        "name": "Joystick Support",
        "description": "Joystick and game controller input",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryJoystick",
        "implemented": False,
    },
    "gamepad": {
        "name": "Gamepad Support",
        "description": "Game controller mapping and input",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryGamepad",
        "implemented": False,
    },
    "touch": {
        "name": "Touch Support",
        "description": "Touch screen and gesture input",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryTouch",
        "implemented": False,
    },
    "pen": {
        "name": "Pen Support",
        "description": "Pen tablet and stylus input",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryPen",
        "implemented": False,
    },
    "sensor": {
        "name": "Sensors",
        "description": "Device sensor access (accelerometer, gyroscope)",
        "wiki": "https://wiki.libsdl.org/SDL3/CategorySensor",
        "implemented": False,
    },
    "hidapi": {
        "name": "HIDAPI",
        "description": "Low-level HID device access",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryHIDAPI",
        "implemented": False,
    },

    # === FORCE FEEDBACK ===
    "haptic": {
        "name": "Force Feedback Support",
        "description": "Haptic feedback and rumble effects",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryHaptic",
        "implemented": False,
    },

    # === AUDIO ===
    "audio": {
        "name": "Audio Playback and Recording",
        "description": "Audio device management, playback, and recording",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryAudio",
        "implemented": False,
    },

    # === GPU ===
    "gpu": {
        "name": "3D Rendering and GPU Compute",
        "description": "Modern GPU API for 3D rendering and compute",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryGPU",
        "implemented": False,
    },

    # === THREADS ===
    "thread": {
        "name": "Thread Management",
        "description": "Thread creation and management",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryThread",
        "implemented": False,
    },
    "mutex": {
        "name": "Thread Synchronization",
        "description": "Mutexes, semaphores, and condition variables",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryMutex",
        "implemented": False,
    },
    "atomic": {
        "name": "Atomic Operations",
        "description": "Lock-free atomic operations",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryAtomic",
        "implemented": False,
    },

    # === TIME ===
    "timer": {
        "name": "Timer Support",
        "description": "High-resolution timers and delays",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryTimer",
        "implemented": True,
    },
    "time": {
        "name": "Date and Time",
        "description": "Date, time, and calendar functions",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryTime",
        "implemented": False,
    },

    # === FILE AND I/O ===
    "filesystem": {
        "name": "Filesystem Access",
        "description": "File and directory operations",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryFilesystem",
        "implemented": False,
    },
    "storage": {
        "name": "Storage Abstraction",
        "description": "Abstract storage interface for files",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryStorage",
        "implemented": False,
    },
    "iostream": {
        "name": "I/O Streams",
        "description": "Stream-based I/O operations",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryIOStream",
        "implemented": False,
    },
    "asyncio": {
        "name": "Async I/O",
        "description": "Asynchronous I/O operations",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryAsyncIO",
        "implemented": False,
    },

    # === PLATFORM AND CPU ===
    "platform": {
        "name": "Platform Detection",
        "description": "Platform and OS detection macros",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryPlatform",
        "implemented": False,
    },
    "cpuinfo": {
        "name": "CPU Feature Detection",
        "description": "CPU capabilities and feature detection",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryCPUInfo",
        "implemented": False,
    },
    "intrin": {
        "name": "Compiler Intrinsics",
        "description": "Compiler-specific intrinsics detection",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryIntrin",
        "implemented": False,
    },
    "endian": {
        "name": "Byte Order and Swapping",
        "description": "Endianness detection and byte swapping",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryEndian",
        "implemented": False,
    },
    "bits": {
        "name": "Bit Manipulation",
        "description": "Bit manipulation utilities",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryBits",
        "implemented": False,
    },

    # === ADDITIONAL ===
    "loadso": {
        "name": "Shared Object Management",
        "description": "Dynamic library loading (DLL/SO)",
        "wiki": "https://wiki.libsdl.org/SDL3/CategorySharedObject",
        "implemented": False,
    },
    "process": {
        "name": "Process Control",
        "description": "Process creation and management",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryProcess",
        "implemented": False,
    },
    "power": {
        "name": "Power Management",
        "description": "Battery and power status information",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryPower",
        "implemented": False,
    },
    "messagebox": {
        "name": "Message Boxes",
        "description": "Native message box dialogs",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryMessageBox",
        "implemented": False,
    },
    "dialog": {
        "name": "File Dialogs",
        "description": "Native file open/save dialogs",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryDialog",
        "implemented": False,
    },
    "tray": {
        "name": "System Tray",
        "description": "System tray icon support",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryTray",
        "implemented": False,
    },
    "locale": {
        "name": "Locale Info",
        "description": "System locale and language information",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryLocale",
        "implemented": False,
    },
    "system": {
        "name": "Platform-specific Functionality",
        "description": "Platform-specific functions and utilities",
        "wiki": "https://wiki.libsdl.org/SDL3/CategorySystem",
        "implemented": False,
    },
    "stdinc": {
        "name": "Standard Library Functionality",
        "description": "Standard C library replacement functions",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryStdinc",
        "implemented": False,
    },
    "guid": {
        "name": "GUIDs",
        "description": "GUID generation and manipulation",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryGUID",
        "implemented": False,
    },
    "misc": {
        "name": "Miscellaneous",
        "description": "Miscellaneous utility functions",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryMisc",
        "implemented": False,
    },
}


def get_category_list() -> str:
    """Generate a formatted list of all SDL3 categories."""
    lines = ["# SDL3 API Categories\n"]
    lines.append("This server provides documentation for the SDL3 API organized by category.\n")

    # Group categories
    groups = {
        "Basics": ["main", "init", "hints", "properties", "error", "log", "assert", "version"],
        "Video": ["video", "render", "pixels", "blendmode", "rect", "surface", "clipboard", "vulkan", "metal", "camera"],
        "Input Events": ["events", "keyboard", "keycode", "scancode", "mouse", "joystick", "gamepad", "touch", "pen", "sensor", "hidapi"],
        "Force Feedback": ["haptic"],
        "Audio": ["audio"],
        "GPU": ["gpu"],
        "Threads": ["thread", "mutex", "atomic"],
        "Time": ["timer", "time"],
        "File and I/O": ["filesystem", "storage", "iostream", "asyncio"],
        "Platform and CPU": ["platform", "cpuinfo", "intrin", "endian", "bits"],
        "Additional": ["loadso", "process", "power", "messagebox", "dialog", "tray", "locale", "system", "stdinc", "guid", "misc"],
    }

    for group_name, category_keys in groups.items():
        lines.append(f"\n## {group_name}\n")
        for key in category_keys:
            if key in SDL3_CATEGORY_CATALOG:
                cat = SDL3_CATEGORY_CATALOG[key]
                status = "✓ Implemented" if cat["implemented"] else "Not yet implemented"
                lines.append(f"- **{cat['name']}** (`{key}`) - {cat['description']} [{status}]")

    lines.append("\n\n*Note: Categories marked as 'Not yet implemented' are part of SDL3 but not yet available in this server.*")
    lines.append("\n*For implemented categories, use `sdl_category_overview` tool with the category name in parentheses.*")

    return "\n".join(lines)


def format_category_suggestions(search_term: str = "") -> str:
    """Format category suggestions when a function is not found."""
    lines = []

    if search_term:
        lines.append(f"Function '{search_term}' not found in the current database.\n")

    lines.append("**Available Categories:**")

    # Show implemented categories first
    implemented = [k for k, v in SDL3_CATEGORY_CATALOG.items() if v["implemented"]]
    if implemented:
        lines.append("\n*Implemented categories you can explore:*")
        for key in sorted(implemented):
            cat = SDL3_CATEGORY_CATALOG[key]
            lines.append(f"- `{key}` - {cat['name']}: {cat['description']}")

    lines.append("\n*Use the `sdl_category_overview` tool with a category name to explore available functions.*")
    lines.append("*Use `sdl_search_functions` with keywords to search across all implemented categories.*")

    return "\n".join(lines)
