"""SDL_SetAppMetadataProperty function definition."""

FUNCTION = {
    "SDL_SetAppMetadataProperty": {
        "category": "init",
        "description": "Specify metadata about your app through a set of properties",
        "signature": "bool SDL_SetAppMetadataProperty(const char *name, const char *value)",
        "parameters": [
            {"name": "name", "type": "const char*", "description": "The property name (e.g., 'SDL_APP_METADATA_NAME', 'SDL_APP_METADATA_VERSION')"},
            {"name": "value", "type": "const char*", "description": "The property value"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Set detailed app metadata
SDL_SetAppMetadataProperty("SDL_APP_METADATA_NAME", "My Game");
SDL_SetAppMetadataProperty("SDL_APP_METADATA_VERSION", "1.0.0");
SDL_SetAppMetadataProperty("SDL_APP_METADATA_IDENTIFIER", "com.example.mygame");
SDL_SetAppMetadataProperty("SDL_APP_METADATA_CREATOR", "Example Games Inc.");"""
    }
}
