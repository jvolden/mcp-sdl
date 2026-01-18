"""SDL_video.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_video.h"

MIGRATION_DATA = """
# SDL_video.h Migration Guide

Several video backends have had their names lower-cased ("kmsdrm", "rpi",
"android", "psp", "ps2", "vita"). SDL already does a case-insensitive compare for
SDL_HINT_VIDEO_DRIVER tests, but if your app is calling SDL_GetVideoDriver() or
SDL_GetCurrentVideoDriver() and doing case-sensitive compares on those strings,
please update your code.

## Video Subsystem Initialization

SDL_VideoInit() and SDL_VideoQuit() have been removed. Instead you can call
SDL_InitSubSystem() and SDL_QuitSubSystem() with SDL_INIT_VIDEO, which will properly
refcount the subsystems. You can choose a specific video driver using
SDL_HINT_VIDEO_DRIVER.

## Display and Display Mode Changes

Rather than iterating over displays using display index, there is a new function
SDL_GetDisplays() to get the current list of displays, and functions which used
to take a display index now take SDL_DisplayID, with an invalid ID being 0.

Example:
```c
{
    if (SDL_InitSubSystem(SDL_INIT_VIDEO)) {
        int i, num_displays = 0;
        SDL_DisplayID *displays = SDL_GetDisplays(&num_displays);
        if (displays) {
            for (i = 0; i < num_displays; ++i) {
                SDL_DisplayID instance_id = displays[i];
                const char *name = SDL_GetDisplayName(instance_id);
                SDL_Log("Display %" SDL_PRIu32 ": %s", instance_id, name ? name : "Unknown");
            }
            SDL_free(displays);
        }
        SDL_QuitSubSystem(SDL_INIT_VIDEO);
    }
}
```

SDL_DisplayMode now includes the pixel density which can be greater than 1.0 for
display modes that have a higher pixel size than the mode size. You should use
SDL_GetWindowSizeInPixels() to get the actual pixel size of the window back buffer.

The refresh rate in SDL_DisplayMode is now a float, as well as being represented
as a precise fraction with numerator and denominator.

Rather than iterating over display modes using an index, there is a new function
SDL_GetFullscreenDisplayModes() to get the list of available fullscreen modes on a display.

SDL_GetDesktopDisplayMode() and SDL_GetCurrentDisplayMode() return pointers to
display modes rather than filling in application memory.

## Window Creation

SDL_CreateWindow() has been simplified and no longer takes a window position.
You can use SDL_CreateWindowWithProperties() if you need to set the window
position when creating it.

Example:
```c
SDL_PropertiesID props = SDL_CreateProperties();
SDL_SetStringProperty(props, SDL_PROP_WINDOW_CREATE_TITLE_STRING, title);
SDL_SetNumberProperty(props, SDL_PROP_WINDOW_CREATE_X_NUMBER, x);
SDL_SetNumberProperty(props, SDL_PROP_WINDOW_CREATE_Y_NUMBER, y);
SDL_SetNumberProperty(props, SDL_PROP_WINDOW_CREATE_WIDTH_NUMBER, width);
SDL_SetNumberProperty(props, SDL_PROP_WINDOW_CREATE_HEIGHT_NUMBER, height);
SDL_Window *window = SDL_CreateWindowWithProperties(props);
SDL_DestroyProperties(props);
```

The SDL_WINDOWPOS_UNDEFINED_DISPLAY() and SDL_WINDOWPOS_CENTERED_DISPLAY()
macros take a display ID instead of display index. The display ID 0 has a special
meaning in this case, and is used to indicate the primary display.

The SDL_WINDOW_SHOWN flag has been removed. Windows are shown by default and can
be created hidden by using the SDL_WINDOW_HIDDEN flag.

The SDL_WINDOW_SKIP_TASKBAR flag has been replaced by the SDL_WINDOW_UTILITY flag.

## Fullscreen Changes

Windows now have an explicit fullscreen mode that is set, using
SDL_SetWindowFullscreenMode(). The fullscreen mode for a window can be queried with
SDL_GetWindowFullscreenMode(), which returns a pointer to the mode, or NULL if the window
will be fullscreen desktop. SDL_SetWindowFullscreen() just takes a boolean value,
setting the correct fullscreen state based on the selected mode.

