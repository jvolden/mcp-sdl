"""SDL_RenderClear function definition."""

FUNCTION = {
    "SDL_RenderClear": {
        "category": "render",
        "description": "Clear the current rendering target with the drawing color",
        "signature": "bool SDL_RenderClear(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "true on success or false on failure",
        "example": """// Clear screen with current draw color
SDL_RenderClear(renderer);"""
    }
}
