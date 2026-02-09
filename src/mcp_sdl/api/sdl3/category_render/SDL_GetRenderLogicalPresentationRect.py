"""SDL_GetRenderLogicalPresentationRect function definition."""

FUNCTION = {
    "SDL_GetRenderLogicalPresentationRect": {
        "category": "render",
        "description": "Get the final presentation rectangle for rendering",
        "signature": "bool SDL_GetRenderLogicalPresentationRect(SDL_Renderer *renderer, SDL_FRect *rect)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "rect", "type": "SDL_FRect*", "description": "Pointer filled in with the presentation rectangle"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_FRect rect;
if (SDL_GetRenderLogicalPresentationRect(renderer, &rect)) {
    SDL_Log("Presentation rect: %.2f,%.2f %.2fx%.2f", rect.x, rect.y, rect.w, rect.h);
}""",
        "remarks": "Shows where logical rendering will be displayed in output coordinates",
        "see_also": ["SDL_SetRenderLogicalPresentation", "SDL_GetRenderLogicalPresentation"]
    }
}
