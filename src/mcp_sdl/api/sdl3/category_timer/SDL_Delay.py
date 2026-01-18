"""SDL_Delay function definition."""

FUNCTION = {
    "SDL_Delay": {
        "category": "timer",
        "description": "Wait a specified number of milliseconds before returning",
        "signature": "void SDL_Delay(Uint32 ms)",
        "parameters": [
            {"name": "ms", "type": "Uint32", "description": "The number of milliseconds to delay"}
        ],
        "returns": "void",
        "example": """SDL_Delay(1000);  // Wait 1 second"""
    }
}
