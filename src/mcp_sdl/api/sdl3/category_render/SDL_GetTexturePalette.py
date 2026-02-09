"""SDL_GetTexturePalette function definition."""

FUNCTION = {
    "SDL_GetTexturePalette": {
        "category": "render",
        "description": "Get the palette of a paletted texture",
        "signature": "SDL_Palette* SDL_GetTexturePalette(SDL_Texture *texture)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"}
        ],
        "returns": "The palette, or NULL if the texture is not paletted",
        "example": """SDL_Palette *palette = SDL_GetTexturePalette(texture);
if (palette) {
    SDL_Log("Palette has %d colors", palette->ncolors);
}""",
        "remarks": "Only works with paletted pixel formats like SDL_PIXELFORMAT_INDEX8",
        "see_also": ["SDL_SetTexturePalette"]
    }
}
