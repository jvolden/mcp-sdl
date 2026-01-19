"""SDL_error.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_error.h"

MIGRATION_DATA = """
# SDL_error.h Migration Guide

## Removed Functions

The following functions have been removed:

• SDL_GetErrorMsg() - Can be implemented as `SDL_strlcpy(errstr, SDL_GetError(), maxlen);`
"""
