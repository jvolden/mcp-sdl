"""SDL_gesture.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_gesture.h"

MIGRATION_DATA = """
# SDL_gesture.h Migration Guide

The gesture API has been removed. There is no replacement planned in SDL3.
However, the SDL2 code has been moved to a single-header library that can be dropped
into an SDL3 or SDL2 program, to continue to provide this functionality to your
app and aid migration. That is located in the [SDL_gesture GitHub repository](https://github.com/libsdl-org/SDL_gesture).
"""
