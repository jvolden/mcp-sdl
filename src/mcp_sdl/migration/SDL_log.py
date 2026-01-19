"""SDL_log.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_log.h"

MIGRATION_DATA = """
# SDL_log.h Migration Guide

## Log Prefix Changes

SDL_Log() no longer prints a log prefix by default for SDL_LOG_PRIORITY_INFO and
below. The log prefixes can be customized with SDL_SetLogPriorityPrefix().

## Removed Macros

The following macros have been removed:

• SDL_MAX_LOG_MESSAGE - there's no message length limit anymore. If you need an
artificial limit, this used to be 4096 in SDL versions before 2.0.24.

## Function Renames

The following functions have been renamed:

• SDL_LogGetOutputFunction() => SDL_GetLogOutputFunction()
• SDL_LogGetPriority() => SDL_GetLogPriority()
• SDL_LogResetPriorities() => SDL_ResetLogPriorities()
• SDL_LogSetAllPriority() => SDL_SetLogPriorities()
• SDL_LogSetOutputFunction() => SDL_SetLogOutputFunction()
• SDL_LogSetPriority() => SDL_SetLogPriority()

## Symbol Renames

The following symbols have been renamed:

• SDL_NUM_LOG_PRIORITIES => SDL_LOG_PRIORITY_COUNT
"""