SDL_WINDOW_FULLSCREEN_DESKTOP has been removed, and you can call
SDL_GetWindowFullscreenMode() to see whether an exclusive fullscreen mode will be used or the
borderless fullscreen desktop mode will be used when the window is fullscreen.

## OpenGL Changes

Removed SDL_GL_CONTEXT_EGL from OpenGL configuration attributes. You can instead
use `SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_ES);`

SDL_GL_GetProcAddress() and SDL_EGL_GetProcAddress() now return `SDL_FunctionPointer` instead of `void *`, and should be cast to the appropriate function type.

SDL_GL_DeleteContext() has been renamed to SDL_GL_DestroyContext to match SDL
naming conventions.

SDL_GL_GetSwapInterval() takes the interval as an output parameter and returns
true if the function succeeds or false if there was an error.

SDL_GL_GetDrawableSize() has been removed. SDL_GetWindowSizeInPixels() can be
used in its place.

## Popup Windows

The SDL_WINDOW_TOOLTIP and SDL_WINDOW_POPUP_MENU window flags are now supported
on Windows, Mac (Cocoa), X11, and Wayland. Creating windows with these flags
must happen via the `SDL_CreatePopupWindow()` function. This function requires passing in the handle to a valid parent window
for the popup, and the popup window is positioned relative to the parent.

## Removed Features

SDL_SetWindowBrightness(), SDL_GetWindowBrightness, SDL_SetWindowGammaRamp(),
and SDL_GetWindowGammaRamp have been removed from the API, because they interact
poorly with modern operating systems and aren't able to limit their effects to
the SDL window. Programs which have access to shaders can implement more robust versions of
those functions using custom shader code rendered as a post-process effect.

## Asynchronous Window Operations

The following window operations are now considered to be asynchronous requests
and should not be assumed to succeed unless a corresponding event has been received:

• SDL_SetWindowSize() (SDL_EVENT_WINDOW_RESIZED)
• SDL_SetWindowPosition() (SDL_EVENT_WINDOW_MOVED)
• SDL_MinimizeWindow() (SDL_EVENT_WINDOW_MINIMIZED)
• SDL_MaximizeWindow() (SDL_EVENT_WINDOW_MAXIMIZED)
• SDL_RestoreWindow() (SDL_EVENT_WINDOW_RESTORED)
• SDL_SetWindowFullscreen() (SDL_EVENT_WINDOW_ENTER_FULLSCREEN / SDL_EVENT_WINDOW_LEAVE_FULLSCREEN)

If it is required that operations be applied immediately after one of the
preceding calls, the `SDL_SyncWindow()` function will attempt to wait until all pending window operations have
completed.

## Function Renames

The following functions have been renamed:

• SDL_GL_DeleteContext() => SDL_GL_DestroyContext(), returns bool
• SDL_GetClosestDisplayMode() => SDL_GetClosestFullscreenDisplayMode(), returns bool
• SDL_GetDisplayOrientation() => SDL_GetCurrentDisplayOrientation()
• SDL_GetPointDisplayIndex() => SDL_GetDisplayForPoint()
• SDL_GetRectDisplayIndex() => SDL_GetDisplayForRect()
• SDL_GetWindowDisplayIndex() => SDL_GetDisplayForWindow()
• SDL_GetWindowDisplayMode() => SDL_GetWindowFullscreenMode()
• SDL_HasWindowSurface() => SDL_WindowHasSurface()
• SDL_IsScreenSaverEnabled() => SDL_ScreenSaverEnabled()
• SDL_SetWindowDisplayMode() => SDL_SetWindowFullscreenMode(), returns bool

## Removed Functions

The following functions have been removed:

• SDL_GetDisplayDPI() - not reliable across platforms, approximately replaced by
  multiplying SDL_GetWindowDisplayScale() times 160 on iPhone and Android, and 96
  on other platforms.
