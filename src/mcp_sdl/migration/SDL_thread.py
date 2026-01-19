"""SDL_thread.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_thread.h"

MIGRATION_DATA = """
# SDL_thread.h Migration Guide

## Thread Creation Changes

SDL_CreateThreadWithStackSize has been replaced with
SDL_CreateThreadWithProperties.

SDL_CreateThread and SDL_CreateThreadWithProperties now take
beginthread/endthread function pointers on all platforms (ignoring them on most), and have been
replaced with macros that hide this detail on all platforms. This works the same as
before at the source code level, but the actual function signature that is
called in SDL has changed. The library's exported symbol is SDL_CreateThreadRuntime,
and looking for "SDL_CreateThread" in the DLL/Shared Library/Dylib will fail.
You should not call this directly, but instead always use the macro!

## TLS Changes

SDL_GetTLS() and SDL_SetTLS() take a pointer to a TLS ID, and will automatically
initialize it in a thread-safe way as needed.

## Function Renames

The following functions have been renamed:

• SDL_SetThreadPriority() => SDL_SetCurrentThreadPriority()
• SDL_TLSCleanup() => SDL_CleanupTLS()
• SDL_TLSGet() => SDL_GetTLS()
• SDL_TLSSet() => SDL_SetTLS(), returns bool
• SDL_ThreadID() => SDL_GetCurrentThreadID()

## Removed Functions

The following functions have been removed:

• SDL_TLSCreate() - TLS IDs are automatically allocated as needed.

## Symbol Renames

The following symbols have been renamed:

• SDL_threadID => SDL_ThreadID
"""
