"""SDL_LockTexture function definition."""

FUNCTION = {
    "SDL_LockTexture": {
        "category": "render",
        "description": "Lock a portion of the texture for write-only pixel access",
        "signature": "bool SDL_LockTexture(SDL_Texture *texture, const SDL_Rect *rect, void **pixels, int *pitch)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to lock"},
            {"name": "rect", "type": "const SDL_Rect*", "description": "The area to lock, or NULL to lock the entire texture"},
            {"name": "pixels", "type": "void**", "description": "Pointer to be filled with a pointer to the locked pixels"},
            {"name": "pitch", "type": "int*", "description": "Pointer to be filled with the pitch of the locked pixels"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Lock and modify texture pixels
void *pixels;
int pitch;
if (SDL_LockTexture(texture, NULL, &pixels, &pitch)) {
    // Modify pixels...
    SDL_UnlockTexture(texture);
}"""
    }
}
