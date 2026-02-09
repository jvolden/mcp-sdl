"""SDL_RenderTextureAffine function definition."""

FUNCTION = {
    "SDL_RenderTextureAffine": {
        "category": "render",
        "description": "Copy a portion of the texture to the current rendering target using an affine transformation",
        "signature": "bool SDL_RenderTextureAffine(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_Rect *srcrect, const SDL_FPoint *origin, const SDL_FPoint *right, const SDL_FPoint *down)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer"},
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to render"},
            {"name": "srcrect", "type": "const SDL_Rect*", "description": "The source rectangle, or NULL for the entire texture"},
            {"name": "origin", "type": "const SDL_FPoint*", "description": "The origin point for the transformation"},
            {"name": "right", "type": "const SDL_FPoint*", "description": "The right vector"},
            {"name": "down", "type": "const SDL_FPoint*", "description": "The down vector"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_FPoint origin = {100, 100};
SDL_FPoint right = {200, 150};
SDL_FPoint down = {50, 200};
SDL_RenderTextureAffine(renderer, texture, NULL, &origin, &right, &down);""",
        "remarks": "Allows arbitrary 2D transformations including shearing and skewing",
        "see_also": ["SDL_RenderTextureRotated", "SDL_RenderTexture"]
    }
}
