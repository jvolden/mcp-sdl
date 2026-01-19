"""SDL_touch.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_touch.h"

MIGRATION_DATA = """
# SDL_touch.h Migration Guide

## Device Enumeration Changes

SDL_GetTouchName is replaced with SDL_GetTouchDeviceName(), which takes an
SDL_TouchID instead of an index.

SDL_TouchID and SDL_FingerID are now Uint64 with 0 being an invalid value.

Rather than iterating over touch devices using an index, there is a new function
SDL_GetTouchDevices() to get the available devices.

Rather than iterating over touch fingers using an index, there is a new function
SDL_GetTouchFingers() to get the current set of active fingers.

## Removed Functions

The following functions have been removed:

• SDL_GetNumTouchDevices() - replaced with SDL_GetTouchDevices()
• SDL_GetNumTouchFingers() - replaced with SDL_GetTouchFingers()
• SDL_GetTouchDevice() - replaced with SDL_GetTouchDevices()
• SDL_GetTouchFinger() - replaced with SDL_GetTouchFingers()
"""
