"""SDL_GetRenderMetalCommandEncoder function definition."""

FUNCTION = {
    "SDL_GetRenderMetalCommandEncoder": {
        "category": "render",
        "description": "Get the Metal command encoder for the current render pass",
        "signature": "void* SDL_GetRenderMetalCommandEncoder(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "An id<MTLRenderCommandEncoder> on success, or NULL if the renderer isn't Metal",
        "example": """void *encoder = SDL_GetRenderMetalCommandEncoder(renderer);
if (encoder) {
    // Cast to id<MTLRenderCommandEncoder> and use Metal API
}""",
        "remarks": "[macOS/iOS only] Allows direct Metal API calls within SDL rendering",
        "thread_safety": "Must be called from the main thread",
        "see_also": ["SDL_GetRenderMetalLayer"]
    }
}
