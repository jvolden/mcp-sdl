"""SDL_CreateGPURenderState function definition."""

FUNCTION = {
    "SDL_CreateGPURenderState": {
        "category": "render",
        "description": "Create a GPU render state object",
        "signature": "SDL_GPURenderState* SDL_CreateGPURenderState(SDL_Renderer *renderer, const SDL_GPURenderStateCreateInfo *createinfo)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The GPU renderer"},
            {"name": "createinfo", "type": "const SDL_GPURenderStateCreateInfo*", "description": "Description of the render state to create"}
        ],
        "returns": "A valid GPU render state object or NULL on failure",
        "example": """SDL_GPURenderStateCreateInfo info = {0};
SDL_GPURenderState *state = SDL_CreateGPURenderState(renderer, &info);
if (!state) {
    SDL_Log("Failed to create GPU render state: %s", SDL_GetError());
}""",
        "remarks": "Part of SDL3's GPU API for configuring graphics pipeline state",
        "see_also": ["SDL_DestroyGPURenderState", "SDL_SetGPURenderState"]
    }
}
