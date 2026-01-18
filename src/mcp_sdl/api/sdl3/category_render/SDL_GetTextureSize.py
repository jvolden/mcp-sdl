"""SDL_GetTextureSize function definition."""

FUNCTION = {
    "SDL_GetTextureSize": {
        "category": "render",
        "description": "Get the width and height of a texture",
        "signature": "bool SDL_GetTextureSize(SDL_Texture *texture, float *w, float *h)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"},
            {"name": "w", "type": "float*", "description": "Pointer to store the width"},
            {"name": "h", "type": "float*", "description": "Pointer to store the height"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get texture size
float w, h;
SDL_GetTextureSize(texture, &w, &h);
SDL_Log("Texture size: %.0fx%.0f", w, h);"""
    }
}
