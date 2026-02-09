"""SDL_SetGPURenderStateFragmentUniforms function definition."""

FUNCTION = {
    "SDL_SetGPURenderStateFragmentUniforms": {
        "category": "render",
        "description": "Set fragment shader uniform data for the current GPU render state",
        "signature": "bool SDL_SetGPURenderStateFragmentUniforms(SDL_Renderer *renderer, const void *data, Uint32 size)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The GPU renderer"},
            {"name": "data", "type": "const void*", "description": "Pointer to uniform data"},
            {"name": "size", "type": "Uint32", "description": "Size of the uniform data in bytes"}
        ],
        "returns": "true on success or false on failure",
        "example": """float time = SDL_GetTicks() / 1000.0f;
SDL_SetGPURenderStateFragmentUniforms(renderer, &time, sizeof(float));""",
        "remarks": "Used to pass custom data to fragment shaders in GPU pipeline",
        "see_also": ["SDL_SetGPURenderState"]
    }
}
