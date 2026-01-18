"""SDL_SetRenderViewport function definition."""

FUNCTION = {
    "SDL_SetRenderViewport": {
        "category": "render",
        "description": "Set the drawing area for rendering on the current target",
        "signature": "bool SDL_SetRenderViewport(SDL_Renderer *renderer, const SDL_Rect *rect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rect", "type": "const SDL_Rect*", "description": "The viewport rectangle, or NULL to use the entire target"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Set viewport to left half of window
SDL_Rect viewport = {0, 0, 320, 480};
SDL_SetRenderViewport(renderer, &viewport);

// Reset to full window
SDL_SetRenderViewport(renderer, NULL);"""
    }
}
