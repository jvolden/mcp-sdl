"""SDL_SetRenderDrawColor function definition."""

FUNCTION = {
    "SDL_SetRenderDrawColor": {
        "category": "render",
        "description": "Set the color used for drawing operations",
        "signature": "bool SDL_SetRenderDrawColor(SDL_Renderer *renderer, Uint8 r, Uint8 g, Uint8 b, Uint8 a)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "r", "type": "Uint8", "description": "The red value (0-255)"},
            {"name": "g", "type": "Uint8", "description": "The green value (0-255)"},
            {"name": "b", "type": "Uint8", "description": "The blue value (0-255)"},
            {"name": "a", "type": "Uint8", "description": "The alpha value (0-255)"}
        ],
        "returns": "true on success or false on failure",
        "example": """// Set draw color to white
SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);"""
    }
}
