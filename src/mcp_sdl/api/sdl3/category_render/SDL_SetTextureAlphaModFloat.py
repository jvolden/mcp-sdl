"""SDL_SetTextureAlphaModFloat function definition."""

FUNCTION = {
    "SDL_SetTextureAlphaModFloat": {
        "category": "render",
        "description": "Set an additional alpha value multiplied into render copy operations as floating point",
        "signature": "bool SDL_SetTextureAlphaModFloat(SDL_Texture *texture, float alpha)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "alpha", "type": "float", "description": "The alpha value multiplied into copy operations (0.0-1.0)"}
        ],
        "returns": "true on success or false on failure",
        "example": """if (SDL_SetTextureAlphaModFloat(texture, 0.5f)) {
    SDL_RenderTexture(renderer, texture, NULL, NULL);
}""",
        "remarks": "Float version provides higher precision than byte-based SDL_SetTextureAlphaMod",
        "see_also": ["SDL_GetTextureAlphaModFloat", "SDL_SetTextureAlphaMod"]
    }
}
