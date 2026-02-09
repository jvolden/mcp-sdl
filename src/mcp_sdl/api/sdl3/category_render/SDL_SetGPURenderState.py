"""SDL_SetGPURenderState function definition."""

FUNCTION = {
    "SDL_SetGPURenderState": {
        "category": "render",
        "description": "Set the current GPU render state",
        "signature": "bool SDL_SetGPURenderState(SDL_Renderer *renderer, SDL_GPURenderState *state)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The GPU renderer"},
            {"name": "state", "type": "SDL_GPURenderState*", "description": "The render state to activate"}
        ],
        "returns": "true on success or false on failure",
        "example": """if (SDL_SetGPURenderState(renderer, state)) {
    SDL_Log("GPU render state activated");
}""",
        "remarks": "Configures graphics pipeline state for subsequent draw calls",
        "see_also": ["SDL_CreateGPURenderState", "SDL_DestroyGPURenderState"]
    }
}
