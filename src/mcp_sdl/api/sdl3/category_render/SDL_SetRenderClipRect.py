"""SDL_SetRenderClipRect function definition."""

FUNCTION = {
    "SDL_SetRenderClipRect": {
        "category": "render",
        "description": "Set the clip rectangle for rendering on the current target",
        "signature": "bool SDL_SetRenderClipRect(SDL_Renderer *renderer, const SDL_Rect *rect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rect", "type": "const SDL_Rect*", "description": "The SDL_Rect structure for the clip area, or NULL to disable clipping"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Set clip rectangle
SDL_Rect clip = {100, 100, 200, 200};
SDL_SetRenderClipRect(renderer, &clip);

// Disable clipping
SDL_SetRenderClipRect(renderer, NULL);"""
    }
}
