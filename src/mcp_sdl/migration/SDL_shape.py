"""SDL_shape.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_shape.h"

MIGRATION_DATA = """
# SDL_shape.h Migration Guide

This header has been removed and a simplified version of this API has been added
as SDL_SetWindowShape() in SDL_video.h. See test/testshape.c for an example.
"""
