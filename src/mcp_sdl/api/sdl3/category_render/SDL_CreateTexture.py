"""SDL_CreateTexture function definition."""

FUNCTION = {
    "SDL_CreateTexture": {
        "category": "render",
        "description": "Create a texture for a rendering context",
        "signature": "SDL_Texture* SDL_CreateTexture(SDL_Renderer *renderer, SDL_PixelFormat format, SDL_TextureAccess access, int w, int h)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "format", "type": "SDL_PixelFormat", "description": "One of the SDL_PixelFormat values"},
            {"name": "access", "type": "SDL_TextureAccess", "description": "One of the SDL_TextureAccess values"},
            {"name": "w", "type": "int", "description": "The width of the texture in pixels"},
            {"name": "h", "type": "int", "description": "The height of the texture in pixels"}
        ],
        "returns": "The created texture or NULL on failure",
        "example": """SDL_Texture *tex = SDL_CreateTexture(renderer,
                                                            SDL_PIXELFORMAT_RGBA8888,
                                                            SDL_TEXTUREACCESS_TARGET,
                                                            640, 480);"""
    }
}
