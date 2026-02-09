"""SDL_SetRenderColorScale function definition."""

FUNCTION = {
    "SDL_SetRenderColorScale": {
        "category": "render",
        "description": "Set the color scale used for drawing operations",
        "signature": "bool SDL_SetRenderColorScale(SDL_Renderer *renderer, float scale)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "scale", "type": "float", "description": "The color scale value"}
        ],
        "returns": "true on success or false on failure",
        "example": """if (SDL_SetRenderColorScale(renderer, 2.0f)) {
    SDL_Log("HDR color scale enabled");
}""",
        "remarks": "Values >1.0 allow HDR rendering on supported displays",
        "see_also": ["SDL_GetRenderColorScale"]
    }
}
