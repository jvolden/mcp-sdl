"""SDL_QuitSubSystem function definition."""

FUNCTION = {
    "SDL_QuitSubSystem": {
        "category": "init",
        "description": "Shut down specific SDL subsystems",
        "signature": "void SDL_QuitSubSystem(SDL_InitFlags flags)",
        "parameters": [
            {"name": "flags", "type": "SDL_InitFlags", "description": "Subsystem flags to shut down"}
        ],
        "returns": "Nothing",
        "example": """// Quit audio subsystem
SDL_QuitSubSystem(SDL_INIT_AUDIO);"""
    }
}
