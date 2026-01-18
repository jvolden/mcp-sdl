"""SDL_CreateRenderer function definition."""

FUNCTION = {
    "SDL_CreateRenderer": {
        "category": "render",
        "description": "Create a 2D rendering context for a window",
        "signature": "SDL_Renderer* SDL_CreateRenderer(SDL_Window *window, const char *name)",
        "parameters": [
            {"name": "window", "type": "SDL_Window*", "description": "The window where rendering is displayed"},
            {"name": "name", "type": "const char*", "description": "The name of the rendering driver to initialize, or NULL for the first one"}
        ],
        "returns": "A valid rendering context or NULL on failure",
        "example": """SDL_Renderer *renderer = SDL_CreateRenderer(window, NULL);
if (!renderer) {
    SDL_Log("Could not create renderer: %s", SDL_GetError());
}"""
    }
}
