"""SDL_mouse.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_mouse.h"

MIGRATION_DATA = """
# SDL_mouse.h Migration Guide

## ShowCursor Split

SDL_ShowCursor() has been split into three functions: SDL_ShowCursor(),
SDL_HideCursor(), and SDL_CursorVisible()

## Floating Point Coordinates

SDL_GetMouseState(), SDL_GetGlobalMouseState(), SDL_GetRelativeMouseState(),
SDL_WarpMouseInWindow(), and SDL_WarpMouseGlobal() all use floating point mouse
positions, to provide sub-pixel precision on platforms that support it.

## System Cursor Names

SDL_SystemCursor's items from SDL2 have been renamed to match CSS cursor names.

## Function Renames

The following functions have been renamed:

• SDL_FreeCursor() => SDL_DestroyCursor()

## Removed Functions

The following functions have been removed:

• SDL_SetRelativeMouseMode() - replaced with SDL_SetWindowRelativeMouseMode()
• SDL_GetRelativeMouseMode() - replaced with SDL_GetWindowRelativeMouseMode()

## Symbol Renames

The following symbols have been renamed:

• SDL_BUTTON => SDL_BUTTON_MASK
• SDL_NUM_SYSTEM_CURSORS => SDL_SYSTEM_CURSOR_COUNT
• SDL_SYSTEM_CURSOR_ARROW => SDL_SYSTEM_CURSOR_DEFAULT
• SDL_SYSTEM_CURSOR_HAND => SDL_SYSTEM_CURSOR_POINTER
• SDL_SYSTEM_CURSOR_IBEAM => SDL_SYSTEM_CURSOR_TEXT
• SDL_SYSTEM_CURSOR_NO => SDL_SYSTEM_CURSOR_NOT_ALLOWED
• SDL_SYSTEM_CURSOR_SIZEALL => SDL_SYSTEM_CURSOR_MOVE
• SDL_SYSTEM_CURSOR_SIZENESW => SDL_SYSTEM_CURSOR_NESW_RESIZE
• SDL_SYSTEM_CURSOR_SIZENS => SDL_SYSTEM_CURSOR_NS_RESIZE
• SDL_SYSTEM_CURSOR_SIZENWSE => SDL_SYSTEM_CURSOR_NWSE_RESIZE
• SDL_SYSTEM_CURSOR_SIZEWE => SDL_SYSTEM_CURSOR_EW_RESIZE
• SDL_SYSTEM_CURSOR_WAITARROW => SDL_SYSTEM_CURSOR_PROGRESS
"""
