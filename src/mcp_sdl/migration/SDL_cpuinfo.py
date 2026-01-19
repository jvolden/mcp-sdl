"""SDL_cpuinfo.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_cpuinfo.h"

MIGRATION_DATA = """
# SDL_cpuinfo.h Migration Guide

## Header Changes

The intrinsics headers (mmintrin.h, etc.) have been moved to `<SDL3/SDL_intrin.h>` and are no longer automatically included in SDL.h.

## Removed Functions

SDL_Has3DNow() has been removed; there is no replacement.

SDL_HasRDTSC() has been removed; there is no replacement. Don't use the RDTSC
opcode in modern times, use SDL_GetPerformanceCounter and
SDL_GetPerformanceFrequency instead.

SDL_SIMDAlloc(), SDL_SIMDRealloc(), and SDL_SIMDFree() have been removed. You
can use SDL_aligned_alloc() and SDL_aligned_free() with SDL_GetSIMDAlignment() to
get the same functionality.

## Function Renames

The following functions have been renamed:

• SDL_GetCPUCount() => SDL_GetNumLogicalCPUCores()
• SDL_SIMDGetAlignment() => SDL_GetSIMDAlignment()
"""
