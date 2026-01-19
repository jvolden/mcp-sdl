"""SDL_gamecontroller.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_gamecontroller.h"

MIGRATION_DATA = """
# SDL_gamecontroller.h Migration Guide

SDL_gamecontroller.h has been renamed SDL_gamepad.h, and all APIs have been
renamed to match.

## Device Enumeration Changes

The SDL_EVENT_GAMEPAD_ADDED event now provides the joystick instance ID in the
which member of the cdevice event structure.

The functions SDL_GetGamepads(), SDL_GetGamepadNameForID(),
SDL_GetGamepadPathForID(), SDL_GetGamepadPlayerIndexForID(), SDL_GetGamepadGUIDForID(),
SDL_GetGamepadVendorForID(), SDL_GetGamepadProductForID(),
SDL_GetGamepadProductVersionForID(), and SDL_GetGamepadTypeForID() have been added to directly query the list of
available gamepads.

## Face Button Changes

The gamepad face buttons have been renamed from A/B/X/Y to North/South/East/West
to indicate that they are positional rather than hardware-specific. You can use
SDL_GetGamepadButtonLabel() to get the labels for the face buttons, e.g.
A/B/X/Y or Cross/Circle/Square/Triangle. The hint
SDL_HINT_GAMECONTROLLER_USE_BUTTON_LABELS is ignored, and mappings that use this hint are translated correctly into
positional buttons.

## Virtual Gamepad Changes

SDL_CONTROLLER_TYPE_VIRTUAL has been removed, so virtual controllers can emulate
other gamepad types. If you need to know whether a controller is virtual, you
can use SDL_IsJoystickVirtual().

## Timestamp Changes

SDL_GameControllerGetSensorDataWithTimestamp() has been removed. If you want
timestamps for the sensor data, you should use the sensor_timestamp member of
SDL_EVENT_GAMEPAD_SENSOR_UPDATE events.

## Binding Type Changes

The inputType and outputType fields of SDL_GamepadBinding have been renamed
input_type and output_type.

SDL_GetGamepadTouchpadFinger() takes a pointer to bool for the finger state
instead of a pointer to Uint8.

## Enum Renames

The following enums have been renamed:

• SDL_GameControllerAxis => SDL_GamepadAxis
• SDL_GameControllerBindType => SDL_GamepadBindingType
• SDL_GameControllerButton => SDL_GamepadButton
• SDL_GameControllerType => SDL_GamepadType

## Structure Renames

The following structures have been renamed:

• SDL_GameController => SDL_Gamepad

## Removed Structures

The following structures have been removed:

• SDL_GameControllerButtonBind - replaced with SDL_GamepadBinding

## Function Renames

The following functions have been renamed:

