"""SDL_AppQuit_func datatype definition."""

DATATYPE = {
    "SDL_AppQuit_func": {
        "category": "init",
        "description": "Function pointer typedef for SDL app shutdown",
        "definition": "typedef void (SDLCALL *SDL_AppQuit_func)(void *appstate, SDL_AppResult result);",
        "fields": [
            {"name": "appstate", "type": "void*", "description": "Application state pointer from SDL_AppInit"},
            {"name": "result", "type": "SDL_AppResult", "description": "The result code that caused the app to quit"}
        ],
        "notes": "Part of SDL's optional app interface. Called during shutdown to clean up application state."
    }
}
