"""SDL_AppInit_func datatype definition."""

DATATYPE = {
    "SDL_AppInit_func": {
        "category": "init",
        "description": "Function pointer typedef for SDL app initialization",
        "definition": "typedef SDL_AppResult (SDLCALL *SDL_AppInit_func)(void **appstate, int argc, char *argv[]);",
        "fields": [
            {"name": "appstate", "type": "void**", "description": "Pointer to store application state"},
            {"name": "argc", "type": "int", "description": "Number of command line arguments"},
            {"name": "argv", "type": "char*[]", "description": "Command line argument strings"}
        ],
        "notes": "Part of SDL's optional app interface. Returns SDL_AppResult indicating success/failure."
    }
}