• SDL_GameControllerAddMapping() => SDL_AddGamepadMapping()
• SDL_GameControllerAddMappingsFromFile() => SDL_AddGamepadMappingsFromFile()
• SDL_GameControllerAddMappingsFromRW() => SDL_AddGamepadMappingsFromIO()
• SDL_GameControllerClose() => SDL_CloseGamepad()
• SDL_GameControllerFromInstanceID() => SDL_GetGamepadFromID()
• SDL_GameControllerFromPlayerIndex() => SDL_GetGamepadFromPlayerIndex()
• SDL_GameControllerGetAppleSFSymbolsNameForAxis() =>
SDL_GetGamepadAppleSFSymbolsNameForAxis()
• SDL_GameControllerGetAppleSFSymbolsNameForButton() =>
SDL_GetGamepadAppleSFSymbolsNameForButton()
• SDL_GameControllerGetAttached() => SDL_GamepadConnected()
• SDL_GameControllerGetAxis() => SDL_GetGamepadAxis()
• SDL_GameControllerGetAxisFromString() => SDL_GetGamepadAxisFromString()
• SDL_GameControllerGetButton() => SDL_GetGamepadButton()
• SDL_GameControllerGetButtonFromString() => SDL_GetGamepadButtonFromString()
• SDL_GameControllerGetFirmwareVersion() => SDL_GetGamepadFirmwareVersion()
• SDL_GameControllerGetJoystick() => SDL_GetGamepadJoystick()
• SDL_GameControllerGetNumTouchpadFingers() => SDL_GetNumGamepadTouchpadFingers()
• SDL_GameControllerGetNumTouchpads() => SDL_GetNumGamepadTouchpads()
• SDL_GameControllerGetPlayerIndex() => SDL_GetGamepadPlayerIndex()
• SDL_GameControllerGetProduct() => SDL_GetGamepadProduct()
• SDL_GameControllerGetProductVersion() => SDL_GetGamepadProductVersion()
• SDL_GameControllerGetSensorData() => SDL_GetGamepadSensorData(), returns bool
• SDL_GameControllerGetSensorDataRate() => SDL_GetGamepadSensorDataRate()
• SDL_GameControllerGetSerial() => SDL_GetGamepadSerial()
• SDL_GameControllerGetSteamHandle() => SDL_GetGamepadSteamHandle()
• SDL_GameControllerGetStringForAxis() => SDL_GetGamepadStringForAxis()
• SDL_GameControllerGetStringForButton() => SDL_GetGamepadStringForButton()
• SDL_GameControllerGetTouchpadFinger() => SDL_GetGamepadTouchpadFinger(), returns
bool
• SDL_GameControllerGetType() => SDL_GetGamepadType()
• SDL_GameControllerGetVendor() => SDL_GetGamepadVendor()
• SDL_GameControllerHasAxis() => SDL_GamepadHasAxis()
• SDL_GameControllerHasButton() => SDL_GamepadHasButton()
• SDL_GameControllerHasSensor() => SDL_GamepadHasSensor()
• SDL_GameControllerIsSensorEnabled() => SDL_GamepadSensorEnabled()
• SDL_GameControllerMapping() => SDL_GetGamepadMapping()
• SDL_GameControllerMappingForGUID() => SDL_GetGamepadMappingForGUID()
• SDL_GameControllerName() => SDL_GetGamepadName()
• SDL_GameControllerOpen() => SDL_OpenGamepad()
• SDL_GameControllerPath() => SDL_GetGamepadPath()
• SDL_GameControllerRumble() => SDL_RumbleGamepad(), returns bool
• SDL_GameControllerRumbleTriggers() => SDL_RumbleGamepadTriggers(), returns bool
• SDL_GameControllerSendEffect() => SDL_SendGamepadEffect(), returns bool
• SDL_GameControllerSetLED() => SDL_SetGamepadLED(), returns bool
• SDL_GameControllerSetPlayerIndex() => SDL_SetGamepadPlayerIndex(), returns bool
• SDL_GameControllerSetSensorEnabled() => SDL_SetGamepadSensorEnabled(), returns
bool
• SDL_GameControllerUpdate() => SDL_UpdateGamepads()
• SDL_IsGameController() => SDL_IsGamepad()

## Removed Functions

The following functions have been removed:

• SDL_GameControllerEventState() - replaced with SDL_SetGamepadEventsEnabled() and
SDL_GamepadEventsEnabled()
• SDL_GameControllerGetBindForAxis() - replaced with SDL_GetGamepadBindings()
• SDL_GameControllerGetBindForButton() - replaced with SDL_GetGamepadBindings()
• SDL_GameControllerHasLED() - replaced with SDL_PROP_GAMEPAD_CAP_RGB_LED_BOOLEAN
• SDL_GameControllerHasRumble() - replaced with
SDL_PROP_GAMEPAD_CAP_RUMBLE_BOOLEAN
• SDL_GameControllerHasRumbleTriggers() - replaced with
SDL_PROP_GAMEPAD_CAP_TRIGGER_RUMBLE_BOOLEAN
• SDL_GameControllerMappingForDeviceIndex() - replaced with
SDL_GetGamepadMappingForID()
• SDL_GameControllerMappingForIndex() - replaced with SDL_GetGamepadMappings()
• SDL_GameControllerNameForIndex() - replaced with SDL_GetGamepadNameForID()
• SDL_GameControllerNumMappings() - replaced with SDL_GetGamepadMappings()
• SDL_GameControllerPathForIndex() - replaced with SDL_GetGamepadPathForID()
• SDL_GameControllerTypeForIndex() - replaced with SDL_GetGamepadTypeForID()

## Symbol Renames

The following symbols have been renamed:

