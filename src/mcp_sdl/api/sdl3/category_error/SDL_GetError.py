"""SDL_GetError function definition."""

FUNCTION = {
    "SDL_GetError": {
        "category": "error",
        "description": "Retrieve the last error message set within SDL",
        "signature": "const char* SDL_GetError(void)",
        "parameters": [],
        "returns": "A pointer to the last error message string",
        "example": """if (!SDL_Init(SDL_INIT_VIDEO)) {
    const char *error = SDL_GetError();
    printf("SDL Error: %s\\n", error);
}"""
    }
}
