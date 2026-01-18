"""SDL_AppResult enum definition."""

ENUM = {
    "SDL_AppResult": {
        "description": "Return values for SDL application callbacks",
        "values": [
            {"name": "SDL_APP_CONTINUE", "description": "Application should continue"},
            {"name": "SDL_APP_SUCCESS", "description": "Application completed successfully"},
            {"name": "SDL_APP_FAILURE", "description": "Application encountered an error"}
        ]
    }
}
