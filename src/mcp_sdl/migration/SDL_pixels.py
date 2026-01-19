"""SDL_pixels.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_pixels.h"

MIGRATION_DATA = """
# SDL_pixels.h Migration Guide

## Pixel Format Structure Changes

SDL_PixelFormat has been renamed SDL_PixelFormatDetails and just describes the
pixel format, it does not include a palette for indexed pixel types.

SDL_PixelFormatEnum has been renamed SDL_PixelFormat and is used instead of
Uint32 for API functions that refer to pixel format by enumerated value.

## Color Mapping and Palette Changes

SDL_MapRGB(), SDL_MapRGBA(), SDL_GetRGB(), and SDL_GetRGBA() take an optional
palette parameter for indexed color lookups.

Code that used to look like this:

```c
SDL_GetRGBA(pixel, surface->format, &r, &g, &b, &a);
```

should be changed to:

```c
SDL_GetRGBA(pixel, SDL_GetPixelFormatDetails(surface->format), SDL_GetSurfacePalette(surface), &r, &g, &b, &a);
```

Code that used to look like this:

```c
pixel = SDL_MapRGBA(surface->format, r, g, b, a);
```

should be changed to:

```c
pixel = SDL_MapSurfaceRGBA(surface, r, g, b, a);
```

## Removed Functions

SDL_CalculateGammaRamp has been removed, because SDL_SetWindowGammaRamp has been
removed as well due to poor support in modern operating systems (see SDL_video.h).

## Function Renames

The following functions have been renamed:

• SDL_AllocFormat() => SDL_GetPixelFormatDetails()
• SDL_AllocPalette() => SDL_CreatePalette()
• SDL_FreePalette() => SDL_DestroyPalette()
• SDL_MasksToPixelFormatEnum() => SDL_GetPixelFormatForMasks()
• SDL_PixelFormatEnumToMasks() => SDL_GetMasksForPixelFormat(), returns bool

## Symbol Renames

The following symbols have been renamed:

• SDL_PIXELFORMAT_BGR444 => SDL_PIXELFORMAT_XBGR4444
• SDL_PIXELFORMAT_BGR555 => SDL_PIXELFORMAT_XBGR1555
• SDL_PIXELFORMAT_BGR888 => SDL_PIXELFORMAT_XBGR8888
• SDL_PIXELFORMAT_RGB444 => SDL_PIXELFORMAT_XRGB4444
• SDL_PIXELFORMAT_RGB555 => SDL_PIXELFORMAT_XRGB1555
• SDL_PIXELFORMAT_RGB888 => SDL_PIXELFORMAT_XRGB8888

## Removed Functions

The following functions have been removed:

• SDL_FreeFormat()
• SDL_SetPixelFormatPalette()
• SDL_CalculateGammaRamp()

## Removed Macros

The following macros have been removed:

• SDL_Colour - use SDL_Color instead

## Structure Renames

The following structures have been renamed:

• SDL_PixelFormat => SDL_PixelFormatDetails
"""
