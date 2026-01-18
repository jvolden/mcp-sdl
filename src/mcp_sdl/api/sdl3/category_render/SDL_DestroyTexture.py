"""SDL_DestroyTexture function definition."""

FUNCTION = {
    "SDL_DestroyTexture": {
        "category": "render",
        "description": "Destroy the specified texture",
        "signature": "void SDL_DestroyTexture(SDL_Texture *texture)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to destroy"}
        ],
        "returns": "void",
        "example": """SDL_DestroyTexture(texture);"""
    }
}
