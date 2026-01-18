"""SDL_LoadBMP function definition."""

FUNCTION = {
    "SDL_LoadBMP": {
        "category": "surface",
        "description": "Load a BMP image from a file",
        "signature": "SDL_Surface* SDL_LoadBMP(const char *file)",
        "parameters": [
            {"name": "file", "type": "const char*", "description": "The BMP file name to load"}
        ],
        "returns": "The loaded surface or NULL on failure",
        "example": """SDL_Surface *surface = SDL_LoadBMP("image.bmp");
if (!surface) {
    SDL_Log("Failed to load BMP: %s", SDL_GetError());
}"""
    }
}
