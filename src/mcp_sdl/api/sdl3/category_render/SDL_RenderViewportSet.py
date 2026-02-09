"""SDL_RenderViewportSet function definition."""

FUNCTION = {
    "SDL_RenderViewportSet": {
        "category": "render",
        "description": "Check if a viewport is set on a renderer",
        "signature": "bool SDL_RenderViewportSet(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "true if a viewport is set, false otherwise",
        "example": """if (SDL_RenderViewportSet(renderer)) {
    SDL_Log("Custom viewport is active");
} else {
    SDL_Log("Using full render target");
}""",
        "remarks": "Returns false when viewport is NULL (rendering to entire target)",
        "see_also": ["SDL_SetRenderViewport", "SDL_GetRenderViewport"]
    }
}
