"""SDL_GetRenderDrawColor function definition."""

FUNCTION = {
    "SDL_GetRenderDrawColor": {
        "category": "render",
        "description": "Get the color used for drawing operations",
        "signature": "bool SDL_GetRenderDrawColor(SDL_Renderer *renderer, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "r", "type": "Uint8*", "description": "Pointer to store the red value"},
            {"name": "g", "type": "Uint8*", "description": "Pointer to store the green value"},
            {"name": "b", "type": "Uint8*", "description": "Pointer to store the blue value"},
            {"name": "a", "type": "Uint8*", "description": "Pointer to store the alpha value"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get current draw color
Uint8 r, g, b, a;
SDL_GetRenderDrawColor(renderer, &r, &g, &b, &a);
SDL_Log("Draw color: %d,%d,%d,%d", r, g, b, a);"""
    }
}
