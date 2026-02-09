"""SDL_GetRenderTextureAddressMode function definition."""

FUNCTION = {
    "SDL_GetRenderTextureAddressMode": {
        "category": "render",
        "description": "Get the texture address mode for texture rendering",
        "signature": "bool SDL_GetRenderTextureAddressMode(SDL_Texture *texture, SDL_TextureAddressMode *u_mode, SDL_TextureAddressMode *v_mode)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"},
            {"name": "u_mode", "type": "SDL_TextureAddressMode*", "description": "Pointer filled in with the horizontal address mode"},
            {"name": "v_mode", "type": "SDL_TextureAddressMode*", "description": "Pointer filled in with the vertical address mode"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_TextureAddressMode u_mode, v_mode;
if (SDL_GetRenderTextureAddressMode(texture, &u_mode, &v_mode)) {
    SDL_Log("Address mode: %d, %d", u_mode, v_mode);
}""",
        "remarks": "Controls wrap/clamp behavior when texture coordinates are outside [0,1]",
        "see_also": ["SDL_SetRenderTextureAddressMode", "SDL_TextureAddressMode"]
    }
}
