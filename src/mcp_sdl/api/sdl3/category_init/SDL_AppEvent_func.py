"""SDL_AppEvent_func datatype definition."""

DATATYPE = {
    "SDL_AppEvent_func": {
        "category": "init",
        "description": "Function pointer typedef for SDL app event handling",
        "definition": "typedef SDL_AppResult (SDLCALL *SDL_AppEvent_func)(void *appstate, SDL_Event *event);",
        "fields": [
            {"name": "appstate", "type": "void*", "description": "Application state pointer from SDL_AppInit"},
            {"name": "event", "type": "SDL_Event*", "description": "The event to process"}
        ],
        "notes": "Part of SDL's optional app interface. Called for each event. Returns SDL_AppResult to continue or quit."
    }
}
