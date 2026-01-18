"""SDL_PollEvent function definition."""

FUNCTION = {
    "SDL_PollEvent": {
        "category": "events",
        "description": "Poll for currently pending events",
        "signature": "bool SDL_PollEvent(SDL_Event *event)",
        "parameters": [
            {"name": "event", "type": "SDL_Event*", "description": "The SDL_Event structure to be filled with event data"}
        ],
        "returns": "true if there is a pending event, false otherwise",
        "example": """SDL_Event event;
while (SDL_PollEvent(&event)) {
    if (event.type == SDL_EVENT_QUIT) {
        quit = true;
    }
}"""
    }
}
