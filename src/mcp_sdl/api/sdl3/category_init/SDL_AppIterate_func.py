"""SDL_AppIterate_func datatype definition."""

DATATYPE = {
    "SDL_AppIterate_func": {
        "category": "init",
        "description": "Function pointer typedef for SDL app main loop iteration",
        "definition": "typedef SDL_AppResult (SDLCALL *SDL_AppIterate_func)(void *appstate);",
        "fields": [
            {"name": "appstate", "type": "void*", "description": "Application state pointer from SDL_AppInit"}
        ],
        "notes": "Part of SDL's optional app interface. Called each frame. Returns SDL_AppResult to continue or quit."
    }
}
