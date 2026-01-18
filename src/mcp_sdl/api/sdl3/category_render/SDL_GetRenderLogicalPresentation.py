"""SDL_GetRenderLogicalPresentation function definition."""

FUNCTION = {
    "SDL_GetRenderLogicalPresentation": {
        "category": "render",
        "description": "Get device independent resolution and presentation mode for rendering",
        "signature": "bool SDL_GetRenderLogicalPresentation(SDL_Renderer *renderer, int *w, int *h, SDL_RendererLogicalPresentation *mode)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "w", "type": "int*", "description": "Pointer to store the width"},
            {"name": "h", "type": "int*", "description": "Pointer to store the height"},
            {"name": "mode", "type": "SDL_RendererLogicalPresentation*", "description": "Pointer to store the presentation mode"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Get logical presentation settings
int w, h;
SDL_RendererLogicalPresentation mode;
SDL_GetRenderLogicalPresentation(renderer, &w, &h, &mode);"""
    }
}
