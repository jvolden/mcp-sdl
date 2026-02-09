"""SDL_RenderCoordinatesToWindow function definition."""

FUNCTION = {
    "SDL_RenderCoordinatesToWindow": {
        "category": "render",
        "description": "Get a point in window coordinates when given a point in render coordinates",
        "signature": "bool SDL_RenderCoordinatesToWindow(SDL_Renderer *renderer, float x, float y, float *window_x, float *window_y)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer"},
            {"name": "x", "type": "float", "description": "The x coordinate in render coordinates"},
            {"name": "y", "type": "float", "description": "The y coordinate in render coordinates"},
            {"name": "window_x", "type": "float*", "description": "Pointer filled in with the x coordinate in window coordinates"},
            {"name": "window_y", "type": "float*", "description": "Pointer filled in with the y coordinate in window coordinates"}
        ],
        "returns": "true on success or false on failure",
        "example": """float window_x, window_y;
if (SDL_RenderCoordinatesToWindow(renderer, 100, 100, &window_x, &window_y)) {
    SDL_Log("Window coords: %.2f, %.2f", window_x, window_y);
}""",
        "remarks": "Inverse of SDL_RenderCoordinatesFromWindow",
        "see_also": ["SDL_RenderCoordinatesFromWindow", "SDL_ConvertEventToRenderCoordinates"]
    }
}
