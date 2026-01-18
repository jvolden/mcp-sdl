"""SDL_DestroyWindow function definition."""

FUNCTION = {
    "SDL_DestroyWindow": {
        "category": "video",
        "description": "Destroy a window",
        "signature": "void SDL_DestroyWindow(SDL_Window *window)",
        "parameters": [
            {"name": "window", "type": "SDL_Window*", "description": "The window to destroy"}
        ],
        "returns": "void",
        "example": """SDL_DestroyWindow(window);"""
    }
}
