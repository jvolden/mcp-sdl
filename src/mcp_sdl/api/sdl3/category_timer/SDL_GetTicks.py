"""SDL_GetTicks function definition."""

FUNCTION = {
    "SDL_GetTicks": {
        "category": "timer",
        "description": "Get the number of milliseconds since SDL library initialization",
        "signature": "Uint64 SDL_GetTicks(void)",
        "parameters": [],
        "returns": "Number of milliseconds since initialization",
        "example": """Uint64 start = SDL_GetTicks();
// Do something
Uint64 elapsed = SDL_GetTicks() - start;"""
    }
}
