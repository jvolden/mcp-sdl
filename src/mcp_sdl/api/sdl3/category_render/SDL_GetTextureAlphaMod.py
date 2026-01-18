"""SDL_GetTextureAlphaMod function definition."""

FUNCTION = {
    "SDL_GetTextureAlphaMod": {
        "category": "render",
        "description": "Get the additional alpha value multiplied into render copy operations",
        "signature": "bool SDL_GetTextureAlphaMod(SDL_Texture *texture, Uint8 *alpha)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"},
            {"name": "alpha", "type": "Uint8*", "description": "Pointer to store the alpha value"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get texture alpha mod
Uint8 alpha;
SDL_GetTextureAlphaMod(texture, &alpha);"""
    }
}
