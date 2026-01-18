"""SDL_TextureAddressMode enum definition."""

ENUM = {
    "SDL_TextureAddressMode": {
        "description": "How textures are addressed outside of the 0-1 range",
        "values": [
            {"name": "SDL_TEXTURE_ADDRESS_CLAMP", "description": "Clamp to edge"},
            {"name": "SDL_TEXTURE_ADDRESS_WRAP", "description": "Wrap around"},
            {"name": "SDL_TEXTURE_ADDRESS_MIRROR", "description": "Mirror repeat"}
        ]
    }
}
