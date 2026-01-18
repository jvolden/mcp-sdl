"""SDL_RenderClipEnabled function definition."""

FUNCTION = {
    "SDL_RenderClipEnabled": {
        "category": "render",
        "description": "Get whether clipping is enabled on the given renderer",
        "signature": "bool SDL_RenderClipEnabled(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"}
        ],
        "returns": "true if clipping is enabled, false if clipping is disabled",
        "example": """// Check if clipping is enabled
if (SDL_RenderClipEnabled(renderer)) {
    SDL_Log("Clipping is enabled");
}"""
    }
}
