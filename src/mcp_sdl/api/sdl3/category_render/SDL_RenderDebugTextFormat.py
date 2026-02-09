"""SDL_RenderDebugTextFormat function definition."""

FUNCTION = {
    "SDL_RenderDebugTextFormat": {
        "category": "render",
        "description": "Draw debug text with formatting to a renderer",
        "signature": "bool SDL_RenderDebugTextFormat(SDL_Renderer *renderer, float x, float y, const char *fmt, ...)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "x", "type": "float", "description": "The x coordinate"},
            {"name": "y", "type": "float", "description": "The y coordinate"},
            {"name": "fmt", "type": "const char*", "description": "A printf-style format string"},
            {"name": "...", "type": "...", "description": "Additional arguments for format string"}
        ],
        "returns": "true on success or false on failure",
        "example": """int fps = 60;
SDL_RenderDebugTextFormat(renderer, 10, 10, "FPS: %d", fps);""",
        "remarks": "Convenient for formatted debug output without manual string formatting",
        "see_also": ["SDL_RenderDebugText"]
    }
}
