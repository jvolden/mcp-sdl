"""SDL_RenderPoints function definition."""

FUNCTION = {
    "SDL_RenderPoints": {
        "category": "render",
        "description": "Draw multiple points on the current rendering target at subpixel precision",
        "signature": "bool SDL_RenderPoints(SDL_Renderer *renderer, const SDL_FPoint *points, int count)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "points", "type": "const SDL_FPoint*", "description": "Array of points to draw"},
            {"name": "count", "type": "int", "description": "Number of points to draw"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Draw multiple points
SDL_FPoint points[] = {
    {10.0f, 10.0f},
    {20.0f, 20.0f},
    {30.0f, 30.0f}
};
SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
SDL_RenderPoints(renderer, points, 3);"""
    }
}
