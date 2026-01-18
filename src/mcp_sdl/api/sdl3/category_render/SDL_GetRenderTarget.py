"""SDL_GetRenderTarget function definition."""

FUNCTION = {
    "SDL_GetRenderTarget": {
        "category": "render",
        "description": "Get the current render target",
        "signature": "SDL_Texture* SDL_GetRenderTarget(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "The current render target, or NULL for the default render target",
        "example": """// Get current render target
SDL_Texture *current_target = SDL_GetRenderTarget(renderer);
if (current_target) {
    SDL_Log("Rendering to texture");
} else {
    SDL_Log("Rendering to default target");
}"""
    }
}
