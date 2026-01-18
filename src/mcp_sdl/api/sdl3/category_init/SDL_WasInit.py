"""SDL_WasInit function definition."""

FUNCTION = {
    "SDL_WasInit": {
        "category": "init",
        "description": "Get a mask of the specified subsystems which are currently initialized",
        "signature": "SDL_InitFlags SDL_WasInit(SDL_InitFlags flags)",
        "parameters": [
            {"name": "flags", "type": "SDL_InitFlags", "description": "Subsystem mask to query, or 0 to query all subsystems"}
        ],
        "returns": "A mask of all initialized subsystems if flags is 0, otherwise a mask of specified subsystems that are initialized",
        "example": """// Check if video subsystem is initialized
if (SDL_WasInit(SDL_INIT_VIDEO)) {
    SDL_Log("Video subsystem is initialized");
}

// Get all initialized subsystems
SDL_InitFlags initialized = SDL_WasInit(0);"""
    }
}
