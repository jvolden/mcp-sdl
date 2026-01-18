"""SDL_RenderRects function definition."""

FUNCTION = {
    "SDL_RenderRects": {
        "category": "render",
        "description": "Draw multiple rectangles on the current rendering target at subpixel precision",
        "signature": "bool SDL_RenderRects(SDL_Renderer *renderer, const SDL_FRect *rects, int count)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rects", "type": "const SDL_FRect*", "description": "Array of rectangles to draw"},
            {"name": "count", "type": "int", "description": "Number of rectangles"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Draw multiple rectangle outlines
SDL_FRect rects[] = {
    {10.0f, 10.0f, 50.0f, 50.0f},
    {70.0f, 10.0f, 50.0f, 50.0f},
    {130.0f, 10.0f, 50.0f, 50.0f}
};
SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255);
SDL_RenderRects(renderer, rects, 3);"""
    }
}
