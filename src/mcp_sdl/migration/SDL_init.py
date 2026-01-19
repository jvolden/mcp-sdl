"""SDL_init.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_init.h"

MIGRATION_DATA = """
# SDL_init.h Migration Guide

## Haiku OS Changes

On Haiku OS, SDL no longer sets the current working directory to the
executable's path during SDL_Init(). If you need this functionality, add this code
directly after the call to SDL_Init:

```c
{
    const char *path = SDL_GetBasePath();
    if (path) {
        chdir(path);
    }
}
```

## Symbol Renames

The following symbols have been renamed:

• SDL_INIT_GAMECONTROLLER => SDL_INIT_GAMEPAD

## Removed Symbols

The following symbols have been removed:

• SDL_INIT_NOPARACHUTE
• SDL_INIT_EVERYTHING - you should only initialize the subsystems you are using
• SDL_INIT_TIMER - no longer needed before calling SDL_AddTimer()
"""
