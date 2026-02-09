"""SDL_CreateWindowAndRenderer function definition."""

FUNCTION = {
    "SDL_CreateWindowAndRenderer": {
        "category": "render",
        "description": "Create a window and default renderer",
        "signature": "bool SDL_CreateWindowAndRenderer(const char *title, int width, int height, SDL_WindowFlags window_flags, SDL_Window **window, SDL_Renderer **renderer)",
        "parameters": [
            {"name": "title", "type": "const char*", "description": "The title of the window, in UTF-8 encoding"},
            {"name": "width", "type": "int", "description": "The width of the window"},
            {"name": "height", "type": "int", "description": "The height of the window"},
            {"name": "window_flags", "type": "SDL_WindowFlags", "description": "The flags for the window"},
            {"name": "window", "type": "SDL_Window**", "description": "Pointer filled with the window, or NULL on error"},
            {"name": "renderer", "type": "SDL_Renderer**", "description": "Pointer filled with the renderer, or NULL on error"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_Window *window;
SDL_Renderer *renderer;
if (SDL_CreateWindowAndRenderer("Game", 800, 600, 0, &window, &renderer)) {
    SDL_Log("Window and renderer created successfully");
}""",
        "remarks": "Convenient function for simple applications that need one window and renderer",
        "see_also": ["SDL_CreateWindow", "SDL_CreateRenderer", "SDL_DestroyRenderer", "SDL_DestroyWindow"]
    }
}
