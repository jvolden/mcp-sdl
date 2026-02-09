"""SDL_SetRenderTextureAddressMode function definition."""

FUNCTION = {
    "SDL_SetRenderTextureAddressMode": {
        "category": "render",
        "description": "Set the texture address mode for texture rendering",
        "signature": "bool SDL_SetRenderTextureAddressMode(SDL_Texture *texture, SDL_TextureAddressMode u_mode, SDL_TextureAddressMode v_mode)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "u_mode", "type": "SDL_TextureAddressMode", "description": "The horizontal address mode"},
            {"name": "v_mode", "type": "SDL_TextureAddressMode", "description": "The vertical address mode"}
        ],
        "returns": "true on success or false on failure",
        "example": """if (SDL_SetRenderTextureAddressMode(texture, SDL_TEXTURE_ADDRESS_WRAP, SDL_TEXTURE_ADDRESS_WRAP)) {
    SDL_Log("Texture wrapping enabled");
}""",
        "remarks": "Use SDL_TEXTURE_ADDRESS_WRAP for tiling, SDL_TEXTURE_ADDRESS_CLAMP to prevent wrapping",
        "see_also": ["SDL_GetRenderTextureAddressMode", "SDL_TextureAddressMode"]
    }
}
