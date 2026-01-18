"""SDL_InitSubSystem function definition."""

FUNCTION = {
    "SDL_InitSubSystem": {
        "category": "init",
        "description": "Initialize specific SDL subsystems",
        "signature": "bool SDL_InitSubSystem(SDL_InitFlags flags)",
        "parameters": [
            {"name": "flags", "type": "SDL_InitFlags", "description": "Subsystem initialization flags (SDL_INIT_VIDEO, SDL_INIT_AUDIO, etc.)"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Initialize video subsystem after SDL_Init
if (!SDL_InitSubSystem(SDL_INIT_VIDEO)) {
    SDL_Log("SDL_InitSubSystem failed: %s", SDL_GetError());
    return 1;
}"""
    }
}
