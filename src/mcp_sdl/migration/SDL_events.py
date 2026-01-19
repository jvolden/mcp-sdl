"""SDL_events.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_events.h"

MIGRATION_DATA = """
# SDL_events.h Migration Guide

## State Constants Removed

SDL_PRESSED and SDL_RELEASED have been removed. For the most part you can
replace uses of these with true and false respectively. Events which had a field `state` to represent these values have had those fields changed to bool `down`, e.g. `event.key.state` is now `event.key.down`.

## Timestamp Changes

The timestamp member of the SDL_Event structure now represents nanoseconds, and
is populated with SDL_GetTicksNS()

The timestamp_us member of the sensor events has been renamed sensor_timestamp
and now represents nanoseconds. This value is filled in from the hardware, if
available, and may not be synchronized with values returned from SDL_GetTicksNS().

You should set the event.common.timestamp field before passing an event to
SDL_PushEvent(). If the timestamp is 0 it will be filled in with SDL_GetTicksNS().

## Event Memory Management

Event memory is now managed by SDL, so you should not free the data in
SDL_EVENT_DROP_FILE, and if you want to hold onto the text in SDL_EVENT_TEXT_EDITING and
SDL_EVENT_TEXT_INPUT events, you should make a copy of it.
SDL_TEXTINPUTEVENT_TEXT_SIZE is no longer necessary and has been removed.

## Mouse Event Coordinates

Mouse events use floating point values for mouse coordinates and relative motion
values. You can get sub-pixel motion depending on the platform and display
scaling.

## Display and Window Events

The SDL_DISPLAYEVENT_* events have been moved to top level events, and
SDL_DISPLAYEVENT has been removed. In general, handling this change just means checking
for the individual events instead of first checking for SDL_DISPLAYEVENT and then
checking for display events. You can compare the event >=
SDL_EVENT_DISPLAY_FIRST and <= SDL_EVENT_DISPLAY_LAST if you need to see whether it's a display
event.

The SDL_WINDOWEVENT_* events have been moved to top level events, and
SDL_WINDOWEVENT has been removed. In general, handling this change just means checking for
the individual events instead of first checking for SDL_WINDOWEVENT and then
checking for window events. You can compare the event >= SDL_EVENT_WINDOW_FIRST
and <= SDL_EVENT_WINDOW_LAST if you need to see whether it's a window event.

The SDL_EVENT_WINDOW_RESIZED event is always sent, even in response to
SDL_SetWindowSize().

The SDL_EVENT_WINDOW_SIZE_CHANGED event has been removed, and you can use
SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED to detect window backbuffer size changes.

## Keysym Changes

The keysym field of key events has been removed to remove one level of
indirection, and `sym` has been renamed `key`.

Code that used to look like this:

```c
SDL_Event event;
SDL_Keycode key = event.key.keysym.sym;
SDL_Keymod mod = event.key.keysym.mod;
```

should be changed to:

```c
SDL_Event event;
SDL_Keycode key = event.key.key;
SDL_Keymod mod = event.key.mod;
```

## Gamepad Events

The gamepad event structures caxis, cbutton, cdevice, ctouchpad, and csensor
have been renamed gaxis, gbutton, gdevice, gtouchpad, and gsensor.

## Other Event Field Changes

The mouseX and mouseY fields of SDL_MouseWheelEvent have been renamed mouse_x
and mouse_y.

The touchId and fingerId fields of SDL_TouchFingerEvent have been renamed
touchID and fingerID.

The level field of SDL_JoyBatteryEvent has been split into state and percent.

The iscapture field of SDL_AudioDeviceEvent has been renamed recording.

## Query/Enable/Disable Changes

SDL_QUERY, SDL_IGNORE, SDL_ENABLE, and SDL_DISABLE have been removed. You can
use the functions SDL_SetEventEnabled() and SDL_EventEnabled() to set and query
event processing state.

## Function Return Types

SDL_AddEventWatch() now returns false if it fails because it ran out of memory
and couldn't add the event watch callback.

SDL_RegisterEvents() now returns 0 if it couldn't allocate any user events.

SDL_EventFilter functions now return bool.

## Symbol Renames

The following symbols have been renamed:

