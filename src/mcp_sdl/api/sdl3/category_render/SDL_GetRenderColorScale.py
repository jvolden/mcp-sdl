"""SDL_GetRenderColorScale function definition."""

FUNCTION = {
    "SDL_GetRenderColorScale": {
        "category": "render",
        "description": "Get the color scale used for drawing operations",
        "signature": "bool SDL_GetRenderColorScale(SDL_Renderer *renderer, float *scale)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "scale", "type": "float*", "description": "Pointer filled in with the current color scale value"}
        ],
        "returns": "true on success or false on failure",
        "example": """float scale;
if (SDL_GetRenderColorScale(renderer, &scale)) {
    SDL_Log("Color scale: %.2f", scale);
}""",
        "remarks": "Used for HDR rendering with values >1.0",
        "see_also": ["SDL_SetRenderColorScale"]
    }
}
