"""SDL_CreateRendererWithProperties function definition."""

FUNCTION = {
    "SDL_CreateRendererWithProperties": {
        "category": "render",
        "description": "Create a 2D rendering context for a window with specified properties",
        "signature": "SDL_Renderer* SDL_CreateRendererWithProperties(SDL_PropertiesID props)",
        "parameters": [
            {"name": "props", "type": "SDL_PropertiesID", "description": "The properties to use for the renderer"}
        ],
        "returns": "A valid rendering context or NULL on failure",
        "example": """SDL_PropertiesID props = SDL_CreateProperties();
SDL_SetPropertyWithID(props, SDL_PROP_RENDERER_CREATE_WINDOW_POINTER, window);
SDL_Renderer *renderer = SDL_CreateRendererWithProperties(props);
SDL_DestroyProperties(props);
if (!renderer) {
    SDL_Log("Could not create renderer: %s", SDL_GetError());
}""",
        "remarks": "Use property constants like SDL_PROP_RENDERER_CREATE_* for configuration",
        "see_also": ["SDL_CreateRenderer", "SDL_DestroyRenderer", "SDL_GetRendererProperties"]
    }
}
