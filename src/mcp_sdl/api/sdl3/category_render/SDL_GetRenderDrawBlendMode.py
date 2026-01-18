"""SDL_GetRenderDrawBlendMode function definition."""

FUNCTION = {
    "SDL_GetRenderDrawBlendMode": {
        "category": "render",
        "description": "Get the blend mode used for drawing operations",
        "signature": "bool SDL_GetRenderDrawBlendMode(SDL_Renderer *renderer, SDL_BlendMode *blendMode)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "blendMode", "type": "SDL_BlendMode*", "description": "Pointer to store the current SDL_BlendMode"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get current blend mode
SDL_BlendMode blendMode;
SDL_GetRenderDrawBlendMode(renderer, &blendMode);"""
    }
}
