"""SDL_GetTextureProperties function definition."""

FUNCTION = {
    "SDL_GetTextureProperties": {
        "category": "render",
        "description": "Get the properties associated with a texture",
        "signature": "SDL_PropertiesID SDL_GetTextureProperties(SDL_Texture *texture)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"}
        ],
        "returns": "A valid property ID with the properties of the texture, or 0 on failure",
        "example": """SDL_PropertiesID props = SDL_GetTextureProperties(texture);
if (props) {
    int format = SDL_GetNumberProperty(props, SDL_PROP_TEXTURE_FORMAT_NUMBER, SDL_PIXELFORMAT_UNKNOWN);
    SDL_Log("Texture format: 0x%08x", format);
}""",
        "remarks": "Properties include format, access, width, height, and backend-specific data",
        "see_also": ["SDL_CreateTextureWithProperties", "SDL_GetRendererProperties"]
    }
}
