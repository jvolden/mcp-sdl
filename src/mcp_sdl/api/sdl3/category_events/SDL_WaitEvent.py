"""SDL_WaitEvent function definition."""

FUNCTION = {
    "SDL_WaitEvent": {
        "category": "events",
        "description": "Wait indefinitely for the next available event",
        "signature": "bool SDL_WaitEvent(SDL_Event *event)",
        "parameters": [
            {"name": "event", "type": "SDL_Event*", "description": "The SDL_Event structure to be filled"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_Event event;
SDL_WaitEvent(&event);  // Blocks until event arrives"""
    }
}
