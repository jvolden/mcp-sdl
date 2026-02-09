"""SDL_RenderDebugText function definition."""

FUNCTION = {
    "SDL_RenderDebugText": {
        "category": "render",
        "description": "Draw debug text to a renderer",
        "signature": "bool SDL_RenderDebugText(SDL_Renderer *renderer, float x, float y, const char *str)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "x", "type": "float", "description": "The x coordinate"},
            {"name": "y", "type": "float", "description": "The y coordinate"},
            {"name": "str", "type": "const char*", "description": "The text string to draw"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_RenderDebugText(renderer, 10, 10, "FPS: 60");""",
        "remarks": "Simple built-in font for debugging; not suitable for production UI",
        "see_also": ["SDL_RenderDebugTextFormat"]
    }
}
