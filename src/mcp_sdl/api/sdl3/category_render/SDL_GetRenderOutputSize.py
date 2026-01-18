"""SDL_GetRenderOutputSize function definition."""

FUNCTION = {
    "SDL_GetRenderOutputSize": {
        "category": "render",
        "description": "Get the output size in pixels of a rendering context",
        "signature": "bool SDL_GetRenderOutputSize(SDL_Renderer *renderer, int *w, int *h)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "w", "type": "int*", "description": "Pointer to store the width in pixels"},
            {"name": "h", "type": "int*", "description": "Pointer to store the height in pixels"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get output size
int w, h;
SDL_GetRenderOutputSize(renderer, &w, &h);
SDL_Log("Output size: %dx%d", w, h);"""
    }
}
