"""SDL_GetRenderWindow function definition."""

FUNCTION = {
    "SDL_GetRenderWindow": {
        "category": "render",
        "description": "Get the window associated with a renderer",
        "signature": "SDL_Window* SDL_GetRenderWindow(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer to query"}
        ],
        "returns": "The window associated with the renderer, or NULL if the renderer isn't bound to a window",
        "example": """// Get window from renderer
SDL_Window *window = SDL_GetRenderWindow(renderer);"""
    }
}
