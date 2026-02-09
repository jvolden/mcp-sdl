"""SDL_GetRenderMetalLayer function definition."""

FUNCTION = {
    "SDL_GetRenderMetalLayer": {
        "category": "render",
        "description": "Get the CAMetalLayer associated with the renderer",
        "signature": "void* SDL_GetRenderMetalLayer(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "A CAMetalLayer on success, or NULL if the renderer isn't Metal",
        "example": """void *layer = SDL_GetRenderMetalLayer(renderer);
if (layer) {
    // Cast to CAMetalLayer and access Metal layer properties
}""",
        "remarks": "[macOS/iOS only] Provides access to underlying Metal layer for advanced rendering",
        "see_also": ["SDL_GetRenderMetalCommandEncoder"]
    }
}
