"""SDL_GetDefaultTextureScaleMode function definition."""

FUNCTION = {
    "SDL_GetDefaultTextureScaleMode": {
        "category": "render",
        "description": "Get the default scale mode used for texture operations",
        "signature": "SDL_ScaleMode SDL_GetDefaultTextureScaleMode(void)",
        "parameters": [],
        "returns": "The current SDL_ScaleMode used for texture operations",
        "example": """SDL_ScaleMode mode = SDL_GetDefaultTextureScaleMode();
if (mode == SDL_SCALEMODE_LINEAR) {
    SDL_Log("Using linear filtering by default");
}""",
        "remarks": "Default is SDL_SCALEMODE_LINEAR, used for new textures unless explicitly set",
        "see_also": ["SDL_SetDefaultTextureScaleMode", "SDL_GetTextureScaleMode", "SDL_SetTextureScaleMode"]
    }
}
