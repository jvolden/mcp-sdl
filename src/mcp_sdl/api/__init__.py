"""
SDL API reference - master module for all SDL libraries.

Currently supports:
- SDL3 (core library)

Future support planned for:
- SDL_image
- SDL_ttf
- SDL_mixer
- SDL_net
"""

from .sdl3 import SDL3_CATEGORIES, SDL3_FUNCTIONS

# Master function dictionary (aggregates all SDL libraries)
ALL_FUNCTIONS = {}
ALL_FUNCTIONS.update(SDL3_FUNCTIONS)

# Master category dictionary
ALL_CATEGORIES = {}
ALL_CATEGORIES.update(SDL3_CATEGORIES)

# Maintain backward compatibility with original names
SDL_FUNCTIONS = SDL3_FUNCTIONS
SDL_CATEGORIES = SDL3_CATEGORIES

# Export everything
__all__ = [
    "SDL_FUNCTIONS",
    "SDL_CATEGORIES",
    "ALL_FUNCTIONS",
    "ALL_CATEGORIES",
    "SDL3_FUNCTIONS",
    "SDL3_CATEGORIES",
]
