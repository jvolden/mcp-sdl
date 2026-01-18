"""SDL_SetAppMetadata function definition."""

FUNCTION = {
    "SDL_SetAppMetadata": {
        "category": "init",
        "description": "Specify basic metadata about your app",
        "signature": "bool SDL_SetAppMetadata(const char *appname, const char *appversion, const char *appidentifier)",
        "parameters": [
            {"name": "appname", "type": "const char*", "description": "A user-visible name for the app (e.g., 'My Game')"},
            {"name": "appversion", "type": "const char*", "description": "A user-visible version string (e.g., '1.0.2')"},
            {"name": "appidentifier", "type": "const char*", "description": "A unique identifier in reverse-domain format (e.g., 'com.example.mygame')"}
        ],
        "returns": "true on success, false on failure",
        "example": """// Set app metadata at startup
if (!SDL_SetAppMetadata("My Game", "1.0.0", "com.example.mygame")) {
    SDL_Log("Failed to set app metadata: %s", SDL_GetError());
}"""
    }
}
