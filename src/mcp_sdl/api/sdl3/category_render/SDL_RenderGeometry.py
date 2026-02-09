"""SDL_RenderGeometry function definition."""

FUNCTION = {
    "SDL_RenderGeometry": {
        "category": "render",
        "description": "Render a list of triangles with optional texture and color per vertex",
        "signature": "bool SDL_RenderGeometry(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_Vertex *vertices, int num_vertices, const int *indices, int num_indices)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "texture", "type": "SDL_Texture*", "description": "The SDL texture to use, or NULL for solid color"},
            {"name": "vertices", "type": "const SDL_Vertex*", "description": "Vertices to render"},
            {"name": "num_vertices", "type": "int", "description": "Number of vertices"},
            {"name": "indices", "type": "const int*", "description": "An array of indices into vertices, or NULL for direct order"},
            {"name": "num_indices", "type": "int", "description": "Number of indices"}
        ],
        "returns": "true on success or false on failure",
        "example": """SDL_Vertex vertices[3] = {
    {{100, 100}, {255, 0, 0, 255}, {0, 0}},
    {{200, 300}, {0, 255, 0, 255}, {1, 0}},
    {{300, 100}, {0, 0, 255, 255}, {1, 1}}
};
SDL_RenderGeometry(renderer, NULL, vertices, 3, NULL, 0);""",
        "remarks": "Useful for 2D polygon rendering and custom geometry",
        "see_also": ["SDL_RenderGeometryRaw", "SDL_Vertex"]
    }
}
