"""SDL_GetAppMetadataProperty function definition."""

FUNCTION = {
    "SDL_GetAppMetadataProperty": {
        "category": "init",
        "description": "Get metadata about your app",
        "signature": "const char* SDL_GetAppMetadataProperty(const char *name)",
        "parameters": [
            {"name": "name", "type": "const char*", "description": "The property name to query"}
        ],
        "returns": "The property value, or NULL if not set",
        "example": """// Get app metadata
const char *appname = SDL_GetAppMetadataProperty("SDL_APP_METADATA_NAME");
if (appname) {
    SDL_Log("App name: %s", appname);
}"""
    }
}
