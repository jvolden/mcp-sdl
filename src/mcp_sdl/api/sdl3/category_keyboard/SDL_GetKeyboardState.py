"""SDL_GetKeyboardState function definition."""

FUNCTION = {
    "SDL_GetKeyboardState": {
        "category": "keyboard",
        "description": "Get a snapshot of the current state of the keyboard",
        "signature": "const bool* SDL_GetKeyboardState(int *numkeys)",
        "parameters": [
            {"name": "numkeys", "type": "int*", "description": "If non-NULL, receives the length of the returned array"}
        ],
        "returns": "Pointer to an array of key states",
        "example": """const bool *keys = SDL_GetKeyboardState(NULL);
if (keys[SDL_SCANCODE_SPACE]) {
    // Space key is pressed
}"""
    }
}
