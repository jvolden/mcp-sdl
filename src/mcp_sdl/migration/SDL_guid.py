"""SDL_guid.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_guid.h"

MIGRATION_DATA = """
# SDL_guid.h Migration Guide

## Return Type Changes

SDL_GUIDToString() returns a const pointer to the string representation of a
GUID.

## Function Renames

The following functions have been renamed:

• SDL_GUIDFromString() => SDL_StringToGUID()
"""
