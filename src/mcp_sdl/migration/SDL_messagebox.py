"""SDL_messagebox.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_messagebox.h"

MIGRATION_DATA = """
# SDL_messagebox.h Migration Guide

## Field Name Changes

The buttonid field of SDL_MessageBoxButtonData has been renamed buttonID.

## Symbol Renames

The following symbols have been renamed:

• SDL_MESSAGEBOX_COLOR_MAX => SDL_MESSAGEBOX_COLOR_COUNT
"""
