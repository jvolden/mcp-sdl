"""SDL_version.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_version.h"

MIGRATION_DATA = """
# SDL_version.h Migration Guide

## Revision Number Removed

SDL_GetRevisionNumber() has been removed from the API, it always returned 0 in
SDL 2.0.

## Version Comparison

SDL_GetVersion() returns the version number, which can be directly compared with
another version wrapped with SDL_VERSIONNUM().

## Removed Structures

The following structures have been removed:

• SDL_version

## Symbol Renames

The following symbols have been renamed:

• SDL_COMPILEDVERSION => SDL_VERSION
• SDL_PATCHLEVEL => SDL_MICRO_VERSION
"""
