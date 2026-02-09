"""SDL_SetTextureColorModFloat function definition."""

FUNCTION = {
    "SDL_SetTextureColorModFloat": {
        "category": "render",
        "description": "Set an additional color value multiplied into render copy operations as floating point",
        "signature": "bool SDL_SetTextureColorModFloat(SDL_Texture *texture, float r, float g, float b)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "r", "type": "float", "description": "The red color value multiplied into copy operations (0.0-1.0)"},
            {"name": "g", "type": "float", "description": "The green color value multiplied into copy operations (0.0-1.0)"},
            {"name": "b", "type": "float", "description": "The blue color value multiplied into copy operations (0.0-1.0)"}
        ],
        "returns": "true on success or false on failure",
        "example": """if (SDL_SetTextureColorModFloat(texture, 1.0f, 0.5f, 0.5f)) {
    SDL_RenderTexture(renderer, texture, NULL, NULL);
}""",
        "remarks": "Float version provides higher precision than byte-based SDL_SetTextureColorMod",
        "see_also": ["SDL_GetTextureColorModFloat", "SDL_SetTextureColorMod"]
    }
}
