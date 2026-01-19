"""SDL_stdinc.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_stdinc.h"

MIGRATION_DATA = """
# SDL_stdinc.h Migration Guide

## Header Changes

The standard C headers like stdio.h and stdlib.h are no longer included, you
should include them directly in your project if you use non-SDL C runtime
functions. M_PI is no longer defined in SDL_stdinc.h, you can use the new symbols
SDL_PI_D (double) and SDL_PI_F (float) instead.

## Bool Type Changes

bool is now defined as bool, and is 1 byte instead of the size of an int.

## Case-Insensitive String Functions

SDL3 attempts to apply consistency to case-insensitive string functions. In
SDL2, things like SDL_strcasecmp() would usually only work on English letters, and
depending on the user's locale, possibly not even those. In SDL3, consistency is
applied:

• SDL_strcasecmp() expects valid UTF-8 strings, and will attempt to support most Unicode characters with a technique known as "case-folding."
• SDL_strncasecmp() works the same, but the third parameter takes bytes.
• SDL_wcscasecmp() and SDL_wcsncasecmp() work the same way but operate on UTF-16
or UTF-32 encoded strings.
• SDL_strcasestr() expects valid UTF-8 strings, and will compare codepoints using
case-folding.
• SDL_tolower() and SDL_toupper() continue to only work on single bytes and only converts low-ASCII English A through Z.
• SDL_strlwr() and SDL_strupr() operates on individual bytes (not UTF-8
codepoints) and only change low-ASCII English 'A' through 'Z'.
• The ctype.h replacement SDL_is*() functions (SDL_isalpha, SDL_isdigit, etc) only
work on low-ASCII characters and ignore user locale, assuming English.

## Type Changes

SDL_strtoll(), SDL_strtoull(), SDL_lltoa(), and SDL_ulltoa() use long long
values instead of 64-bit values, to match their C runtime counterparts.

## Thread Safety

SDL_setenv() is not thread-safe and has been renamed SDL_setenv_unsafe().

## Removed Macros

The following macros have been removed:

• SDL_TABLESIZE() - use SDL_arraysize() instead

## Function Renames

The following functions have been renamed:

• SDL_size_add_overflow() => SDL_size_add_check_overflow(), returns bool
• SDL_size_mul_overflow() => SDL_size_mul_check_overflow(), returns bool
• SDL_strtokr() => SDL_strtok_r()

## Removed Functions

The following functions have been removed:

• SDL_memcpy4()

## Symbol Renames

The following symbols have been renamed:

• SDL_FALSE => false
• SDL_TRUE => true
• SDL_bool => bool
"""
