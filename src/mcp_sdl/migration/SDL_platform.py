"""SDL_platform.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_platform.h"

MIGRATION_DATA = """
# SDL_platform.h Migration Guide

## Platform Macro Renames

The following platform preprocessor macros have been renamed:

• __3DS__ => SDL_PLATFORM_3DS
• __AIX__ => SDL_PLATFORM_AIX
• __ANDROID__ => SDL_PLATFORM_ANDROID
• __APPLE__ => SDL_PLATFORM_APPLE
• __BSDI__ => SDL_PLATFORM_BSDI
• __CYGWIN__ => SDL_PLATFORM_CYGWIN
• __EMSCRIPTEN__ => SDL_PLATFORM_EMSCRIPTEN
• __FREEBSD__ => SDL_PLATFORM_FREEBSD
• __GDK__ => SDL_PLATFORM_GDK
• __HAIKU__ => SDL_PLATFORM_HAIKU
• __HPUX__ => SDL_PLATFORM_HPUX
• __IPHONEOS__ => SDL_PLATFORM_IOS
• __IRIX__ => SDL_PLATFORM_IRIX
• __LINUX__ => SDL_PLATFORM_LINUX
• __MACOSX__ => SDL_PLATFORM_MACOS
• __NETBSD__ => SDL_PLATFORM_NETBSD
• __OPENBSD__ => SDL_PLATFORM_OPENBSD
• __OS2__ => SDL_PLATFORM_OS2
• __OSF__ => SDL_PLATFORM_OSF
• __PS2__ => SDL_PLATFORM_PS2
• __PSP__ => SDL_PLATFORM_PSP
• __QNXNTO__ => SDL_PLATFORM_QNXNTO
• __RISCOS__ => SDL_PLATFORM_RISCOS
• __SOLARIS__ => SDL_PLATFORM_SOLARIS
• __TVOS__ => SDL_PLATFORM_TVOS
• __unix__ => SDL_PLATFORM_UNIX
• __VITA__ => SDL_PLATFORM_VITA
• __WIN32__ => SDL_PLATFORM_WIN32
• __WINGDK__ => SDL_PLATFORM_WINGDK
• __XBOXONE__ => SDL_PLATFORM_XBOXONE
• __XBOXSERIES__ => SDL_PLATFORM_XBOXSERIES

You can use the Python script [rename_macros.py](https://github.com/libsdl-org/SDL/blob/main/build-scripts/rename_macros.py) to automatically rename these in your source code.

A new macro `SDL_PLATFORM_WINDOWS` has been added that is true for all Windows platforms, including Xbox, GDK,
etc.

## Removed Platform Macros

The following platform preprocessor macros have been removed:

• __DREAMCAST__
• __NACL__
• __PNACL__
• __WINDOWS__
• __WINRT__
"""
