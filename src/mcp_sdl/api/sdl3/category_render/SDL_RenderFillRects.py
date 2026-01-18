"""SDL_RenderFillRects function definition."""

FUNCTION = {
    "SDL_RenderFillRects": {
        "category": "render",
        "description": "Fill multiple rectangles on the current rendering target with the drawing color at subpixel precision",
        "signature": "bool SDL_RenderFillRects(SDL_Renderer *renderer, const SDL_FRect *rects, int count)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rects", "type": "const SDL_FRect*", "description": "Array of rectangles to fill"},
            {"name": "count", "type": "int", "description": "Number of rectangles"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Fill multiple rectangles
SDL_FRect rects[] = {
    {10.0f, 10.0f, 50.0f, 50.0f},
    {70.0f, 10.0f, 50.0f, 50.0f}
};
SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
SDL_RenderFillRects(renderer, rects, 2);"""
    }
}
