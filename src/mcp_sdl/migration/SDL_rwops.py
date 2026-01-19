"""SDL_rwops.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_rwops.h"

MIGRATION_DATA = """
# SDL_rwops.h Migration Guide

## Symbol Renames

The following symbols have been renamed:

• RW_SEEK_CUR => SDL_IO_SEEK_CUR
• RW_SEEK_END => SDL_IO_SEEK_END
• RW_SEEK_SET => SDL_IO_SEEK_SET

## Header Rename

SDL_rwops.h is now named SDL_iostream.h

## Structure Changes

SDL_RWops is now an opaque structure, and has been renamed to SDL_IOStream. The
SDL3 APIs to create an SDL_IOStream (SDL_IOFromFile, etc) are renamed but
otherwise still function as they did in SDL2. However, to make a custom SDL_IOStream
with app-provided function pointers, call SDL_OpenIO and provide the function
pointers through there. To call into an SDL_IOStream's functionality, use the
standard APIs (SDL_ReadIO, etc), as the function pointers are internal.

SDL_IOStream is not to be confused with the unrelated standard C++ iostream
class!

## Function Signature Changes

SDL_RWread and SDL_RWwrite (and the read and write function pointers) have a
different function signature in SDL3, in addition to being renamed.

Previously they looked more like stdio:

```c
size_t SDL_RWread(SDL_RWops *context, void *ptr, size_t size, size_t maxnum);
size_t SDL_RWwrite(SDL_RWops *context, const void *ptr, size_t size, size_t maxnum);
```

But now they look more like POSIX:

```c
size_t SDL_ReadIO(SDL_IOStream *context, void *ptr, size_t size);
size_t SDL_WriteIO(SDL_IOStream *context, const void *ptr, size_t size);
```

Code that used to look like this:

```c
size_t custom_read(void *ptr, size_t size, size_t nitems, SDL_RWops *stream)
{
    return SDL_RWread(stream, ptr, size, nitems);
}
```

should be changed to:

```c
size_t custom_read(void *ptr, size_t size, size_t nitems, SDL_IOStream *stream)
{
    if (size > 0 && nitems > 0) {
        return SDL_ReadIO(stream, ptr, size * nitems) / size;
    }
    return 0;
}
```

## Removed Features

SDL_RWops::type was removed; it wasn't meaningful for app-provided
implementations at all, and wasn't much use for SDL's internal implementations, either. If
you have to identify the type, you can examine the SDL_IOStream's properties to detect
built-in implementations.

SDL_RWFromFP has been removed from the API, due to issues when the SDL library
uses a different C runtime from the application.

## Lifecycle Changes

SDL_AllocRW(), SDL_FreeRW(), SDL_RWclose() and direct access to the `->close` function pointer have been removed from the API, so there's only one path to
manage RWops lifetimes now: SDL_OpenIO() and SDL_CloseIO().

SDL_IOStreamInterface::close implementations should clean up their own userdata,
but not call SDL_CloseIO on themselves; now the contract is always that
SDL_CloseIO is called, which calls `->close` before freeing the opaque object.

## Read/Write Return Type Changes

The functions SDL_ReadU8(), SDL_ReadU16LE(), SDL_ReadU16BE(), SDL_ReadU32LE(),
SDL_ReadU32BE(), SDL_ReadU64LE(), and SDL_ReadU64BE() now return true if the read
succeeded and false if it didn't, and store the data in a pointer passed in as
a parameter.

## Function Renames

The following functions have been renamed:

• SDL_RWFromConstMem() => SDL_IOFromConstMem()
• SDL_RWFromFile() => SDL_IOFromFile()
• SDL_RWFromMem() => SDL_IOFromMem()
• SDL_RWclose() => SDL_CloseIO(), returns bool
• SDL_RWread() => SDL_ReadIO()
• SDL_RWseek() => SDL_SeekIO()
• SDL_RWsize() => SDL_GetIOSize()
• SDL_RWtell() => SDL_TellIO()
• SDL_RWwrite() => SDL_WriteIO()
• SDL_ReadBE16() => SDL_ReadU16BE()
• SDL_ReadBE32() => SDL_ReadU32BE()
• SDL_ReadBE64() => SDL_ReadU64BE()
• SDL_ReadLE16() => SDL_ReadU16LE()
• SDL_ReadLE32() => SDL_ReadU32LE()
• SDL_ReadLE64() => SDL_ReadU64LE()
• SDL_WriteBE16() => SDL_WriteU16BE()
• SDL_WriteBE32() => SDL_WriteU32BE()
• SDL_WriteBE64() => SDL_WriteU64BE()
• SDL_WriteLE16() => SDL_WriteU16LE()
• SDL_WriteLE32() => SDL_WriteU32LE()
• SDL_WriteLE64() => SDL_WriteU64LE()

## Structure Renames

The following structures have been renamed:

• SDL_RWops => SDL_IOStream
"""
