"""SDL_TextureAccess enum definition."""

ENUM = {
    "SDL_TextureAccess": {
        "description": "Texture access patterns",
        "values": [
            {"name": "SDL_TEXTUREACCESS_STATIC", "description": "Changes rarely, not lockable"},
            {"name": "SDL_TEXTUREACCESS_STREAMING", "description": "Changes frequently, lockable"},
            {"name": "SDL_TEXTUREACCESS_TARGET", "description": "Can be used as a render target"}
        ]
    }
}
