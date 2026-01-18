"""SDL_GetMouseState function definition."""

FUNCTION = {
    "SDL_GetMouseState": {
        "category": "mouse",
        "description": "Query SDL's cache for the synchronous mouse button state and the window-relative SDL-cursor position",
        "signature": "SDL_MouseButtonFlags SDL_GetMouseState(float *x, float *y)",
        "parameters": [
            {"name": "x", "type": "float*", "description": "Pointer to receive the SDL-cursor's x-position from the focused window's top left corner, can be NULL if unused"},
            {"name": "y", "type": "float*", "description": "Pointer to receive the SDL-cursor's y-position from the focused window's top left corner, can be NULL if unused"}
        ],
        "returns": "A 32-bit bitmask of the button state that can be bitwise-compared against the SDL_BUTTON_MASK(X) macro",
        "remarks": "This function returns the cached synchronous state as SDL understands it from the last pump of the event queue. To query the platform for immediate asynchronous state, use SDL_GetGlobalMouseState(). In Relative Mode, the SDL-cursor's position usually contradicts the platform-cursor's position.",
        "thread_safety": "This function should only be called on the main thread.",
        "example": """float x, y;
SDL_MouseButtonFlags buttons = SDL_GetMouseState(&x, &y);
if (buttons & SDL_BUTTON_LMASK) {
    // Left button is pressed
}""",
        "see_also": ["SDL_GetGlobalMouseState", "SDL_GetRelativeMouseState"]
    }
}
