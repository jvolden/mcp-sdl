"""SDL_timer.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_timer.h"

MIGRATION_DATA = """
# SDL_timer.h Migration Guide

## Tick Value Changes

SDL_GetTicks() now returns a 64-bit value. Instead of using the SDL_TICKS_PASSED
macro, you can directly compare tick values, e.g.

SDL2 code:

```c
Uint32 deadline = SDL_GetTicks() + 1000;
...
if (SDL_TICKS_PASSED(SDL_GetTicks(), deadline)) {
    ...
}
```

becomes:

```c
Uint64 deadline = SDL_GetTicks() + 1000
...
if (SDL_GetTicks() >= deadline) {
    ...
}
```

If you were using this macro for other things besides SDL ticks values, you can
define it in your own code as:

```c
#define SDL_TICKS_PASSED(A, B)  ((Sint32)((B) - (A)) <= 0)
```

...but this macro is sort of messy, calling two functions in sequence in an
expression.

## Timer Callback Changes

The callback passed to SDL_AddTimer() has changed parameters to:

```c
Uint32 SDLCALL TimerCallback(void *userdata, SDL_TimerID timerID, Uint32 interval);
```
"""
