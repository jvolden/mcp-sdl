"""SDL_DestroyRenderer function definition."""

FUNCTION = {
    "SDL_DestroyRenderer": {
        "category": "render",
        "description": "Destroy the rendering context for a window and free all associated resources",
        "signature": "void SDL_DestroyRenderer(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context to destroy"}
        ],
        "returns": "void",
        "example": """SDL_DestroyRenderer(renderer);"""
    }
}
