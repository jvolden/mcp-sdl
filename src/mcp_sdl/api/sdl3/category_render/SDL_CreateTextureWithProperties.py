"""SDL_CreateTextureWithProperties function definition."""

FUNCTION = {
    "SDL_CreateTextureWithProperties": {
        "category": "render",
        "description": "Create a texture with specified properties",
        "signature": "SDL_Texture* SDL_CreateTextureWithProperties(SDL_Renderer *renderer, SDL_PropertiesID props)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "props", "type": "SDL_PropertiesID", "description": "The properties to use for the texture"}
        ],
        "returns": "A valid texture or NULL on failure",
        "example": """SDL_PropertiesID props = SDL_CreateProperties();
SDL_SetNumberProperty(props, SDL_PROP_TEXTURE_CREATE_FORMAT_NUMBER, SDL_PIXELFORMAT_RGBA32);
SDL_SetNumberProperty(props, SDL_PROP_TEXTURE_CREATE_WIDTH_NUMBER, 640);
SDL_SetNumberProperty(props, SDL_PROP_TEXTURE_CREATE_HEIGHT_NUMBER, 480);
SDL_Texture *texture = SDL_CreateTextureWithProperties(renderer, props);
SDL_DestroyProperties(props);""",
        "remarks": "Allows fine-grained control over texture creation using property system",
        "see_also": ["SDL_CreateTexture", "SDL_DestroyTexture", "SDL_GetTextureProperties"]
    }
}
