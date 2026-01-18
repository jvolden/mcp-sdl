"""SDL_GetTextureScaleMode function definition."""

FUNCTION = {
    "SDL_GetTextureScaleMode": {
        "category": "render",
        "description": "Get the scale mode used for texture scale operations",
        "signature": "bool SDL_GetTextureScaleMode(SDL_Texture *texture, SDL_ScaleMode *scaleMode)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"},
            {"name": "scaleMode", "type": "SDL_ScaleMode*", "description": "Pointer to store the SDL_ScaleMode"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get texture scale mode
SDL_ScaleMode scaleMode;
SDL_GetTextureScaleMode(texture, &scaleMode);"""
    }
}
