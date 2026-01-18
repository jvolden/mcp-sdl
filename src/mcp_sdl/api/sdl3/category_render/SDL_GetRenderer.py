"""SDL_GetRenderer function definition."""

FUNCTION = {
    "SDL_GetRenderer": {
        "category": "render",
        "description": "Get the renderer associated with a window",
        "signature": "SDL_Renderer* SDL_GetRenderer(SDL_Window *window)",
        "parameters": [
            {"name": "window", "type": "SDL_Window*", "description": "The window to query"}
        ],
        "returns": "The renderer associated with the window, or NULL if there isn't one",
        "example": """// Get renderer from window
SDL_Renderer *renderer = SDL_GetRenderer(window);"""
    }
}
