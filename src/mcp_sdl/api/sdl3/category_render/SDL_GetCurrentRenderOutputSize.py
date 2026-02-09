"""SDL_GetCurrentRenderOutputSize function definition."""

FUNCTION = {
    "SDL_GetCurrentRenderOutputSize": {
        "category": "render",
        "description": "Get the current output size in pixels of a rendering context",
        "signature": "bool SDL_GetCurrentRenderOutputSize(SDL_Renderer *renderer, int *w, int *h)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "w", "type": "int*", "description": "Pointer filled in with the current width"},
            {"name": "h", "type": "int*", "description": "Pointer filled in with the current height"}
        ],
        "returns": "true on success or false on failure",
        "example": """int w, h;
if (SDL_GetCurrentRenderOutputSize(renderer, &w, &h)) {
    SDL_Log("Current output size: %dx%d", w, h);
}""",
        "remarks": "This accounts for high-DPI displays and render targets",
        "see_also": ["SDL_GetRenderOutputSize", "SDL_GetRenderWindow"]
    }
}
