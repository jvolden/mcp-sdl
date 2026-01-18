"""SDL_MainThreadCallback datatype definition."""

DATATYPE = {
    "SDL_MainThreadCallback": {
        "category": "init",
        "description": "A callback to be invoked on the main thread",
        "definition": "typedef bool (SDLCALL *SDL_MainThreadCallback)(void *userdata);",
        "fields": [
            {"name": "userdata", "type": "void*", "description": "User data pointer passed to the callback"}
        ],
        "notes": "Returns true on success, false on failure. Used with SDL_RunOnMainThread()."
    }
}
