"""SDL_RenderTexture9Grid function definition."""

FUNCTION = {
    "SDL_RenderTexture9Grid": {
        "category": "render",
        "description": "Perform a scaled copy using a 9-grid with the given segment sizes",
        "signature": "bool SDL_RenderTexture9Grid(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_Rect *srcrect, float left_width, float right_width, float top_height, float bottom_height, float scale, const SDL_FRect *dstrect)",
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
SDL_RenderTexture9Grid(renderer, button_texture, NULL, 10, 10, 10, 10, 1.0f, &dest);""",
        "remarks": "9-grid allows UI elements to scale without distorting corners",
        "see_also": ["SDL_RenderTexture9GridTiled", "SDL_RenderTexture"]
    }
}
