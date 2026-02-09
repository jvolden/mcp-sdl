"""SDL_DestroyGPURenderState function definition."""

FUNCTION = {
    "SDL_DestroyGPURenderState": {
        "category": "render",
        "description": "Destroy a GPU render state object",
        "signature": "void SDL_DestroyGPURenderState(SDL_GPURenderState *state)",
        "parameters": [
            {"name": "state", "type": "SDL_GPURenderState*", "description": "The GPU render state to destroy"}
        ],
        "returns": "No return value",
        "example": """SDL_DestroyGPURenderState(state);""",
        "remarks": "Must be called to free GPU render state resources",
        "see_also": ["SDL_CreateGPURenderState"]
    }
}
