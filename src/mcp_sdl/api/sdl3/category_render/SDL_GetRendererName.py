"""SDL_GetRendererName function definition."""

FUNCTION = {
    "SDL_GetRendererName": {
        "category": "render",
        "description": "Get the name of a renderer",
        "signature": "const char* SDL_GetRendererName(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "The name of the selected renderer, or NULL on failure",
        "example": """const char *name = SDL_GetRendererName(renderer);
if (name) {
    SDL_Log("Using renderer: %s", name);
}""",
        "remarks": "Returns the name of the backend being used (e.g., 'opengl', 'metal', 'direct3d')",
        "see_also": ["SDL_CreateRenderer", "SDL_GetRenderDriver"]
    }
}
