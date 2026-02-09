"""SDL_SetTexturePalette function definition."""

FUNCTION = {
    "SDL_SetTexturePalette": {
        "category": "render",
        "description": "Set the palette of a paletted texture",
        "signature": "bool SDL_SetTexturePalette(SDL_Texture *texture, SDL_Palette *palette)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to update"},
            {"name": "palette", "type": "SDL_Palette*", "description": "The palette to assign"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_Palette *palette = SDL_CreatePalette(256);
if (SDL_SetTexturePalette(texture, palette)) {
    SDL_Log("Palette updated");
}""",
        "remarks": "Only works with paletted pixel formats; allows palette animation",
        "see_also": ["SDL_GetTexturePalette", "SDL_CreatePalette"]
    }
}
