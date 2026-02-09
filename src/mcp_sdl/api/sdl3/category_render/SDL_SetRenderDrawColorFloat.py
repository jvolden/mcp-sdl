"""SDL_SetRenderDrawColorFloat function definition."""

FUNCTION = {
    "SDL_SetRenderDrawColorFloat": {
        "category": "render",
        "description": "Set the color used for drawing operations (Rect, Line, and Clear) as floating point",
        "signature": "bool SDL_SetRenderDrawColorFloat(SDL_Renderer *renderer, float r, float g, float b, float a)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "r", "type": "float", "description": "The red value (0.0-1.0)"},
            {"name": "g", "type": "float", "description": "The green value (0.0-1.0)"},
            {"name": "b", "type": "float", "description": "The blue value (0.0-1.0)"},
            {"name": "a", "type": "float", "description": "The alpha value (0.0-1.0)"}
        ],
        "returns": "true on success or false on failure",
        "example": """if (SDL_SetRenderDrawColorFloat(renderer, 1.0f, 0.5f, 0.0f, 1.0f)) {
    SDL_RenderClear(renderer);
}""",
        "remarks": "Float version provides higher precision than byte-based SDL_SetRenderDrawColor",
        "see_also": ["SDL_GetRenderDrawColorFloat", "SDL_SetRenderDrawColor"]
    }
}
