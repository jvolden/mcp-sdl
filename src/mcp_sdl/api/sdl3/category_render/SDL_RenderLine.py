"""SDL_RenderLine function definition."""

FUNCTION = {
    "SDL_RenderLine": {
        "category": "render",
        "description": "Draw a line on the current rendering target at subpixel precision",
        "signature": "bool SDL_RenderLine(SDL_Renderer *renderer, float x1, float y1, float x2, float y2)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "x1", "type": "float", "description": "The x coordinate of the start point"},
            {"name": "y1", "type": "float", "description": "The y coordinate of the start point"},
            {"name": "x2", "type": "float", "description": "The x coordinate of the end point"},
            {"name": "y2", "type": "float", "description": "The y coordinate of the end point"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Draw a line from (0,0) to (100,100)
SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
SDL_RenderLine(renderer, 0.0f, 0.0f, 100.0f, 100.0f);"""
    }
}
