"""SDL_GetNumRenderDrivers function definition."""

FUNCTION = {
    "SDL_GetNumRenderDrivers": {
        "category": "render",
        "description": "Get the number of 2D rendering drivers available for the current display",
        "signature": "int SDL_GetNumRenderDrivers(void)",
        "parameters": [],
        "returns": "The number of rendering drivers available or -1 on failure",
        "example": """int num_drivers = SDL_GetNumRenderDrivers();
SDL_Log("Available rendering drivers: %d", num_drivers);
for (int i = 0; i < num_drivers; i++) {
    const char *name = SDL_GetRenderDriver(i);
    SDL_Log("  Driver %d: %s", i, name);
}""",
        "see_also": ["SDL_GetRenderDriver", "SDL_CreateRenderer"]
    }
}
