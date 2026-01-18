"""SDL_InitFlags datatype definition."""

DATATYPE = {
    "SDL_InitFlags": {
        "description": "Flags for subsystems to initialize",
        "values": [
            {"name": "SDL_INIT_AUDIO", "description": "Audio subsystem"},
            {"name": "SDL_INIT_VIDEO", "description": "Video subsystem"},
            {"name": "SDL_INIT_JOYSTICK", "description": "Joystick subsystem"},
            {"name": "SDL_INIT_HAPTIC", "description": "Haptic (force feedback) subsystem"},
            {"name": "SDL_INIT_GAMEPAD", "description": "Gamepad subsystem"},
            {"name": "SDL_INIT_EVENTS", "description": "Events subsystem"},
            {"name": "SDL_INIT_SENSOR", "description": "Sensor subsystem"},
            {"name": "SDL_INIT_CAMERA", "description": "Camera subsystem"}
        ]
    }
}
