"""SDL_GetRenderDriver function definition."""

FUNCTION = {
    "SDL_GetRenderDriver": {
        "category": "render",
        "description": "Get the name of a rendering driver",
        "signature": "const char* SDL_GetRenderDriver(int index)",
        "parameters": [
            {"name": "index", "type": "int", "description": "The index of the driver to query"}
        ],
        "returns": "The name of the rendering driver, or NULL if the index is out of range",
        "example": """int num_drivers = SDL_GetNumRenderDrivers();
for (int i = 0; i < num_drivers; i++) {
    const char *name = SDL_GetRenderDriver(i);
    SDL_Log("Render driver %d: %s", i, name);
}""",
        "remarks": "Common drivers include 'direct3d', 'opengl', 'opengles2', 'metal', and 'software'",
        "see_also": ["SDL_GetNumRenderDrivers", "SDL_CreateRenderer", "SDL_GetRendererName"]
    }
}
