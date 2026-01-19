"""SDL_atomic.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_atomic.h"

MIGRATION_DATA = """
# SDL_atomic.h Migration Guide

## Structure Renames

The following structures have been renamed:

• SDL_atomic_t => SDL_AtomicInt

## Function Renames

The following functions have been renamed:

• SDL_AtomicAdd() => SDL_AddAtomicInt()
• SDL_AtomicCAS() => SDL_CompareAndSwapAtomicInt()
• SDL_AtomicCASPtr() => SDL_CompareAndSwapAtomicPointer()
• SDL_AtomicGet() => SDL_GetAtomicInt()
• SDL_AtomicGetPtr() => SDL_GetAtomicPointer()
• SDL_AtomicLock() => SDL_LockSpinlock()
• SDL_AtomicSet() => SDL_SetAtomicInt()
• SDL_AtomicSetPtr() => SDL_SetAtomicPointer()
• SDL_AtomicTryLock() => SDL_TryLockSpinlock()
• SDL_AtomicUnlock() => SDL_UnlockSpinlock()
"""
