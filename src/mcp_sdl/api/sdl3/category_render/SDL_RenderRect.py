"""SDL_RenderRect function definition."""

FUNCTION = {
    "SDL_RenderRect": {
        "category": "render",
        "description": "Draw a rectangle on the current rendering target at subpixel precision",
        "signature": "bool SDL_RenderRect(SDL_Renderer *renderer, const SDL_FRect *rect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rect", "type": "const SDL_FRect*", "description": "Rectangle to draw, or NULL to draw the entire rendering target"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Draw a rectangle outline
SDL_FRect rect = {50.0f, 50.0f, 200.0f, 100.0f};
SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255);
SDL_RenderRect(renderer, &rect);"""
    }
}
