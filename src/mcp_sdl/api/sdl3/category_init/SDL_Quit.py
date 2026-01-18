"""SDL_Quit function definition."""

FUNCTION = {
    "SDL_Quit": {
        "category": "init",
        "description": "Clean up all initialized subsystems and shut down SDL",
        "signature": "void SDL_Quit(void)",
        "parameters": [],
        "returns": "void",
        "example": """// Clean up before exiting
SDL_Quit();
return 0;"""
    }
}
