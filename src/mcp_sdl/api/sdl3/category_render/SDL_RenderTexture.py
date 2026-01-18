"""SDL_RenderTexture function definition."""

FUNCTION = {
    "SDL_RenderTexture": {
        "category": "render",
        "description": "Copy a portion of the texture to the current rendering target",
        "signature": "bool SDL_RenderTexture(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_FRect *srcrect, const SDL_FRect *dstrect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "texture", "type": "SDL_Texture*", "description": "The source texture"},
            {"name": "srcrect", "type": "const SDL_FRect*", "description": "The source rectangle, or NULL for the entire texture"},
            {"name": "dstrect", "type": "const SDL_FRect*", "description": "The destination rectangle, or NULL for the entire rendering target"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_RenderTexture(renderer, texture, NULL, NULL);  // Draw entire texture"""
    }
}
