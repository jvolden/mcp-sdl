"""SDL_GetRenderDrawColorFloat function definition."""

FUNCTION = {
    "SDL_GetRenderDrawColorFloat": {
        "category": "render",
        "description": "Get the color used for drawing operations (Rect, Line, and Clear) as floating point",
        "signature": "bool SDL_GetRenderDrawColorFloat(SDL_Renderer *renderer, float *r, float *g, float *b, float *a)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "r", "type": "float*", "description": "Pointer filled in with the red value (0.0-1.0)"},
            {"name": "g", "type": "float*", "description": "Pointer filled in with the green value (0.0-1.0)"},
            {"name": "b", "type": "float*", "description": "Pointer filled in with the blue value (0.0-1.0)"},
            {"name": "a", "type": "float*", "description": "Pointer filled in with the alpha value (0.0-1.0)"}
        ],
        "returns": "true on success or false on failure",
        "example": """float r, g, b, a;
if (SDL_GetRenderDrawColorFloat(renderer, &r, &g, &b, &a)) {
    SDL_Log("Draw color: %.2f, %.2f, %.2f, %.2f", r, g, b, a);
}""",
        "remarks": "Float version provides higher precision than byte-based SDL_GetRenderDrawColor",
        "see_also": ["SDL_SetRenderDrawColorFloat", "SDL_GetRenderDrawColor"]
    }
}
