"""SDL_rect.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_rect.h"

MIGRATION_DATA = """
# SDL_rect.h Migration Guide

## Function Renames

The following functions have been renamed:

• SDL_EncloseFPoints() => SDL_GetRectEnclosingPointsFloat()
• SDL_EnclosePoints() => SDL_GetRectEnclosingPoints()
• SDL_FRectEmpty() => SDL_RectEmptyFloat()
• SDL_FRectEquals() => SDL_RectsEqualFloat()
• SDL_FRectEqualsEpsilon() => SDL_RectsEqualEpsilon()
• SDL_HasIntersection() => SDL_HasRectIntersection()
• SDL_HasIntersectionF() => SDL_HasRectIntersectionFloat()
• SDL_IntersectFRect() => SDL_GetRectIntersectionFloat()
• SDL_IntersectFRectAndLine() => SDL_GetRectAndLineIntersectionFloat()
• SDL_IntersectRect() => SDL_GetRectIntersection()
• SDL_IntersectRectAndLine() => SDL_GetRectAndLineIntersection()
• SDL_PointInFRect() => SDL_PointInRectFloat()
• SDL_RectEquals() => SDL_RectsEqual()
• SDL_UnionFRect() => SDL_GetRectUnionFloat(), returns bool
• SDL_UnionRect() => SDL_GetRectUnion(), returns bool
"""
