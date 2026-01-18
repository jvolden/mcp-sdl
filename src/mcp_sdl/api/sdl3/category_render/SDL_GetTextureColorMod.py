"""SDL_GetTextureColorMod function definition."""

FUNCTION = {
    "SDL_GetTextureColorMod": {
        "category": "render",
        "description": "Get the additional color value multiplied into render copy operations",
        "signature": "bool SDL_GetTextureColorMod(SDL_Texture *texture, Uint8 *r, Uint8 *g, Uint8 *b)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"},
            {"name": "r", "type": "Uint8*", "description": "Pointer to store the red color value"},
            {"name": "g", "type": "Uint8*", "description": "Pointer to store the green color value"},
            {"name": "b", "type": "Uint8*", "description": "Pointer to store the blue color value"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get texture color mod
Uint8 r, g, b;
SDL_GetTextureColorMod(texture, &r, &g, &b);"""
    }
}
