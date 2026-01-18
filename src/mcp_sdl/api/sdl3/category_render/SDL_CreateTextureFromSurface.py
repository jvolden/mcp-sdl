"""SDL_CreateTextureFromSurface function definition."""

FUNCTION = {
    "SDL_CreateTextureFromSurface": {
        "category": "render",
        "description": "Create a texture from an existing surface",
        "signature": "SDL_Texture* SDL_CreateTextureFromSurface(SDL_Renderer *renderer, SDL_Surface *surface)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "surface", "type": "SDL_Surface*", "description": "The surface containing pixel data"}
        ],
        "returns": "The created texture or NULL on failure",
        "example": """SDL_Surface *surface = SDL_LoadBMP("image.bmp");
SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);
SDL_DestroySurface(surface);"""
    }
}
