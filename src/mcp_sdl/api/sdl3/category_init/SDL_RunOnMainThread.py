"""SDL_RunOnMainThread function definition."""

FUNCTION = {
    "SDL_RunOnMainThread": {
        "category": "init",
        "description": "Call a function on the main thread during event processing",
        "signature": "bool SDL_RunOnMainThread(SDL_MainThreadCallback callback, void *userdata, bool wait_complete)",
        "parameters": [
            {"name": "callback", "type": "SDL_MainThreadCallback", "description": "The callback to call on the main thread"},
            {"name": "userdata", "type": "void*", "description": "A pointer to pass to the callback"},
            {"name": "wait_complete", "type": "bool", "description": "true to wait for the callback to complete, false to return immediately"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Run a function on the main thread
bool my_callback(void *userdata) {
    SDL_Log("Called on main thread");
    return true;
}

SDL_RunOnMainThread(my_callback, NULL, true);"""
    }
}
