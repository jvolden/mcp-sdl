"""SDL_UpdateYUVTexture function definition."""

FUNCTION = {
    "SDL_UpdateYUVTexture": {
        "category": "render",
        "description": "Update a rectangle within a planar YUV texture with new pixel data",
        "signature": "bool SDL_UpdateYUVTexture(SDL_Texture *texture, const SDL_Rect *rect, const Uint8 *Yplane, int Ypitch, const Uint8 *Uplane, int Upitch, const Uint8 *Vplane, int Vpitch)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "rect", "type": "const SDL_Rect*", "description": "The area to update, or NULL for the entire texture"},
            {"name": "Yplane", "type": "const Uint8*", "description": "The raw pixel data for the Y plane"},
            {"name": "Ypitch", "type": "int", "description": "The number of bytes between rows in the Y plane"},
            {"name": "Uplane", "type": "const Uint8*", "description": "The raw pixel data for the U plane"},
            {"name": "Upitch", "type": "int", "description": "The number of bytes between rows in the U plane"},
            {"name": "Vplane", "type": "const Uint8*", "description": "The raw pixel data for the V plane"},
            {"name": "Vpitch", "type": "int", "description": "The number of bytes between rows in the V plane"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_UpdateYUVTexture(texture, NULL, y_data, y_pitch, u_data, u_pitch, v_data, v_pitch);""",
        "remarks": "Used for efficient video frame rendering",
        "see_also": ["SDL_UpdateNVTexture", "SDL_UpdateTexture"]
    }
}
