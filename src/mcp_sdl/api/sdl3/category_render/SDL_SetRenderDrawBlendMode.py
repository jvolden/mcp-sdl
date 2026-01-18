"""SDL_SetRenderDrawBlendMode function definition."""

FUNCTION = {
    "SDL_SetRenderDrawBlendMode": {
        "category": "render",
        "description": "Set the blend mode used for drawing operations",
        "signature": "bool SDL_SetRenderDrawBlendMode(SDL_Renderer *renderer, SDL_BlendMode blendMode)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "blendMode", "type": "SDL_BlendMode", "description": "The SDL_BlendMode to use"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Set blend mode for alpha blending
SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND);"""
    }
}
