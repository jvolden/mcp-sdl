"""SDL_SetDefaultTextureScaleMode function definition."""

FUNCTION = {
    "SDL_SetDefaultTextureScaleMode": {
        "category": "render",
        "description": "Set the default scale mode used for texture operations",
        "signature": "bool SDL_SetDefaultTextureScaleMode(SDL_ScaleMode scaleMode)",
        "parameters": [
            {"name": "scaleMode", "type": "SDL_ScaleMode", "description": "The SDL_ScaleMode to use for texture operations"}
        ],
        "returns": "true on success or false on failure",
        "example": """if (SDL_SetDefaultTextureScaleMode(SDL_SCALEMODE_NEAREST)) {
    SDL_Log("Pixelated rendering enabled");
} else {
    SDL_Log("Failed to set scale mode: %s", SDL_GetError());
}""",
        "remarks": "Affects all subsequently created textures; does not modify existing textures",
        "see_also": ["SDL_GetDefaultTextureScaleMode", "SDL_SetTextureScaleMode"]
    }
}
