"""SDL_Init function definition."""

FUNCTION = {
    "SDL_Init": {
        "category": "init",
        "description": "Initialize SDL library subsystems",
        "signature": "bool SDL_Init(SDL_InitFlags flags)",
        "parameters": [
            {"name": "flags", "type": "SDL_InitFlags", "description": "Subsystem initialization flags (SDL_INIT_VIDEO, SDL_INIT_AUDIO, etc.)"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Initialize SDL with video and audio subsystems
if (!SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO)) {
    SDL_Log("SDL_Init failed: %s", SDL_GetError());
    return 1;
}"""
    }
}
