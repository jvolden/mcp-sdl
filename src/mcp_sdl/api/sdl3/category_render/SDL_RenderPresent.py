"""SDL_RenderPresent function definition."""

FUNCTION = {
    "SDL_RenderPresent": {
        "category": "render",
        "description": "Update the screen with any rendering performed since the previous call",
        "signature": "bool SDL_RenderPresent(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "true on success or false on failure",
        "example": """// Present the rendered frame
SDL_RenderPresent(renderer);"""
    }
}
