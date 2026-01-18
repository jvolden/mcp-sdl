"""SDL_SetRenderScale function definition."""

FUNCTION = {
    "SDL_SetRenderScale": {
        "category": "render",
        "description": "Set the drawing scale for rendering on the current target",
        "signature": "bool SDL_SetRenderScale(SDL_Renderer *renderer, float scaleX, float scaleY)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "scaleX", "type": "float", "description": "The horizontal scaling factor"},
            {"name": "scaleY", "type": "float", "description": "The vertical scaling factor"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Set 2x scale
SDL_SetRenderScale(renderer, 2.0f, 2.0f);"""
    }
}
