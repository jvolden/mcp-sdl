"""SDL_haptic.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_haptic.h"

MIGRATION_DATA = """
# SDL_haptic.h Migration Guide

## Gamepad Rumble Changes

Gamepads with simple rumble capability no longer show up in the SDL haptics
interface, instead you should use SDL_RumbleGamepad().

## Device Enumeration

Rather than iterating over haptic devices using device index, there is a new
function SDL_GetHaptics() to get the current list of haptic devices, and new
functions to get information about haptic devices from their instance ID.

## Return Type Changes

SDL_GetHapticEffectStatus() now returns bool instead of an int result. You
should call SDL_GetHapticFeatures() to make sure effect status is supported before
calling this function.

## Function Renames

The following functions have been renamed:

• SDL_HapticClose() => SDL_CloseHaptic()
• SDL_HapticDestroyEffect() => SDL_DestroyHapticEffect()
• SDL_HapticGetEffectStatus() => SDL_GetHapticEffectStatus(), returns bool
• SDL_HapticNewEffect() => SDL_CreateHapticEffect()
• SDL_HapticNumAxes() => SDL_GetNumHapticAxes()
• SDL_HapticNumEffects() => SDL_GetMaxHapticEffects()
• SDL_HapticNumEffectsPlaying() => SDL_GetMaxHapticEffectsPlaying()
• SDL_HapticOpen() => SDL_OpenHaptic()
• SDL_HapticOpenFromJoystick() => SDL_OpenHapticFromJoystick()
• SDL_HapticOpenFromMouse() => SDL_OpenHapticFromMouse()
• SDL_HapticPause() => SDL_PauseHaptic(), returns bool
• SDL_HapticQuery() => SDL_GetHapticFeatures()
• SDL_HapticRumbleInit() => SDL_InitHapticRumble(), returns bool
• SDL_HapticRumblePlay() => SDL_PlayHapticRumble(), returns bool
• SDL_HapticRumbleStop() => SDL_StopHapticRumble(), returns bool
• SDL_HapticRunEffect() => SDL_RunHapticEffect(), returns bool
• SDL_HapticSetAutocenter() => SDL_SetHapticAutocenter(), returns bool
• SDL_HapticSetGain() => SDL_SetHapticGain(), returns bool
• SDL_HapticStopAll() => SDL_StopHapticEffects(), returns bool
• SDL_HapticStopEffect() => SDL_StopHapticEffect(), returns bool
• SDL_HapticUnpause() => SDL_ResumeHaptic(), returns bool
• SDL_HapticUpdateEffect() => SDL_UpdateHapticEffect(), returns bool
• SDL_JoystickIsHaptic() => SDL_IsJoystickHaptic()
• SDL_MouseIsHaptic() => SDL_IsMouseHaptic()

## Removed Functions

The following functions have been removed:

• SDL_HapticIndex() - replaced with SDL_GetHapticID()
• SDL_HapticName() - replaced with SDL_GetHapticNameForID()
• SDL_HapticOpened() - replaced with SDL_GetHapticFromID()
• SDL_NumHaptics() - replaced with SDL_GetHaptics()
"""
