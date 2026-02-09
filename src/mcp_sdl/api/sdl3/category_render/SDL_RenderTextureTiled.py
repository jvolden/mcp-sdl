"""SDL_RenderTextureTiled function definition."""

FUNCTION = {
    "SDL_RenderTextureTiled": {
        "category": "render",
        "description": "Tile a portion of the texture to the current rendering target",
        "signature": "bool SDL_RenderTextureTiled(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_Rect *srcrect, float scale, const SDL_FRect *dstrect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer"},
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to render"},
            {"name": "srcrect", "type": "const SDL_Rect*", "description": "The source rectangle, or NULL for the entire texture"},
            {"name": "scale", "type": "float", "description": "Scale factor for the tiles"},
            {"name": "dstrect", "type": "const SDL_FRect*", "description": "The destination rectangle, or NULL for the entire rendering target"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_FRect dest = {0, 0, 800, 600};
SDL_RenderTextureTiled(renderer, background_texture, NULL, 1.0f, &dest);""",
        "remarks": "Useful for tiled backgrounds and repeating patterns",
        "see_also": ["SDL_RenderTexture", "SDL_RenderTexture9GridTiled"]
    }
}
