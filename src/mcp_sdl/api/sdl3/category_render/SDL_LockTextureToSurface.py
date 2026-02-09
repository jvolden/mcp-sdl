"""SDL_LockTextureToSurface function definition."""

FUNCTION = {
    "SDL_LockTextureToSurface": {
        "category": "render",
        "description": "Lock a portion of the texture for write-only pixel access, and expose it as an SDL surface",
        "signature": "bool SDL_LockTextureToSurface(SDL_Texture *texture, const SDL_Rect *rect, SDL_Surface **surface)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to lock"},
            {"name": "rect", "type": "const SDL_Rect*", "description": "The rectangle to lock, or NULL for the entire texture"},
            {"name": "surface", "type": "SDL_Surface**", "description": "Pointer filled with an SDL surface representing the locked area"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_Surface *surface;
if (SDL_LockTextureToSurface(texture, NULL, &surface)) {
    // Modify surface->pixels
    SDL_UnlockTexture(texture);
}""",
        "remarks": "Must call SDL_UnlockTexture() when done; only for SDL_TEXTUREACCESS_STREAMING",
        "see_also": ["SDL_LockTexture", "SDL_UnlockTexture"]
    }
}
