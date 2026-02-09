"""SDL_RenderReadPixels function definition."""

FUNCTION = {
    "SDL_RenderReadPixels": {
        "category": "render",
        "description": "Read pixels from the current rendering target",
        "signature": "bool SDL_RenderReadPixels(SDL_Renderer *renderer, const SDL_Rect *rect, SDL_PixelFormat format, void *pixels, int pitch)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rect", "type": "const SDL_Rect*", "description": "The area to read, or NULL for the entire render target"},
            {"name": "format", "type": "SDL_PixelFormat", "description": "Desired format of the pixel data, or SDL_PIXELFORMAT_UNKNOWN to use native format"},
            {"name": "pixels", "type": "void*", "description": "Pointer to the pixel data buffer"},
            {"name": "pitch", "type": "int", "description": "Number of bytes in a row of pixel data"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_Rect rect = {0, 0, 640, 480};
void *pixels = malloc(640 * 480 * 4);
if (SDL_RenderReadPixels(renderer, &rect, SDL_PIXELFORMAT_RGBA32, pixels, 640 * 4)) {
    SDL_Log("Screenshot captured");
}""",
        "remarks": "Slow operation, avoid calling every frame",
        "see_also": ["SDL_RenderPresent", "SDL_CreateTexture"]
    }
}