• SDL_GetDisplayMode()
• SDL_GetNumDisplayModes() - replaced with SDL_GetFullscreenDisplayModes()
• SDL_GetNumVideoDisplays() - replaced with SDL_GetDisplays()
• SDL_SetWindowGrab() - use SDL_SetWindowMouseGrab() instead
• SDL_GetWindowGrab() - use SDL_GetWindowMouseGrab() instead
• SDL_GetWindowData() - use SDL_GetPointerProperty() with SDL_GetWindowProperties()
• SDL_SetWindowData() - use SDL_SetPointerProperty() with SDL_GetWindowProperties()
• SDL_CreateWindowFrom() - use SDL_CreateWindowWithProperties()
• SDL_SetWindowInputFocus() - use SDL_RaiseWindow() instead
• SDL_SetWindowModalFor() - use SDL_SetWindowParent() with SDL_SetWindowModal()
• SDL_SetWindowBrightness() - use a shader or other in-game effect
• SDL_GetWindowBrightness() - use a shader or other in-game effect
• SDL_SetWindowGammaRamp() - use a shader or other in-game effect
• SDL_GetWindowGammaRamp() - use a shader or other in-game effect

## Type Changes

SDL_WindowFlags is used instead of Uint32 for API functions that refer to window
flags, and has been extended to 64 bits.

SDL_GetWindowOpacity() directly returns the opacity instead of using an out parameter.

The SDL_Window id type is named SDL_WindowID

## Symbol Renames

The following symbols have been renamed:

• SDL_DISPLAYEVENT_DISCONNECTED => SDL_EVENT_DISPLAY_REMOVED
• SDL_DISPLAYEVENT_MOVED => SDL_EVENT_DISPLAY_MOVED
• SDL_DISPLAYEVENT_ORIENTATION => SDL_EVENT_DISPLAY_ORIENTATION
• SDL_GLattr => SDL_GLAttr
• SDL_GLcontextFlag => SDL_GLContextFlag
• SDL_GLcontextReleaseFlag => SDL_GLContextReleaseFlag
• SDL_GLprofile => SDL_GLProfile
• SDL_WINDOWEVENT_CLOSE => SDL_EVENT_WINDOW_CLOSE_REQUESTED
• SDL_WINDOWEVENT_DISPLAY_CHANGED => SDL_EVENT_WINDOW_DISPLAY_CHANGED
• SDL_WINDOWEVENT_ENTER => SDL_EVENT_WINDOW_MOUSE_ENTER
• SDL_WINDOWEVENT_EXPOSED => SDL_EVENT_WINDOW_EXPOSED
• SDL_WINDOWEVENT_FOCUS_GAINED => SDL_EVENT_WINDOW_FOCUS_GAINED
• SDL_WINDOWEVENT_FOCUS_LOST => SDL_EVENT_WINDOW_FOCUS_LOST
• SDL_WINDOWEVENT_HIDDEN => SDL_EVENT_WINDOW_HIDDEN
• SDL_WINDOWEVENT_HIT_TEST => SDL_EVENT_WINDOW_HIT_TEST
• SDL_WINDOWEVENT_LEAVE => SDL_EVENT_WINDOW_MOUSE_LEAVE
• SDL_WINDOWEVENT_MAXIMIZED => SDL_EVENT_WINDOW_MAXIMIZED
• SDL_WINDOWEVENT_MINIMIZED => SDL_EVENT_WINDOW_MINIMIZED
• SDL_WINDOWEVENT_MOVED => SDL_EVENT_WINDOW_MOVED
• SDL_WINDOWEVENT_RESIZED => SDL_EVENT_WINDOW_RESIZED
• SDL_WINDOWEVENT_RESTORED => SDL_EVENT_WINDOW_RESTORED
• SDL_WINDOWEVENT_SHOWN => SDL_EVENT_WINDOW_SHOWN
• SDL_WINDOW_ALLOW_HIGHDPI => SDL_WINDOW_HIGH_PIXEL_DENSITY
• SDL_WINDOW_INPUT_GRABBED => SDL_WINDOW_MOUSE_GRABBED

## Symbol Removals

The following symbols have been removed:

• SDL_WINDOWEVENT_SIZE_CHANGED - handle SDL_EVENT_WINDOW_RESIZED and
  SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED events instead
• SDL_WINDOWEVENT_TAKE_FOCUS
"""
