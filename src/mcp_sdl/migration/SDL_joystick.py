"""SDL_joystick.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_joystick.h"

MIGRATION_DATA = """
# SDL_joystick.h Migration Guide

## ID Type Changes

SDL_JoystickID has changed from Sint32 to Uint32, with an invalid ID being 0.

## Device Enumeration

Rather than iterating over joysticks using device index, there is a new function
SDL_GetJoysticks() to get the current list of joysticks, and new functions to
get information about joysticks from their instance ID.

The SDL_EVENT_JOYSTICK_ADDED event now provides the joystick instance ID in the `which` member of the jdevice event structure.

The functions SDL_GetJoysticks(), SDL_GetJoystickNameForID(),
SDL_GetJoystickPathForID(), SDL_GetJoystickPlayerIndexForID(), SDL_GetJoystickGUIDForID(),
SDL_GetJoystickVendorForID(), SDL_GetJoystickProductForID(),
SDL_GetJoystickProductVersionForID(), and SDL_GetJoystickTypeForID() have been added to directly query the
list of available joysticks.

## Virtual Joystick Changes

SDL_AttachVirtualJoystick() now returns the joystick instance ID instead of a
device index, and returns 0 if there was an error.

SDL_VirtualJoystickDesc version should not be set to
SDL_VIRTUAL_JOYSTICK_DESC_VERSION, instead the structure should be initialized using SDL_INIT_INTERFACE().

## Function Renames

The following functions have been renamed:

• SDL_JoystickAttachVirtualEx() => SDL_AttachVirtualJoystick()
• SDL_JoystickClose() => SDL_CloseJoystick()
• SDL_JoystickDetachVirtual() => SDL_DetachVirtualJoystick(), returns bool
• SDL_JoystickFromInstanceID() => SDL_GetJoystickFromID()
• SDL_JoystickFromPlayerIndex() => SDL_GetJoystickFromPlayerIndex()
• SDL_JoystickGetAttached() => SDL_JoystickConnected()
• SDL_JoystickGetAxis() => SDL_GetJoystickAxis()
• SDL_JoystickGetAxisInitialState() => SDL_GetJoystickAxisInitialState()
• SDL_JoystickGetBall() => SDL_GetJoystickBall(), returns bool
• SDL_JoystickGetButton() => SDL_GetJoystickButton()
• SDL_JoystickGetFirmwareVersion() => SDL_GetJoystickFirmwareVersion()
• SDL_JoystickGetGUID() => SDL_GetJoystickGUID()
• SDL_JoystickGetGUIDFromString() => SDL_StringToGUID()
• SDL_JoystickGetHat() => SDL_GetJoystickHat()
• SDL_JoystickGetPlayerIndex() => SDL_GetJoystickPlayerIndex()
• SDL_JoystickGetProduct() => SDL_GetJoystickProduct()
• SDL_JoystickGetProductVersion() => SDL_GetJoystickProductVersion()
• SDL_JoystickGetSerial() => SDL_GetJoystickSerial()
• SDL_JoystickGetType() => SDL_GetJoystickType()
• SDL_JoystickGetVendor() => SDL_GetJoystickVendor()
• SDL_JoystickInstanceID() => SDL_GetJoystickID()
• SDL_JoystickIsVirtual() => SDL_IsJoystickVirtual()
• SDL_JoystickName() => SDL_GetJoystickName()
• SDL_JoystickNumAxes() => SDL_GetNumJoystickAxes()
• SDL_JoystickNumBalls() => SDL_GetNumJoystickBalls()
• SDL_JoystickNumButtons() => SDL_GetNumJoystickButtons()
• SDL_JoystickNumHats() => SDL_GetNumJoystickHats()
• SDL_JoystickOpen() => SDL_OpenJoystick()
• SDL_JoystickPath() => SDL_GetJoystickPath()
• SDL_JoystickRumble() => SDL_RumbleJoystick(), returns bool
• SDL_JoystickRumbleTriggers() => SDL_RumbleJoystickTriggers(), returns bool
• SDL_JoystickSendEffect() => SDL_SendJoystickEffect(), returns bool
• SDL_JoystickSetLED() => SDL_SetJoystickLED(), returns bool
• SDL_JoystickSetPlayerIndex() => SDL_SetJoystickPlayerIndex(), returns bool
• SDL_JoystickSetVirtualAxis() => SDL_SetJoystickVirtualAxis(), returns bool
• SDL_JoystickSetVirtualButton() => SDL_SetJoystickVirtualButton(), returns bool
• SDL_JoystickSetVirtualHat() => SDL_SetJoystickVirtualHat(), returns bool
• SDL_JoystickUpdate() => SDL_UpdateJoysticks()

## Symbol Renames

The following symbols have been renamed:

• SDL_JOYSTICK_TYPE_GAMECONTROLLER => SDL_JOYSTICK_TYPE_GAMEPAD

## Removed Functions

The following functions have been removed:

• SDL_JoystickAttachVirtual() - replaced with SDL_AttachVirtualJoystick()
• SDL_JoystickCurrentPowerLevel() - replaced with SDL_GetJoystickConnectionState()
and SDL_GetJoystickPowerInfo()
• SDL_JoystickEventState() - replaced with SDL_SetJoystickEventsEnabled() and
SDL_JoystickEventsEnabled()
• SDL_JoystickGetDeviceGUID() - replaced with SDL_GetJoystickGUIDForID()
• SDL_JoystickGetDeviceInstanceID()
• SDL_JoystickGetDevicePlayerIndex() - replaced with
SDL_GetJoystickPlayerIndexForID()
• SDL_JoystickGetDeviceProduct() - replaced with SDL_GetJoystickProductForID()
• SDL_JoystickGetDeviceProductVersion() - replaced with
SDL_GetJoystickProductVersionForID()
• SDL_JoystickGetDeviceType() - replaced with SDL_GetJoystickTypeForID()
• SDL_JoystickGetDeviceVendor() - replaced with SDL_GetJoystickVendorForID()
• SDL_JoystickGetGUIDString() - replaced with SDL_GUIDToString()
• SDL_JoystickHasLED() - replaced with SDL_PROP_JOYSTICK_CAP_RGB_LED_BOOLEAN
• SDL_JoystickHasRumble() - replaced with SDL_PROP_JOYSTICK_CAP_RUMBLE_BOOLEAN
• SDL_JoystickHasRumbleTriggers() - replaced with
SDL_PROP_JOYSTICK_CAP_TRIGGER_RUMBLE_BOOLEAN
• SDL_JoystickNameForIndex() - replaced with SDL_GetJoystickNameForID()
• SDL_JoystickPathForIndex() - replaced with SDL_GetJoystickPathForID()
• SDL_NumJoysticks() - replaced with SDL_GetJoysticks()
• SDL_VIRTUAL_JOYSTICK_DESC_VERSION - no longer needed

## Removed Symbols

The following symbols have been removed:

• SDL_IPHONE_MAX_GFORCE
• SDL_JOYBALLMOTION

## Structure Renames

The following structures have been renamed:

• SDL_JoystickGUID => SDL_GUID
"""
