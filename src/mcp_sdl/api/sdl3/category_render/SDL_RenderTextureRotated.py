"""SDL_RenderTextureRotated function definition."""

FUNCTION = {
    "SDL_RenderTextureRotated": {
        "category": "render",
        "description": "Copy a portion of the texture to the current rendering target with rotation",
        "signature": "bool SDL_RenderTextureRotated(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_Rect *srcrect, const SDL_FRect *dstrect, double angle, const SDL_FPoint *center, SDL_FlipMode flip)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer"},
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to render"},
            {"name": "srcrect", "type": "const SDL_Rect*", "description": "The source rectangle, or NULL for the entire texture"},
            {"name": "dstrect", "type": "const SDL_FRect*", "description": "The destination rectangle, or NULL for the entire rendering target"},
            {"name": "angle", "type": "double", "description": "Angle in degrees, clockwise"},
            {"name": "center", "type": "const SDL_FPoint*", "description": "Point indicating rotation center, or NULL for dstrect center"},
            {"name": "flip", "type": "SDL_FlipMode", "description": "SDL_FLIP_NONE, SDL_FLIP_HORIZONTAL, or SDL_FLIP_VERTICAL"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_FRect dest = {100, 100, 64, 64};
SDL_FPoint center = {32, 32};
SDL_RenderTextureRotated(renderer, texture, NULL, &dest, 45.0, &center, SDL_FLIP_NONE);""",
        "remarks": "Useful for sprite rotation and transformations",
        "see_also": ["SDL_RenderTexture", "SDL_RenderTextureAffine"]
    }
}
