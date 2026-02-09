"""SDL_GetTextureColorModFloat function definition."""

FUNCTION = {
    "SDL_GetTextureColorModFloat": {
        "category": "render",
        "description": "Get the additional color value multiplied into render copy operations as floating point",
        "signature": "bool SDL_GetTextureColorModFloat(SDL_Texture *texture, float *r, float *g, float *b)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"},
            {"name": "r", "type": "float*", "description": "Pointer filled in with the red color value (0.0-1.0)"},
            {"name": "g", "type": "float*", "description": "Pointer filled in with the green color value (0.0-1.0)"},
            {"name": "b", "type": "float*", "description": "Pointer filled in with the blue color value (0.0-1.0)"}
        ],
        "returns": "true on success or false on failure",
        "example": """float r, g, b;
if (SDL_GetTextureColorModFloat(texture, &r, &g, &b)) {
    SDL_Log("Color mod: %.2f, %.2f, %.2f", r, g, b);
}""",
        "remarks": "Float version provides higher precision than byte-based SDL_GetTextureColorMod",
        "see_also": ["SDL_SetTextureColorModFloat", "SDL_GetTextureColorMod"]
    }
}
