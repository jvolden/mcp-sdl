"""SDL_vulkan.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_vulkan.h"

MIGRATION_DATA = """
# SDL_vulkan.h Migration Guide

## Function Signature Changes

SDL_Vulkan_GetInstanceExtensions() no longer takes a window parameter, and no
longer makes the app allocate query/allocate space for the result, instead
returning a static const internal string.

SDL_Vulkan_GetVkGetInstanceProcAddr() now returns `SDL_FunctionPointer` instead of `void *`, and should be cast to PFN_vkGetInstanceProcAddr.

SDL_Vulkan_CreateSurface() now takes a VkAllocationCallbacks pointer as its
third parameter. If you don't have an allocator to supply, pass a NULL here to use
the system default allocator (SDL2 always used the system default allocator
here).

## Removed Functions

SDL_Vulkan_GetDrawableSize() has been removed. SDL_GetWindowSizeInPixels() can
be used in its place.

SDL_vulkanInstance and SDL_vulkanSurface have been removed. They were for
compatibility with Tizen, who had built their own Vulkan interface into SDL2, but
these apps will need changes for the SDL3 API if they are upgraded anyhow.
"""
