"""SDL_GetTextureAlphaModFloat function definition."""

FUNCTION = {
    "SDL_GetTextureAlphaModFloat": {
        "category": "render",
        "description": "Get the additional alpha value multiplied into render copy operations as floating point",
        "signature": "bool SDL_GetTextureAlphaModFloat(SDL_Texture *texture, float *alpha)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"},
            {"name": "alpha", "type": "float*", "description": "Pointer filled in with the current alpha value (0.0-1.0)"}
        ],
        "returns": "true on success or false on failure",
        "example": """float alpha;
if (SDL_GetTextureAlphaModFloat(texture, &alpha)) {
    SDL_Log("Texture alpha: %.2f", alpha);
}""",
        "remarks": "Float version provides higher precision than byte-based SDL_GetTextureAlphaMod",
        "see_also": ["SDL_SetTextureAlphaModFloat", "SDL_GetTextureAlphaMod"]
    }
}
