"""SDL_GetRendererProperties function definition."""

FUNCTION = {
    "SDL_GetRendererProperties": {
        "category": "render",
        "description": "Get the properties associated with a renderer",
        "signature": "SDL_PropertiesID SDL_GetRendererProperties(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "A valid property ID with the properties of the renderer, or 0 on failure",
        "example": """SDL_PropertiesID props = SDL_GetRendererProperties(renderer);
if (props) {
    const char *name = SDL_GetStringProperty(props, SDL_PROP_RENDERER_NAME_STRING, "unknown");
    SDL_Log("Renderer name: %s", name);
}""",
        "remarks": "Properties include backend name, output size, and other renderer capabilities",
        "see_also": ["SDL_CreateRendererWithProperties", "SDL_GetTextureProperties"]
    }
}
