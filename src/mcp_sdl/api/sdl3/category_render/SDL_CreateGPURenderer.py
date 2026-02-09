"""SDL_CreateGPURenderer function definition."""

FUNCTION = {
    "SDL_CreateGPURenderer": {
        "category": "render",
        "description": "Create a GPU-based rendering context for a window",
        "signature": "SDL_Renderer* SDL_CreateGPURenderer(SDL_Window *window, const char *name)",
        "parameters": [
            {"name": "window", "type": "SDL_Window*", "description": "The window where rendering is displayed"},
            {"name": "name", "type": "const char*", "description": "The name of the GPU driver to initialize, or NULL"}
        ],
        "returns": "A valid rendering context or NULL on failure",
        "example": """SDL_Renderer *renderer = SDL_CreateGPURenderer(window, NULL);
if (!renderer) {
    SDL_Log("Could not create GPU renderer: %s", SDL_GetError());
}""",
        "remarks": "Part of SDL3's new GPU API for high-performance graphics",
        "see_also": ["SDL_CreateRenderer", "SDL_DestroyRenderer", "SDL_GetGPURendererDevice"]
    }
}
