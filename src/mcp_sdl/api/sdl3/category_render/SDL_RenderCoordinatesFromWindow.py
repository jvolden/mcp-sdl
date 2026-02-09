"""SDL_RenderCoordinatesFromWindow function definition."""

FUNCTION = {
    "SDL_RenderCoordinatesFromWindow": {
        "category": "render",
        "description": "Get a point in render coordinates when given a point in window coordinates",
        "signature": "bool SDL_RenderCoordinatesFromWindow(SDL_Renderer *renderer, float window_x, float window_y, float *x, float *y)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The renderer"},
            {"name": "window_x", "type": "float", "description": "The x coordinate in window coordinates"},
            {"name": "window_y", "type": "float", "description": "The y coordinate in window coordinates"},
            {"name": "x", "type": "float*", "description": "Pointer filled in with the x coordinate in render coordinates"},
            {"name": "y", "type": "float*", "description": "Pointer filled in with the y coordinate in render coordinates"}
        ],
        "returns": "true on success or false on failure",
        "example": """float render_x, render_y;
if (SDL_RenderCoordinatesFromWindow(renderer, mouse_x, mouse_y, &render_x, &render_y)) {
    SDL_Log("Render coords: %.2f, %.2f", render_x, render_y);
}""",
        "remarks": "Accounts for viewport, logical presentation, and scaling",
        "see_also": ["SDL_RenderCoordinatesToWindow", "SDL_ConvertEventToRenderCoordinates"]
    }
}
