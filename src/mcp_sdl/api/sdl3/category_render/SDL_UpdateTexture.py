"""SDL_UpdateTexture function definition."""

FUNCTION = {
    "SDL_UpdateTexture": {
        "category": "render",
        "description": "Update the given texture rectangle with new pixel data",
        "signature": "bool SDL_UpdateTexture(SDL_Texture *texture, const SDL_Rect *rect, const void *pixels, int pitch)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "rect", "type": "const SDL_Rect*", "description": "The area to update, or NULL to update the entire texture"},
            {"name": "pixels", "type": "const void*", "description": "The raw pixel data in the format of the texture"},
            {"name": "pitch", "type": "int", "description": "The number of bytes in a row of pixel data"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Update entire texture
SDL_UpdateTexture(texture, NULL, pixels, pitch);"""
    }
}
