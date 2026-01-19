"""SDL_quit.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_quit.h"

MIGRATION_DATA = """
# SDL_quit.h Migration Guide

SDL_quit.h has been completely removed. It only had one symbol in
it--SDL_QuitRequested--and if you want it, you can just add this to your app:

```c
#define SDL_QuitRequested() (SDL_PumpEvents(), (SDL_PeepEvents(NULL,0,SDL_PEEKEVENT,SDL_EVENT_QUIT,SDL_EVENT_QUIT) > 0))
```

...but this macro is sort of messy, calling two functions in sequence in an
expression.

## Removed Macros

The following macros have been removed:

• SDL_QuitRequested - call SDL_PumpEvents() then SDL_PeepEvents() directly,
instead.
"""
