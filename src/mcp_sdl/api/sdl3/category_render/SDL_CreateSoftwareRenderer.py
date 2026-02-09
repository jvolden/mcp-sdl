"""SDL_CreateSoftwareRenderer function definition."""

FUNCTION = {
    "SDL_CreateSoftwareRenderer": {
        "category": "render",
        "description": "Create a 2D software rendering context for a surface",
        "signature": "SDL_Renderer* SDL_CreateSoftwareRenderer(SDL_Surface *surface)",
        "parameters": [
            {"name": "surface", "type": "SDL_Surface*", "description": "The surface where rendering is done"}
        ],
        "returns": "A valid rendering context or NULL on failure",
        "example": """SDL_Surface *surface = SDL_CreateSurface(640, 480, SDL_PIXELFORMAT_RGBA32);
SDL_Renderer *renderer = SDL_CreateSoftwareRenderer(surface);
if (renderer) {
    SDL_RenderClear(renderer);
}""",
        "remarks": "Useful for offscreen rendering without window or hardware acceleration",
        "see_also": ["SDL_CreateRenderer", "SDL_DestroyRenderer"]
    }
}
