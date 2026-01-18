"""SDL_GetRenderScale function definition."""

FUNCTION = {
    "SDL_GetRenderScale": {
        "category": "render",
        "description": "Get the drawing scale for the current target",
        "signature": "bool SDL_GetRenderScale(SDL_Renderer *renderer, float *scaleX, float *scaleY)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "scaleX", "type": "float*", "description": "Pointer to store the horizontal scaling factor"},
            {"name": "scaleY", "type": "float*", "description": "Pointer to store the vertical scaling factor"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get render scale
float scaleX, scaleY;
SDL_GetRenderScale(renderer, &scaleX, &scaleY);"""
    }
}
