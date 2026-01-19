"""SDL_endian.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_endian.h"

MIGRATION_DATA = """
# SDL_endian.h Migration Guide

## Function Renames

The following functions have been renamed:

• SDL_SwapBE16() => SDL_Swap16BE()
• SDL_SwapBE32() => SDL_Swap32BE()
• SDL_SwapBE64() => SDL_Swap64BE()
• SDL_SwapLE16() => SDL_Swap16LE()
• SDL_SwapLE32() => SDL_Swap32LE()
• SDL_SwapLE64() => SDL_Swap64LE()
"""
