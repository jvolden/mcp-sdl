"""SDL_SetTextureAlphaMod function definition."""

FUNCTION = {
    "SDL_SetTextureAlphaMod": {
        "category": "render",
        "description": "Set an additional alpha value multiplied into render copy operations",
        "signature": "bool SDL_SetTextureAlphaMod(SDL_Texture *texture, Uint8 alpha)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "alpha", "type": "Uint8", "description": "The alpha value multiplied into copy operations"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Set texture to 50% transparency
SDL_SetTextureAlphaMod(texture, 128);"""
    }
}
