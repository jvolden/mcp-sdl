"""SDL2 to SDL3 migration guides organized by header file."""

import importlib
from pathlib import Path
from typing import TypedDict

# General overview of SDL2 to SDL3 migration
OVERVIEW = """# Migrating to SDL 3.0

This guide provides useful information for migrating applications from SDL 2.0 to SDL 3.0.

Details on API changes are organized by SDL 2.0 header below.

The file with your main() function should include <SDL3/SDL_main.h>, as that is no longer included in SDL.h.

## Return Value Changes

Functions that previously returned a negative error code now return bool.

Code that used to look like this:
```c
if (SDL_Function() < 0 || SDL_Function() == -1) {
    /* Failure... */
}
```

should be changed to:
```c
if (SDL_Function()) {
    /* Success... */
} else {
    /* Failure... */
}
```

This only applies to camel case functions, e.g. SDL_[A-Z]*. Lower case functions like SDL_strcmp() and SDL_memcpy() are unchanged.

## Migration Tools

Many functions and symbols have been renamed. SDL provides Python migration scripts:
- rename_symbols.py - Rename SDL2 functions to SDL3 counterparts
- rename_headers.py - Update include paths from SDL2 to SDL3
- rename_macros.py - Replace renamed/removed macros
- SDL_migration.cocci - Semantic patch for migration

## Include Path Changes

SDL headers should now be included as `#include <SDL3/SDL.h>`.

## Build System Changes

### CMake
```cmake
find_package(SDL3 REQUIRED CONFIG REQUIRED COMPONENTS SDL3)
target_link_libraries(mygame PRIVATE SDL3::SDL3)
```

### Autotools
```bash
PKG_CHECK_MODULES([SDL3], [sdl3])
```

### Makefile
```make
CFLAGS += $(shell pkg-config sdl3 --cflags)
LDFLAGS += $(shell pkg-config sdl3 --libs)
```

## Library Changes

- The SDL3test library has been renamed SDL3_test
- The SDLmain library has been removed (replaced by SDL_main.h)
- Installed CMake configuration files no longer define SDL3_PREFIX, SDL3_EXEC_PREFIX, etc.

For detailed information about specific headers, see the individual migration guides below.
"""


class MigrationSearchResult(TypedDict):
    """Result from migration search."""
    header: str
    matches: list[str]


# Discover all migration header modules
current_dir = Path(__file__).parent
header_files = [
    f.stem for f in current_dir.glob("SDL_*.py")
    if f.is_file() and not f.name.startswith('_')
]

HEADERS = {}

for header_name in sorted(header_files):
    try:
        module = importlib.import_module(f".{header_name}", package=__name__)
        if hasattr(module, "HEADER") and hasattr(module, "MIGRATION_DATA"):
            HEADERS[module.HEADER] = module.MIGRATION_DATA
    except ImportError:
        pass

def get_all_headers() -> list[str]:
    """Get list of all available migration headers."""
    return sorted(HEADERS.keys())

def get_migration_data(header: str) -> str | None:
    """Get migration data for a specific header."""
    return HEADERS.get(header)

def search_migrations(query: str) -> list[MigrationSearchResult]:
    """Search across all migration data for a query string."""
    results: list[MigrationSearchResult] = []
    query_lower = query.lower()

    for header, data in HEADERS.items():
        if query_lower in data.lower():
            # Find context around matches
            lines = data.split('\n')
            matching_lines = []
            for i, line in enumerate(lines):
                if query_lower in line.lower():
                    # Get some context
                    start = max(0, i - 2)
                    end = min(len(lines), i + 3)
                    context = '\n'.join(lines[start:end])
                    matching_lines.append(context)

            if matching_lines:
                results.append({
                    'header': header,
                    'matches': matching_lines
                })

    return results

__all__ = ["OVERVIEW", "HEADERS", "get_all_headers", "get_migration_data", "search_migrations"]
