"""SDL_GetRendererFromTexture function definition."""

FUNCTION = {
    "SDL_GetRendererFromTexture": {
        "category": "render",
        "description": "Get the renderer that created a texture",
        "signature": "SDL_Renderer* SDL_GetRendererFromTexture(SDL_Texture *texture)",
        "parameters": [
            {"name": "texture", "type": "SDL_Texture*", "description": "The texture to query"}
        ],
        "returns": "The rendering context, or NULL on error",
        "example": """SDL_Renderer *renderer = SDL_GetRendererFromTexture(texture);
if (renderer) {
    SDL_Log("Got renderer from texture");
}""",
        "remarks": "Useful when you have a texture but need its associated renderer",
        "see_also": ["SDL_CreateTexture", "SDL_GetRenderer"]
    }
}
