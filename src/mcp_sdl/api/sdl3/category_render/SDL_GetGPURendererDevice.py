"""SDL_GetGPURendererDevice function definition."""

FUNCTION = {
    "SDL_GetGPURendererDevice": {
        "category": "render",
        "description": "Get the GPU device associated with a renderer",
        "signature": "SDL_GPUDevice* SDL_GetGPURendererDevice(SDL_Renderer *renderer)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The GPU renderer"}
        ],
        "returns": "The GPU device, or NULL if the renderer is not a GPU renderer",
        "example": """SDL_GPUDevice *device = SDL_GetGPURendererDevice(renderer);
if (device) {
    SDL_Log("Got GPU device from renderer");
}""",
        "remarks": "Allows direct access to GPU API for advanced rendering",
        "see_also": ["SDL_CreateGPURenderer"]
    }
}
