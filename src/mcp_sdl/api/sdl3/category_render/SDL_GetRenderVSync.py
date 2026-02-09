"""SDL_GetRenderVSync function definition."""

FUNCTION = {
    "SDL_GetRenderVSync": {
        "category": "render",
        "description": "Get VSync of the given renderer",
        "signature": "bool SDL_GetRenderVSync(SDL_Renderer *renderer, int *vsync)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer from which VSync should be queried"},
            {"name": "vsync", "type": "int*", "description": "Pointer filled in with 1 for on, 0 for off, or adaptive vsync"}
        ],
        "returns": "true on success or false on failure",
        "example": """int vsync;
if (SDL_GetRenderVSync(renderer, &vsync)) {
    SDL_Log("VSync is %s", vsync ? "enabled" : "disabled");
}""",
        "remarks": "VSync synchronizes rendering with monitor refresh to prevent screen tearing",
        "see_also": ["SDL_SetRenderVSync"]
    }
}
