"""SDL_ConvertEventToRenderCoordinates function definition."""

FUNCTION = {
    "SDL_ConvertEventToRenderCoordinates": {
        "category": "render",
        "description": "Convert the coordinates in an event to render coordinates",
        "signature": "bool SDL_ConvertEventToRenderCoordinates(SDL_Renderer *renderer, SDL_Event *event)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer"},
            {"name": "event", "type": "SDL_Event*", "description": "The event to modify"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_Event event;
while (SDL_PollEvent(&event)) {
    SDL_ConvertEventToRenderCoordinates(renderer, &event);
    if (event.type == SDL_EVENT_MOUSE_BUTTON_DOWN) {
        SDL_Log("Click at render coords: %.2f, %.2f", event.button.x, event.button.y);
    }
}""",
        "remarks": "Useful when using logical presentation or viewport settings",
        "see_also": ["SDL_RenderCoordinatesFromWindow", "SDL_RenderCoordinatesToWindow"]
    }
}
