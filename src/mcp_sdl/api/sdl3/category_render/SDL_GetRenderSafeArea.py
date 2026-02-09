"""SDL_GetRenderSafeArea function definition."""

FUNCTION = {
    "SDL_GetRenderSafeArea": {
        "category": "render",
        "description": "Get the safe area for rendering within the current viewport",
        "signature": "bool SDL_GetRenderSafeArea(SDL_Renderer *renderer, SDL_Rect *rect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rect", "type": "SDL_Rect*", "description": "Pointer filled in with the safe area rectangle"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_Rect safe_area;
if (SDL_GetRenderSafeArea(renderer, &safe_area)) {
    SDL_Log("Safe area: %d,%d %dx%d", safe_area.x, safe_area.y, safe_area.w, safe_area.h);
}""",
        "remarks": "Important for TV displays and devices with screen notches",
        "see_also": ["SDL_GetRenderViewport"]
    }
}
