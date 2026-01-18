"""SDL_SetTextureScaleMode function definition."""

FUNCTION = {
    "SDL_SetTextureScaleMode": {
        "category": "render",
        "description": "Set the scale mode used for texture scale operations",
        "signature": "bool SDL_SetTextureScaleMode(SDL_Texture *texture, SDL_ScaleMode scaleMode)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "scaleMode", "type": "SDL_ScaleMode", "description": "The SDL_ScaleMode to use"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Use linear filtering
SDL_SetTextureScaleMode(texture, SDL_SCALEMODE_LINEAR);"""
    }
}
