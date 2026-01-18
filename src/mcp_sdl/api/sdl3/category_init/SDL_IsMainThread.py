"""SDL_IsMainThread function definition."""

FUNCTION = {
    "SDL_IsMainThread": {
        "category": "init",
        "description": "Return whether this is the main thread",
        "signature": "bool SDL_IsMainThread(void)",
        "parameters": [],
        "returns": "true if this is the main thread, false otherwise",
        "example": """// Check if running on main thread
if (SDL_IsMainThread()) {
    SDL_Log("Running on main thread");
} else {
    SDL_Log("Running on background thread");
}"""
    }
}
