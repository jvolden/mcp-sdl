"""SDL_RenderPoint function definition."""

FUNCTION = {
    "SDL_RenderPoint": {
        "category": "render",
        "description": "Draw a point on the current rendering target at subpixel precision",
        "signature": "bool SDL_RenderPoint(SDL_Renderer *renderer, float x, float y)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "x", "type": "float", "description": "The x coordinate of the point"},
            {"name": "y", "type": "float", "description": "The y coordinate of the point"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Draw a single point
SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
SDL_RenderPoint(renderer, 100.0f, 100.0f);"""
    }
}
