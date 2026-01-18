"""SDL_UnlockTexture function definition."""

FUNCTION = {
    "SDL_UnlockTexture": {
        "category": "render",
        "description": "Unlock a texture, uploading the changes to video memory, if needed",
        "signature": "void SDL_UnlockTexture(SDL_Texture *texture)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to unlock"}
        ],
        "returns": "Nothing",
        "example": """// Unlock texture after modification
SDL_UnlockTexture(texture);"""
    }
}
