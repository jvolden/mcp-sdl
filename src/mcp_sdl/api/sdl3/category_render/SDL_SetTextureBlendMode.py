"""SDL_SetTextureBlendMode function definition."""

FUNCTION = {
    "SDL_SetTextureBlendMode": {
        "category": "render",
        "description": "Set the blend mode for a texture, used by SDL_RenderTexture()",
        "signature": "bool SDL_SetTextureBlendMode(SDL_Texture *texture, SDL_BlendMode blendMode)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "blendMode", "type": "SDL_BlendMode", "description": "The SDL_BlendMode to use"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Set texture blend mode
SDL_SetTextureBlendMode(texture, SDL_BLENDMODE_BLEND);"""
    }
}
