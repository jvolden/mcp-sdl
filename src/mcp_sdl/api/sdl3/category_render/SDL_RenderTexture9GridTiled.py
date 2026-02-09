"""SDL_RenderTexture9GridTiled function definition."""

FUNCTION = {
    "SDL_RenderTexture9GridTiled": {
        "category": "render",
        "description": "Perform a tiled copy using a 9-grid with the given segment sizes",
        "signature": "bool SDL_RenderTexture9GridTiled(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_Rect *srcrect, float left_width, float right_width, float top_height, float bottom_height, float scale, const SDL_FRect *dstrect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer"},
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to render"},
            {"name": "srcrect", "type": "const SDL_Rect*", "description": "The source rectangle, or NULL for the entire texture"},
            {"name": "left_width", "type": "float", "description": "Width of left corners"},
            {"name": "right_width", "type": "float", "description": "Width of right corners"},
            {"name": "top_height", "type": "float", "description": "Height of top corners"},
            {"name": "bottom_height", "type": "float", "description": "Height of bottom corners"},
            {"name": "scale", "type": "float", "description": "Scale factor for the center"},
            {"name": "dstrect", "type": "const SDL_FRect*", "description": "The destination rectangle"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_FRect dest = {50, 50, 300, 200};
SDL_RenderTexture9GridTiled(renderer, panel_texture, NULL, 8, 8, 8, 8, 1.0f, &dest);""",
        "remarks": "Similar to SDL_RenderTexture9Grid but tiles instead of stretching the center",
        "see_also": ["SDL_RenderTexture9Grid", "SDL_RenderTextureTiled"]
    }
}
