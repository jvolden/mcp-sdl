"""SDL_FlushRenderer function definition."""

FUNCTION = {
    "SDL_FlushRenderer": {
        "category": "render",
        "description": "Force the rendering context to flush any pending commands",
        "signature": "bool SDL_FlushRenderer(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Flush rendering commands
SDL_FlushRenderer(renderer);"""
    }
}
