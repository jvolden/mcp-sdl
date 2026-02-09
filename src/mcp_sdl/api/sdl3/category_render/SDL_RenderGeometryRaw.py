"""SDL_RenderGeometryRaw function definition."""

FUNCTION = {
    "SDL_RenderGeometryRaw": {
        "category": "render",
        "description": "Render a list of triangles using raw float arrays for positions, colors, and texture coordinates",
        "signature": "bool SDL_RenderGeometryRaw(SDL_Renderer *renderer, SDL_Texture *texture, const float *xy, int xy_stride, const SDL_FColor *color, int color_stride, const float *uv, int uv_stride, int num_vertices, const void *indices, int num_indices, int size_indices)",
        "parameters": [
            {"name": "renderer", "type": "SDL_Renderer*", "description": "The rendering context"},
            {"name": "texture", "type": "SDL_Texture*", "description": "The SDL texture to use, or NULL"},
            {"name": "xy", "type": "const float*", "description": "Vertex positions as (x, y) pairs"},
            {"name": "xy_stride", "type": "int", "description": "Byte size between consecutive positions"},
            {"name": "color", "type": "const SDL_FColor*", "description": "Vertex colors"},
            {"name": "color_stride", "type": "int", "description": "Byte size between consecutive colors"},
            {"name": "uv", "type": "const float*", "description": "Vertex texture coordinates as (u, v) pairs"},
            {"name": "uv_stride", "type": "int", "description": "Byte size between consecutive UVs"},
            {"name": "num_vertices", "type": "int", "description": "Number of vertices"},
            {"name": "indices", "type": "const void*", "description": "An array of indices, or NULL"},
            {"name": "num_indices", "type": "int", "description": "Number of indices"},
            {"name": "size_indices", "type": "int", "description": "Size of each index (1, 2, or 4 bytes)"}
        ],
        "returns": "true on success or false on failure",
        "example": """float positions[] = {100, 100, 200, 300, 300, 100};
SDL_FColor colors[] = {{1, 0, 0, 1}, {0, 1, 0, 1}, {0, 0, 1, 1}};
SDL_RenderGeometryRaw(renderer, NULL, positions, 8, colors, sizeof(SDL_FColor), NULL, 0, 3, NULL, 0, 0);""",
        "remarks": "More flexible than SDL_RenderGeometry, useful for interleaved vertex data",
        "see_also": ["SDL_RenderGeometry", "SDL_Vertex"]
    }
}
