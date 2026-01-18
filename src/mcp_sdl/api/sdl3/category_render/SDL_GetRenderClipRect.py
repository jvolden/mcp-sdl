"""SDL_GetRenderClipRect function definition."""

FUNCTION = {
    "SDL_GetRenderClipRect": {
        "category": "render",
        "description": "Get the clip rectangle for the current target",
        "signature": "bool SDL_GetRenderClipRect(SDL_Renderer *renderer, SDL_Rect *rect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rect", "type": "SDL_Rect*", "description": "Pointer to an SDL_Rect structure filled in with the current clipping area"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get current clip rectangle
SDL_Rect clip;
SDL_GetRenderClipRect(renderer, &clip);
SDL_Log("Clip: %d,%d %dx%d", clip.x, clip.y, clip.w, clip.h);"""
    }
}
