"""SDL_render.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_render.h"

MIGRATION_DATA = """
# SDL_render.h Migration Guide

The 2D renderer API always uses batching in SDL3. There is no magic to turn it
on and off; it doesn't matter if you select a specific renderer or try to use any
hint. This means that all apps that use SDL3's 2D renderer and also want to
call directly into the platform's lower-layer graphics API must call SDL_FlushRenderer() before doing so. This will make sure any pending
rendering work from SDL is done before the app starts directly drawing.

## Renderer Creation Changes

SDL_GetRenderDriverInfo() has been removed, since most of the information it
reported were estimates and could not be accurate before creating a renderer. Often
times this function was used to figure out the index of a driver, so one would
call it in a for-loop, looking for the driver named "opengl" or whatnot.
SDL_GetRenderDriver() has been added for this functionality, which returns only the
name of the driver.

SDL_CreateRenderer()'s second argument is no longer an integer index, but a `const char *` representing a renderer's name; if you were just using a for-loop to find which
index is the "opengl" or whatnot driver, you can just pass that string directly
here, now. Passing NULL is the same as passing -1 here in SDL2, to signify you
want SDL to decide for you.

SDL_CreateRenderer()'s flags parameter has been removed. See specific flags
below for how to achieve the same functionality in SDL 3.0.

SDL_CreateWindowAndRenderer() now takes the window title as the first parameter.

## Texture and Rendering Changes

Textures are created with SDL_SCALEMODE_LINEAR by default, and use
SDL_BLENDMODE_BLEND by default if they are created with a format that has an alpha channel.

SDL_QueryTexture() has been removed. The properties of the texture can be
queried using SDL_PROP_TEXTURE_FORMAT_NUMBER, SDL_PROP_TEXTURE_ACCESS_NUMBER,
SDL_PROP_TEXTURE_WIDTH_NUMBER, and SDL_PROP_TEXTURE_HEIGHT_NUMBER. A function
SDL_GetTextureSize() has been added to get the size of the texture as floating point
values.

Mouse and touch events are no longer filtered to change their coordinates,
instead you can call SDL_ConvertEventToRenderCoordinates() to explicitly map event
coordinates into the rendering viewport.

SDL_Vertex has been changed to use floating point colors, in the range of [0..1]
for SDR content.

SDL_RenderReadPixels() returns a surface instead of filling in preallocated memory.

## Logical Presentation

SDL_RenderSetLogicalSize() (now called SDL_SetRenderLogicalPresentation()) in
SDL2 would modify the scaling and viewport state. In SDL3, logical presentation
maintains its state separately, so the app can use its own viewport and scaling
while also setting a logical size.

The viewport, clipping state, and scale for render targets are now persistent
and will remain set whenever they are active.

## Function Renames

The following functions have been renamed:

• SDL_GetRendererOutputSize() => SDL_GetCurrentRenderOutputSize(), returns bool
• SDL_RenderCopy() => SDL_RenderTexture(), returns bool
• SDL_RenderCopyEx() => SDL_RenderTextureRotated(), returns bool
• SDL_RenderCopyExF() => SDL_RenderTextureRotated(), returns bool
• SDL_RenderCopyF() => SDL_RenderTexture(), returns bool
• SDL_RenderDrawLine() => SDL_RenderLine(), returns bool
• SDL_RenderDrawLineF() => SDL_RenderLine(), returns bool
• SDL_RenderDrawLines() => SDL_RenderLines(), returns bool
• SDL_RenderDrawLinesF() => SDL_RenderLines(), returns bool
• SDL_RenderDrawPoint() => SDL_RenderPoint(), returns bool
• SDL_RenderDrawPointF() => SDL_RenderPoint(), returns bool
• SDL_RenderDrawPoints() => SDL_RenderPoints(), returns bool
• SDL_RenderDrawPointsF() => SDL_RenderPoints(), returns bool
• SDL_RenderDrawRect() => SDL_RenderRect(), returns bool
• SDL_RenderDrawRectF() => SDL_RenderRect(), returns bool
• SDL_RenderDrawRects() => SDL_RenderRects(), returns bool
• SDL_RenderDrawRectsF() => SDL_RenderRects(), returns bool
• SDL_RenderFillRectF() => SDL_RenderFillRect(), returns bool
• SDL_RenderFillRectsF() => SDL_RenderFillRects(), returns bool
• SDL_RenderFlush() => SDL_FlushRenderer(), returns bool
• SDL_RenderGetClipRect() => SDL_GetRenderClipRect(), returns bool
• SDL_RenderGetIntegerScale() => SDL_GetRenderIntegerScale()
• SDL_RenderGetLogicalSize() => SDL_GetRenderLogicalPresentation(), returns bool
• SDL_RenderGetMetalCommandEncoder() => SDL_GetRenderMetalCommandEncoder()
• SDL_RenderGetMetalLayer() => SDL_GetRenderMetalLayer()
• SDL_RenderGetScale() => SDL_GetRenderScale(), returns bool
• SDL_RenderGetViewport() => SDL_GetRenderViewport(), returns bool
• SDL_RenderGetWindow() => SDL_GetRenderWindow()
• SDL_RenderIsClipEnabled() => SDL_RenderClipEnabled()
• SDL_RenderLogicalToWindow() => SDL_RenderCoordinatesToWindow(), returns bool
• SDL_RenderSetClipRect() => SDL_SetRenderClipRect(), returns bool
• SDL_RenderSetLogicalSize() => SDL_SetRenderLogicalPresentation(), returns bool
• SDL_RenderSetScale() => SDL_SetRenderScale(), returns bool
• SDL_RenderSetVSync() => SDL_SetRenderVSync(), returns bool
• SDL_RenderSetViewport() => SDL_SetRenderViewport(), returns bool
• SDL_RenderWindowToLogical() => SDL_RenderCoordinatesFromWindow(), returns bool

## Removed Functions

The following functions have been removed:

• SDL_GL_BindTexture() - use SDL_GetTextureProperties() to get the OpenGL texture
  ID and bind the texture directly
• SDL_GL_UnbindTexture() - use SDL_GetTextureProperties() to get the OpenGL
  texture ID and unbind the texture directly
• SDL_GetTextureUserData() - use SDL_GetTextureProperties() instead
• SDL_RenderGetIntegerScale()
• SDL_RenderSetIntegerScale() - this is now explicit with
  SDL_LOGICAL_PRESENTATION_INTEGER_SCALE
• SDL_RenderTargetSupported() - render targets are always supported
• SDL_SetTextureUserData() - use SDL_GetTextureProperties() instead

## Enum Changes

The following enums have been renamed:

• SDL_RendererFlip => SDL_FlipMode - moved to SDL_surface.h

## Symbol Renames

The following symbols have been renamed:

• SDL_ScaleModeLinear => SDL_SCALEMODE_LINEAR
• SDL_ScaleModeNearest => SDL_SCALEMODE_NEAREST

## Symbol Removals

The following symbols have been removed:

• SDL_RENDERER_ACCELERATED - all renderers except `SDL_SOFTWARE_RENDERER` are accelerated
• SDL_RENDERER_PRESENTVSYNC - replaced with
  SDL_PROP_RENDERER_CREATE_PRESENT_VSYNC_NUMBER during renderer creation and SDL_PROP_RENDERER_VSYNC_NUMBER after
  renderer creation
• SDL_RENDERER_SOFTWARE - you can check whether the name of the renderer is `SDL_SOFTWARE_RENDERER`
• SDL_RENDERER_TARGETTEXTURE - all renderers support target texture functionality
• SDL_ScaleModeBest - use SDL_SCALEMODE_LINEAR instead
"""
