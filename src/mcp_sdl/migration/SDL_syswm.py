"""SDL_syswm.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_syswm.h"

MIGRATION_DATA = """
# SDL_syswm.h Migration Guide

This header has been removed.

## Event Callbacks

The Windows and X11 events are now available via callbacks which you can set
with SDL_SetWindowsMessageHook() and SDL_SetX11EventHook().

## Window Properties

The information previously available in SDL_GetWindowWMInfo() is now available
as window properties. For example:

SDL2 code:

```c
#if defined(__WIN32__)
    HWND hwnd = NULL;
    if (SDL_GetWindowWMInfo(window, &info) && info.subsystem == SDL_SYSWM_WINDOWS) {
        hwnd = info.info.win.window;
    }
#elif defined(__MACOSX__)
    NSWindow *nswindow = NULL;
    if (SDL_GetWindowWMInfo(window, &info) && info.subsystem == SDL_SYSWM_COCOA) {
        nswindow = (__bridge NSWindow *)info.info.cocoa.window;
    }
#endif
```

SDL3 code:

```c
#if defined(SDL_PLATFORM_WIN32)
    HWND hwnd = (HWND)SDL_GetPointerProperty(SDL_GetWindowProperties(window), SDL_PROP_WINDOW_WIN32_HWND_POINTER, NULL);
#elif defined(SDL_PLATFORM_MACOS)
    NSWindow *nswindow = (__bridge NSWindow *)SDL_GetPointerProperty(SDL_GetWindowProperties(window), SDL_PROP_WINDOW_COCOA_WINDOW_POINTER, NULL);
#endif
```

Platform-specific window properties are available for Windows, macOS, X11, Wayland, iOS, Android, and other supported platforms.
"""
