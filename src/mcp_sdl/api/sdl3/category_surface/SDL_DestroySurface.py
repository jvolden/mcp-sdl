"""SDL_DestroySurface function definition."""

FUNCTION = {
    "SDL_DestroySurface": {
        "category": "surface",
        "description": "Free a surface",
        "signature": "void SDL_DestroySurface(SDL_Surface *surface)",
        "parameters": [
            {"name": "surface", "type": "SDL_Surface*", "description": "The surface to free"}
        ],
        "returns": "void",
        "example": """SDL_DestroySurface(surface);"""
    }
}
