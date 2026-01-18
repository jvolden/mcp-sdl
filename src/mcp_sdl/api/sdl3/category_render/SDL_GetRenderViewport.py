"""SDL_GetRenderViewport function definition."""

FUNCTION = {
    "SDL_GetRenderViewport": {
        "category": "render",
        "description": "Get the drawing area for the current target",
        "signature": "bool SDL_GetRenderViewport(SDL_Renderer *renderer, SDL_Rect *rect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rect", "type": "SDL_Rect*", "description": "Pointer to an SDL_Rect structure filled in with the current drawing area"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get current viewport
SDL_Rect viewport;
if (SDL_GetRenderViewport(renderer, &viewport)) {
    SDL_Log("Viewport: %d,%d %dx%d", viewport.x, viewport.y, viewport.w, viewport.h);
}"""
    }
}
