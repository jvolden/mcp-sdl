"""SDL_RenderFillRect function definition."""

FUNCTION = {
    "SDL_RenderFillRect": {
        "category": "render",
        "description": "Fill a rectangle on the current rendering target with the drawing color",
        "signature": "bool SDL_RenderFillRect(SDL_Renderer *renderer, const SDL_FRect *rect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rect", "type": "const SDL_FRect*", "description": "The rectangle to fill, or NULL for the entire target"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_FRect rect = {100, 100, 200, 150};
SDL_RenderFillRect(renderer, &rect);"""
    }
}
