"""SDL_RenderLines function definition."""

FUNCTION = {
    "SDL_RenderLines": {
        "category": "render",
        "description": "Draw a series of connected lines on the current rendering target at subpixel precision",
        "signature": "bool SDL_RenderLines(SDL_Renderer *renderer, const SDL_FPoint *points, int count)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "points", "type": "const SDL_FPoint*", "description": "Array of points for connected lines"},
            {"name": "count", "type": "int", "description": "Number of points (count-1 lines will be drawn)"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Draw connected lines forming a triangle
SDL_FPoint points[] = {
    {100.0f, 100.0f},
    {200.0f, 100.0f},
    {150.0f, 200.0f},
    {100.0f, 100.0f}  // Close the triangle
};
SDL_SetRenderDrawColor(renderer, 255, 255, 0, 255);
SDL_RenderLines(renderer, points, 4);"""
    }
}
