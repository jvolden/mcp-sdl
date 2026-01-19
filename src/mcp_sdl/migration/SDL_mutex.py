"""SDL_mutex.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_mutex.h"

MIGRATION_DATA = """
# SDL_mutex.h Migration Guide

## Timeout Changes

SDL_MUTEX_MAXWAIT has been removed; it suggested there was a maximum timeout one
could outlive, instead of an infinite wait. Instead, pass a -1 to functions
that accepted this symbol.

SDL_MUTEX_TIMEDOUT has been removed, the wait functions return true if the
operation succeeded or false if they timed out.

## Return Type Changes

SDL_LockMutex(), SDL_UnlockMutex(), SDL_WaitSemaphore(), SDL_SignalSemaphore(),
SDL_WaitCondition(), SDL_SignalCondition(), and SDL_BroadcastCondition() now
return void; if the object is valid (including being a NULL pointer, which returns
immediately), these functions never fail. If the object is invalid or the caller
does something illegal, like unlock another thread's mutex, this is considered
undefined behavior.

SDL_TryWaitSemaphore(), SDL_WaitSemaphoreTimeout(), and
SDL_WaitConditionTimeout() now return true if the operation succeeded or false if they timed out.

## Function Renames

The following functions have been renamed:

• SDL_CondBroadcast() => SDL_BroadcastCondition()
• SDL_CondSignal() => SDL_SignalCondition()
• SDL_CondWait() => SDL_WaitCondition()
• SDL_CondWaitTimeout() => SDL_WaitConditionTimeout(), returns bool
• SDL_CreateCond() => SDL_CreateCondition()
• SDL_DestroyCond() => SDL_DestroyCondition()
• SDL_SemPost() => SDL_SignalSemaphore()
• SDL_SemTryWait() => SDL_TryWaitSemaphore(), returns bool
• SDL_SemValue() => SDL_GetSemaphoreValue()
• SDL_SemWait() => SDL_WaitSemaphore()
• SDL_SemWaitTimeout() => SDL_WaitSemaphoreTimeout(), returns bool

## Symbol Renames

The following symbols have been renamed:

• SDL_cond => SDL_Condition
• SDL_mutex => SDL_Mutex
• SDL_sem => SDL_Semaphore
"""
