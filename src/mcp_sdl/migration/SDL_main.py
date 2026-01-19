"""SDL_main.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_main.h"

MIGRATION_DATA = """
# SDL_main.h Migration Guide

## Header-Only Library

SDL3 doesn't have a static libSDLmain to link against anymore. Instead
SDL_main.h is now a header-only library and not included by SDL.h anymore.

Using it is really simple: Just `#include <SDL3/SDL_main.h>` in the source file with your standard `int main(int argc, char* argv[])` function. See docs/README-main-functions.md for details.

## Entry Point Functions

Several platform-specific entry point functions have been removed as
unnecessary. If for some reason you explicitly need them, here are easy replacements:

```c
#define SDL_UIKitRunApp(ARGC, ARGV, MAIN_FUNC)  SDL_RunApp(ARGC, ARGV, MAIN_FUNC, NULL)
#define SDL_GDKRunApp(MAIN_FUNC, RESERVED)  SDL_RunApp(0, NULL, MAIN_FUNC, RESERVED)
```

## Removed Functions

The following functions have been removed:

• SDL_WinRTRunApp() - WinRT support was removed in SDL3.
"""
