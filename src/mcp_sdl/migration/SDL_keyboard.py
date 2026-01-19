"""SDL_keyboard.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_keyboard.h"

MIGRATION_DATA = """
# SDL_keyboard.h Migration Guide

## Text Input Changes

Text input is no longer automatically enabled when initializing video, you
should call SDL_StartTextInput() when you want to receive text input and call
SDL_StopTextInput() when you are done. Starting text input may shown an input method
editor (IME) and cause key up/down events to be skipped, so should only be enabled
when the application wants text input.

The text input state hase been changed to be window-specific.
SDL_StartTextInput(), SDL_StopTextInput(), SDL_TextInputActive(), and SDL_ClearComposition() all
now take a window parameter.

## Keycode and Scancode Functions

SDL_GetDefaultKeyFromScancode(), SDL_GetKeyFromScancode(), and
SDL_GetScancodeFromKey() take an SDL_Keymod parameter and use that to provide the correct result
based on keyboard modifier state.

## Keyboard State

SDL_GetKeyboardState() returns a pointer to bool instead of Uint8.

## Function Renames

The following functions have been renamed:

• SDL_IsScreenKeyboardShown() => SDL_ScreenKeyboardShown()
• SDL_IsTextInputActive() => SDL_TextInputActive()

## Removed Functions

The following functions have been removed:

• SDL_IsTextInputShown()
• SDL_SetTextInputRect() - replaced with SDL_SetTextInputArea()

## Removed Structures

The following structures have been removed:

• SDL_Keysym
"""
