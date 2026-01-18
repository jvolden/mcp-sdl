"""SDL_GetTextureBlendMode function definition."""

FUNCTION = {
    "SDL_GetTextureBlendMode": {
        "category": "render",
        "description": "Get the blend mode used for texture copy operations",
        "signature": "bool SDL_GetTextureBlendMode(SDL_Texture *texture, SDL_BlendMode *blendMode)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"},
            {"name": "blendMode", "type": "SDL_BlendMode*", "description": "Pointer to store the SDL_BlendMode"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get texture blend mode
SDL_BlendMode blendMode;
SDL_GetTextureBlendMode(texture, &blendMode);"""
    }
}
