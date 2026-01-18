"""SDL_CreateWindow function definition."""

FUNCTION = {
    "SDL_CreateWindow": {
        "category": "video",
        "description": "Create a window with the specified position, dimensions, and flags",
        "signature": "SDL_Window* SDL_CreateWindow(const char *title, int w, int h, SDL_WindowFlags flags)",
        "parameters": [
            {"name": "title", "type": "const char*", "description": "Window title"},
            {"name": "w", "type": "int", "description": "Window width in screen coordinates"},
            {"name": "h", "type": "int", "description": "Window height in screen coordinates"},
            {"name": "flags", "type": "SDL_WindowFlags", "description": "Window flags (SDL_WINDOW_RESIZABLE, etc.)"}
        ],
        "returns": "The window that was created or NULL on failure",
        "example": """SDL_Window *window = SDL_CreateWindow(
    "My SDL3 Window",
    800, 600,
    SDL_WINDOW_RESIZABLE
);
if (!window) {
    SDL_Log("Could not create window: %s", SDL_GetError());
}"""
    }
}
