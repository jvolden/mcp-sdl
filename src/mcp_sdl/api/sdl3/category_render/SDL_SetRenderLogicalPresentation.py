"""SDL_SetRenderLogicalPresentation function definition."""

FUNCTION = {
    "SDL_SetRenderLogicalPresentation": {
        "category": "render",
        "description": "Set a device independent resolution and presentation mode for rendering",
        "signature": "bool SDL_SetRenderLogicalPresentation(SDL_Renderer *renderer, int w, int h, SDL_RendererLogicalPresentation mode)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "w", "type": "int", "description": "The width of the logical resolution"},
            {"name": "h", "type": "int", "description": "The height of the logical resolution"},
            {"name": "mode", "type": "SDL_RendererLogicalPresentation", "description": "The presentation mode"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Set logical resolution to 1920x1080
SDL_SetRenderLogicalPresentation(renderer, 1920, 1080, 
                                  SDL_LOGICAL_PRESENTATION_LETTERBOX);"""
    }
}