• SDL_CONTROLLER_AXIS_INVALID => SDL_GAMEPAD_AXIS_INVALID
• SDL_CONTROLLER_AXIS_LEFTX => SDL_GAMEPAD_AXIS_LEFTX
• SDL_CONTROLLER_AXIS_LEFTY => SDL_GAMEPAD_AXIS_LEFTY
• SDL_CONTROLLER_AXIS_MAX => SDL_GAMEPAD_AXIS_COUNT
• SDL_CONTROLLER_AXIS_RIGHTX => SDL_GAMEPAD_AXIS_RIGHTX
• SDL_CONTROLLER_AXIS_RIGHTY => SDL_GAMEPAD_AXIS_RIGHTY
• SDL_CONTROLLER_AXIS_TRIGGERLEFT => SDL_GAMEPAD_AXIS_LEFT_TRIGGER
• SDL_CONTROLLER_AXIS_TRIGGERRIGHT => SDL_GAMEPAD_AXIS_RIGHT_TRIGGER
• SDL_CONTROLLER_BINDTYPE_AXIS => SDL_GAMEPAD_BINDTYPE_AXIS
• SDL_CONTROLLER_BINDTYPE_BUTTON => SDL_GAMEPAD_BINDTYPE_BUTTON
• SDL_CONTROLLER_BINDTYPE_HAT => SDL_GAMEPAD_BINDTYPE_HAT
• SDL_CONTROLLER_BINDTYPE_NONE => SDL_GAMEPAD_BINDTYPE_NONE
• SDL_CONTROLLER_BUTTON_A => SDL_GAMEPAD_BUTTON_SOUTH
• SDL_CONTROLLER_BUTTON_B => SDL_GAMEPAD_BUTTON_EAST
• SDL_CONTROLLER_BUTTON_BACK => SDL_GAMEPAD_BUTTON_BACK
• SDL_CONTROLLER_BUTTON_DPAD_DOWN => SDL_GAMEPAD_BUTTON_DPAD_DOWN
• SDL_CONTROLLER_BUTTON_DPAD_LEFT => SDL_GAMEPAD_BUTTON_DPAD_LEFT
• SDL_CONTROLLER_BUTTON_DPAD_RIGHT => SDL_GAMEPAD_BUTTON_DPAD_RIGHT
• SDL_CONTROLLER_BUTTON_DPAD_UP => SDL_GAMEPAD_BUTTON_DPAD_UP
• SDL_CONTROLLER_BUTTON_GUIDE => SDL_GAMEPAD_BUTTON_GUIDE
• SDL_CONTROLLER_BUTTON_INVALID => SDL_GAMEPAD_BUTTON_INVALID
• SDL_CONTROLLER_BUTTON_LEFTSHOULDER => SDL_GAMEPAD_BUTTON_LEFT_SHOULDER
• SDL_CONTROLLER_BUTTON_LEFTSTICK => SDL_GAMEPAD_BUTTON_LEFT_STICK
• SDL_CONTROLLER_BUTTON_MAX => SDL_GAMEPAD_BUTTON_COUNT
• SDL_CONTROLLER_BUTTON_MISC1 => SDL_GAMEPAD_BUTTON_MISC1
• SDL_CONTROLLER_BUTTON_PADDLE1 => SDL_GAMEPAD_BUTTON_RIGHT_PADDLE1
• SDL_CONTROLLER_BUTTON_PADDLE2 => SDL_GAMEPAD_BUTTON_LEFT_PADDLE1
• SDL_CONTROLLER_BUTTON_PADDLE3 => SDL_GAMEPAD_BUTTON_RIGHT_PADDLE2
• SDL_CONTROLLER_BUTTON_PADDLE4 => SDL_GAMEPAD_BUTTON_LEFT_PADDLE2
• SDL_CONTROLLER_BUTTON_RIGHTSHOULDER => SDL_GAMEPAD_BUTTON_RIGHT_SHOULDER
• SDL_CONTROLLER_BUTTON_RIGHTSTICK => SDL_GAMEPAD_BUTTON_RIGHT_STICK
• SDL_CONTROLLER_BUTTON_START => SDL_GAMEPAD_BUTTON_START
• SDL_CONTROLLER_BUTTON_TOUCHPAD => SDL_GAMEPAD_BUTTON_TOUCHPAD
• SDL_CONTROLLER_BUTTON_X => SDL_GAMEPAD_BUTTON_WEST
• SDL_CONTROLLER_BUTTON_Y => SDL_GAMEPAD_BUTTON_NORTH
• SDL_CONTROLLER_TYPE_NINTENDO_SWITCH_JOYCON_LEFT =>
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_LEFT
• SDL_CONTROLLER_TYPE_NINTENDO_SWITCH_JOYCON_PAIR =>
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_PAIR
• SDL_CONTROLLER_TYPE_NINTENDO_SWITCH_JOYCON_RIGHT =>
SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_JOYCON_RIGHT
• SDL_CONTROLLER_TYPE_NINTENDO_SWITCH_PRO => SDL_GAMEPAD_TYPE_NINTENDO_SWITCH_PRO
• SDL_CONTROLLER_TYPE_PS3 => SDL_GAMEPAD_TYPE_PS3
• SDL_CONTROLLER_TYPE_PS4 => SDL_GAMEPAD_TYPE_PS4
• SDL_CONTROLLER_TYPE_PS5 => SDL_GAMEPAD_TYPE_PS5
• SDL_CONTROLLER_TYPE_UNKNOWN => SDL_GAMEPAD_TYPE_STANDARD
• SDL_CONTROLLER_TYPE_VIRTUAL => SDL_GAMEPAD_TYPE_VIRTUAL
• SDL_CONTROLLER_TYPE_XBOX360 => SDL_GAMEPAD_TYPE_XBOX360
• SDL_CONTROLLER_TYPE_XBOXONE => SDL_GAMEPAD_TYPE_XBOXONE
"""
