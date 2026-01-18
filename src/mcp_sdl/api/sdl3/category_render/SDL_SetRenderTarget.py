"""SDL_SetRenderTarget function definition."""

FUNCTION = {
    "SDL_SetRenderTarget": {
        "category": "render",
        "description": "Set a texture as the current rendering target",
        "signature": "bool SDL_SetRenderTarget(SDL_Renderer *renderer, SDL_Texture *texture)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "texture", "type": "SDL_Texture*", "description": "The targeted texture, or NULL for the default render target"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Render to texture
SDL_Texture *target = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_RGBA8888,
                                        SDL_TEXTUREACCESS_TARGET, 640, 480);
SDL_SetRenderTarget(renderer, target);
// Draw to the texture...
SDL_RenderClear(renderer);
// Reset to default target
SDL_SetRenderTarget(renderer, NULL);"""
    }
}