• SDL_APP_DIDENTERBACKGROUND => SDL_EVENT_DID_ENTER_BACKGROUND
• SDL_APP_DIDENTERFOREGROUND => SDL_EVENT_DID_ENTER_FOREGROUND
• SDL_APP_LOWMEMORY => SDL_EVENT_LOW_MEMORY
• SDL_APP_TERMINATING => SDL_EVENT_TERMINATING
• SDL_APP_WILLENTERBACKGROUND => SDL_EVENT_WILL_ENTER_BACKGROUND
• SDL_APP_WILLENTERFOREGROUND => SDL_EVENT_WILL_ENTER_FOREGROUND
• SDL_AUDIODEVICEADDED => SDL_EVENT_AUDIO_DEVICE_ADDED
• SDL_AUDIODEVICEREMOVED => SDL_EVENT_AUDIO_DEVICE_REMOVED
• SDL_CLIPBOARDUPDATE => SDL_EVENT_CLIPBOARD_UPDATE
• SDL_CONTROLLERAXISMOTION => SDL_EVENT_GAMEPAD_AXIS_MOTION
• SDL_CONTROLLERBUTTONDOWN => SDL_EVENT_GAMEPAD_BUTTON_DOWN
• SDL_CONTROLLERBUTTONUP => SDL_EVENT_GAMEPAD_BUTTON_UP
• SDL_CONTROLLERDEVICEADDED => SDL_EVENT_GAMEPAD_ADDED
• SDL_CONTROLLERDEVICEREMAPPED => SDL_EVENT_GAMEPAD_REMAPPED
• SDL_CONTROLLERDEVICEREMOVED => SDL_EVENT_GAMEPAD_REMOVED
• SDL_CONTROLLERSENSORUPDATE => SDL_EVENT_GAMEPAD_SENSOR_UPDATE
• SDL_CONTROLLERSTEAMHANDLEUPDATED => SDL_EVENT_GAMEPAD_STEAM_HANDLE_UPDATED
• SDL_CONTROLLERTOUCHPADDOWN => SDL_EVENT_GAMEPAD_TOUCHPAD_DOWN
• SDL_CONTROLLERTOUCHPADMOTION => SDL_EVENT_GAMEPAD_TOUCHPAD_MOTION
• SDL_CONTROLLERTOUCHPADUP => SDL_EVENT_GAMEPAD_TOUCHPAD_UP
• SDL_DROPBEGIN => SDL_EVENT_DROP_BEGIN
• SDL_DROPCOMPLETE => SDL_EVENT_DROP_COMPLETE
• SDL_DROPFILE => SDL_EVENT_DROP_FILE
• SDL_DROPTEXT => SDL_EVENT_DROP_TEXT
• SDL_FINGERDOWN => SDL_EVENT_FINGER_DOWN
• SDL_FINGERMOTION => SDL_EVENT_FINGER_MOTION
• SDL_FINGERUP => SDL_EVENT_FINGER_UP
• SDL_FIRSTEVENT => SDL_EVENT_FIRST
• SDL_JOYAXISMOTION => SDL_EVENT_JOYSTICK_AXIS_MOTION
• SDL_JOYBALLMOTION => SDL_EVENT_JOYSTICK_BALL_MOTION
• SDL_JOYBATTERYUPDATED => SDL_EVENT_JOYSTICK_BATTERY_UPDATED
• SDL_JOYBUTTONDOWN => SDL_EVENT_JOYSTICK_BUTTON_DOWN
• SDL_JOYBUTTONUP => SDL_EVENT_JOYSTICK_BUTTON_UP
• SDL_JOYDEVICEADDED => SDL_EVENT_JOYSTICK_ADDED
• SDL_JOYDEVICEREMOVED => SDL_EVENT_JOYSTICK_REMOVED
• SDL_JOYHATMOTION => SDL_EVENT_JOYSTICK_HAT_MOTION
• SDL_KEYDOWN => SDL_EVENT_KEY_DOWN
• SDL_KEYMAPCHANGED => SDL_EVENT_KEYMAP_CHANGED
• SDL_KEYUP => SDL_EVENT_KEY_UP
• SDL_LASTEVENT => SDL_EVENT_LAST
• SDL_LOCALECHANGED => SDL_EVENT_LOCALE_CHANGED
• SDL_MOUSEBUTTONDOWN => SDL_EVENT_MOUSE_BUTTON_DOWN
• SDL_MOUSEBUTTONUP => SDL_EVENT_MOUSE_BUTTON_UP
• SDL_MOUSEMOTION => SDL_EVENT_MOUSE_MOTION
• SDL_MOUSEWHEEL => SDL_EVENT_MOUSE_WHEEL
• SDL_POLLSENTINEL => SDL_EVENT_POLL_SENTINEL
• SDL_QUIT => SDL_EVENT_QUIT
• SDL_RENDER_DEVICE_RESET => SDL_EVENT_RENDER_DEVICE_RESET
• SDL_RENDER_TARGETS_RESET => SDL_EVENT_RENDER_TARGETS_RESET
• SDL_SENSORUPDATE => SDL_EVENT_SENSOR_UPDATE
• SDL_TEXTEDITING => SDL_EVENT_TEXT_EDITING
• SDL_TEXTEDITING_EXT => SDL_EVENT_TEXT_EDITING_EXT
• SDL_TEXTINPUT => SDL_EVENT_TEXT_INPUT
• SDL_USEREVENT => SDL_EVENT_USER

## Removed Symbols

The following symbols have been removed:

• SDL_DROPEVENT_DATA_SIZE - drop event data is dynamically allocated
• SDL_SYSWMEVENT - you can use SDL_SetWindowsMessageHook() and
SDL_SetX11EventHook() to watch and modify system events before SDL sees them.
• SDL_TEXTEDITINGEVENT_TEXT_SIZE - text editing event data is dynamically
allocated

## Structure Renames

The following structures have been renamed:

• SDL_ControllerAxisEvent => SDL_GamepadAxisEvent
• SDL_ControllerButtonEvent => SDL_GamepadButtonEvent
• SDL_ControllerDeviceEvent => SDL_GamepadDeviceEvent
• SDL_ControllerSensorEvent => SDL_GamepadSensorEvent
• SDL_ControllerTouchpadEvent => SDL_GamepadTouchpadEvent

## Removed Functions

The following functions have been removed:

• SDL_EventState() - replaced with SDL_SetEventEnabled()
• SDL_GetEventState() - replaced with SDL_EventEnabled()

## Enum Renames

The following enums have been renamed:

• SDL_eventaction => SDL_EventAction

## Function Renames

The following functions have been renamed:

• SDL_DelEventWatch() => SDL_RemoveEventWatch()
"""
