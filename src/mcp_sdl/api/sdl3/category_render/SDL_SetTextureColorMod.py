"""SDL_SetTextureColorMod function definition."""

FUNCTION = {
    "SDL_SetTextureColorMod": {
        "category": "render",
        "description": "Set an additional color value multiplied into render copy operations",
        "signature": "bool SDL_SetTextureColorMod(SDL_Texture *texture, Uint8 r, Uint8 g, Uint8 b)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "r", "type": "Uint8", "description": "The red color value multiplied into copy operations"},
            {"name": "g", "type": "Uint8", "description": "The green color value multiplied into copy operations"},
            {"name": "b", "type": "Uint8", "description": "The blue color value multiplied into copy operations"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Tint texture red
SDL_SetTextureColorMod(texture, 255, 128, 128);"""
    }
}
