"""SDL_UpdateNVTexture function definition."""

FUNCTION = {
    "SDL_UpdateNVTexture": {
        "category": "render",
        "description": "Update a rectangle within a planar NV12 or NV21 texture with new pixel data",
        "signature": "bool SDL_UpdateNVTexture(SDL_Texture *texture, const SDL_Rect *rect, const Uint8 *Yplane, int Ypitch, const Uint8 *UVplane, int UVpitch)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "rect", "type": "const SDL_Rect*", "description": "The area to update, or NULL for the entire texture"},
            {"name": "Yplane", "type": "const Uint8*", "description": "The raw pixel data for the Y plane"},
            {"name": "Ypitch", "type": "int", "description": "The number of bytes between rows in the Y plane"},
            {"name": "UVplane", "type": "const Uint8*", "description": "The raw pixel data for the UV plane"},
            {"name": "UVpitch", "type": "int", "description": "The number of bytes between rows in the UV plane"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_UpdateNVTexture(texture, NULL, y_data, y_pitch, uv_data, uv_pitch);""",
        "remarks": "Optimized for video playback with hardware decoding",
        "see_also": ["SDL_UpdateYUVTexture", "SDL_UpdateTexture"]
    }
}
