"""SDL_metal.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_metal.h"

MIGRATION_DATA = """
# SDL_metal.h Migration Guide

## Removed Functions

SDL_Metal_GetDrawableSize() has been removed. SDL_GetWindowSizeInPixels() can be
used in its place.
"""
