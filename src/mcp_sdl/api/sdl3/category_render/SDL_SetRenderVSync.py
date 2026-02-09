"""SDL_SetRenderVSync function definition."""

FUNCTION = {
    "SDL_SetRenderVSync": {
        "category": "render",
        "description": "Set VSync of the given renderer",
        "signature": "bool SDL_SetRenderVSync(SDL_Renderer *renderer, int vsync)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer for which VSync should be set"},
            {"name": "vsync", "type": "int", "description": "1 for on, 0 for off, or adaptive vsync"}
        ],
        "returns": "true on success or false on failure",
        "example": """if (SDL_SetRenderVSync(renderer, 1)) {
    SDL_Log("VSync enabled");
} else {
    SDL_Log("Failed to enable VSync: %s", SDL_GetError());
}""",
        "remarks": "VSync prevents screen tearing but may limit frame rate to display refresh rate",
        "see_also": ["SDL_GetRenderVSync"]
    }
}
