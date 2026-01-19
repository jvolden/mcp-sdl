"""SDL_loadso.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_loadso.h"

MIGRATION_DATA = """
# SDL_loadso.h Migration Guide

## Shared Object Handle Type

Shared object handles are now `SDL_SharedObject *`, an opaque type, instead of `void *`. This is just for type-safety and there is no functional difference.

## Function Pointer Type

SDL_LoadFunction() now returns `SDL_FunctionPointer` instead of `void *`, and should be cast to the appropriate function type. You can define
SDL_FUNCTION_POINTER_IS_VOID_POINTER in your project to restore the previous behavior.
"""
