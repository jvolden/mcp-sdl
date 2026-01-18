"""SDL_RendererLogicalPresentation enum definition."""

ENUM = {
    "SDL_RendererLogicalPresentation": {
        "description": "How the logical size is mapped to the output",
        "values": [
            {"name": "SDL_LOGICAL_PRESENTATION_DISABLED", "description": "No logical size"},
            {"name": "SDL_LOGICAL_PRESENTATION_STRETCH", "description": "Stretch to fill the output"},
            {"name": "SDL_LOGICAL_PRESENTATION_LETTERBOX", "description": "Letterbox to fit in output"},
            {"name": "SDL_LOGICAL_PRESENTATION_OVERSCAN", "description": "Overscan to fill output"},
            {"name": "SDL_LOGICAL_PRESENTATION_INTEGER_SCALE", "description": "Scale to integer multiples"}
        ]
    }
}
