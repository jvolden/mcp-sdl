"""SDL_surface.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_surface.h"

MIGRATION_DATA = """
# SDL_surface.h Migration Guide

## Surface Structure Changes

SDL_Surface has been simplified and internal details are no longer in the public
structure.

The `format` member of SDL_Surface is now an enumerated pixel format value. You can get the
full details of the pixel format by calling `SDL_GetPixelFormatDetails(surface->format)`. You can get the palette associated with the surface by calling
SDL_GetSurfacePalette(). You can get the clip rectangle by calling SDL_GetSurfaceClipRect().

The userdata member of SDL_Surface has been replaced with a more general
properties interface, which can be queried with SDL_GetSurfaceProperties()

## Indexed Format Changes

Indexed format surfaces no longer have a palette by default. Surfaces without a
palette will copy the pixels untranslated between surfaces.

Code that used to look like this:

```c
SDL_Surface *surface = SDL_CreateRGBSurfaceWithFormat(0, 32, 32, 8, SDL_PIXELFORMAT_INDEX8);
SDL_Palette *palette = surface->format->palette;
```

should be changed to:

```c
SDL_Surface *surface = SDL_CreateSurface(32, 32, SDL_PIXELFORMAT_INDEX8);
SDL_Palette *palette = SDL_CreateSurfacePalette(surface);
```

## Function Parameter Changes

Removed the unused 'flags' parameter from SDL_ConvertSurface.

SDL_CreateRGBSurface() and SDL_CreateRGBSurfaceWithFormat() have been combined
into a new function SDL_CreateSurface(). SDL_CreateRGBSurfaceFrom() and
SDL_CreateRGBSurfaceWithFormatFrom() have been combined into a new function
SDL_CreateSurfaceFrom(), and the parameter order has changed for consistency with
SDL_CreateSurface().

SDL_BlitSurface() and SDL_BlitSurfaceScaled() now have a const `dstrect` parameter and do not fill it in with the final destination rectangle.

SDL_BlitSurfaceScaled() and SDL_BlitSurfaceUncheckedScaled() now take a scale
parameter.

SDL_PixelFormat is used instead of Uint32 for API functions that refer to pixel
format by enumerated value.

SDL_SetSurfaceColorKey() takes an bool to enable and disable colorkey. RLE
acceleration isn't controlled by the parameter, you should use SDL_SetSurfaceRLE() to
change that separately.

SDL_SetSurfaceRLE() takes an bool to enable and disable RLE acceleration.

## Function Renames

The following functions have been renamed:

• SDL_BlitScaled() => SDL_BlitSurfaceScaled(), returns bool
• SDL_ConvertSurfaceFormat() => SDL_ConvertSurface()
• SDL_FillRect() => SDL_FillSurfaceRect(), returns bool
• SDL_FillRects() => SDL_FillSurfaceRects(), returns bool
• SDL_FreeSurface() => SDL_DestroySurface()
• SDL_GetClipRect() => SDL_GetSurfaceClipRect(), returns bool
• SDL_GetColorKey() => SDL_GetSurfaceColorKey(), returns bool
• SDL_HasColorKey() => SDL_SurfaceHasColorKey()
• SDL_HasSurfaceRLE() => SDL_SurfaceHasRLE()
• SDL_LoadBMP_RW() => SDL_LoadBMP_IO()
• SDL_LowerBlit() => SDL_BlitSurfaceUnchecked(), returns bool
• SDL_LowerBlitScaled() => SDL_BlitSurfaceUncheckedScaled(), returns bool
• SDL_SaveBMP_RW() => SDL_SaveBMP_IO(), returns bool
• SDL_SetClipRect() => SDL_SetSurfaceClipRect()
• SDL_SetColorKey() => SDL_SetSurfaceColorKey(), returns bool
• SDL_UpperBlit() => SDL_BlitSurface(), returns bool
• SDL_UpperBlitScaled() => SDL_BlitSurfaceScaled(), returns bool

## Removed Symbols

The following symbols have been removed:

• SDL_SWSURFACE

## Removed Functions

The following functions have been removed:

• SDL_FreeFormat()
• SDL_GetYUVConversionMode()
• SDL_GetYUVConversionModeForResolution()
• SDL_SetYUVConversionMode() - use SDL_SetSurfaceColorspace() and
SDL_PROP_TEXTURE_CREATE_COLORSPACE_NUMBER instead
• SDL_SoftStretch() - use SDL_StretchSurface() with SDL_SCALEMODE_NEAREST
• SDL_SoftStretchLinear() - use SDL_StretchSurface() with SDL_SCALEMODE_LINEAR

## Symbol Renames

The following symbols have been renamed:

• SDL_PREALLOC => SDL_SURFACE_PREALLOCATED
• SDL_SIMD_ALIGNED => SDL_SURFACE_SIMD_ALIGNED
"""
