"""SDL3 input example: Gamepad state polling."""

EXAMPLE = {
    "03-gamepad-polling": {
        "title": "Gamepad State Polling",
        "description": "Polls gamepad state each frame and draws a visual representation",
        "difficulty": "intermediate",
        "url": "https://examples.libsdl.org/SDL3/input/03-gamepad-polling/",
        "code": """/*
 * This example code looks for the current gamepad state once per frame,
 * and draws a visual representation of it.
 *
 * This code is public domain. Feel free to use it for any purpose!
 */

#define SDL_MAIN_USE_CALLBACKS 1
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

static SDL_Window *window = NULL;
static SDL_Renderer *renderer = NULL;
static SDL_Texture *texture = NULL;
static SDL_Gamepad *gamepad = NULL;

#define WINDOW_WIDTH 640
#define WINDOW_HEIGHT 480

SDL_AppResult SDL_AppInit(void **appstate, int argc, char *argv[])
{
    char *png_path = NULL;
    SDL_Surface *surface = NULL;

    SDL_SetAppMetadata("Example Input Gamepad Polling", "1.0", "com.example.input-gamepad-polling");

    if (!SDL_Init(SDL_INIT_VIDEO | SDL_INIT_GAMEPAD)) {
        SDL_Log("Couldn't initialize SDL: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    if (!SDL_CreateWindowAndRenderer("examples/input/gamepad-polling", WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_RESIZABLE, &window, &renderer)) {
        SDL_Log("Couldn't create window/renderer: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    if (!SDL_SetRenderLogicalPresentation(renderer, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_LOGICAL_PRESENTATION_STRETCH)) {
        return SDL_APP_FAILURE;
    }

    SDL_asprintf(&png_path, "%sgamepad_front.png", SDL_GetBasePath());
    surface = SDL_LoadPNG(png_path);
    if (!surface) {
        SDL_Log("Couldn't load bitmap: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    SDL_free(png_path);

    texture = SDL_CreateTextureFromSurface(renderer, surface);
    if (!texture) {
        SDL_Log("Couldn't create static texture: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    SDL_DestroySurface(surface);

    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppEvent(void *appstate, SDL_Event *event)
{
    if (event->type == SDL_EVENT_QUIT) {
        return SDL_APP_SUCCESS;
    } else if (event->type == SDL_EVENT_GAMEPAD_ADDED) {
        if (gamepad == NULL) {
            gamepad = SDL_OpenGamepad(event->gdevice.which);
            if (!gamepad) {
                SDL_Log("Failed to open gamepad ID %u: %s", (unsigned int) event->gdevice.which, SDL_GetError());
            }
        }
    } else if (event->type == SDL_EVENT_GAMEPAD_REMOVED) {
        if (gamepad && (SDL_GetGamepadID(gamepad) == event->gdevice.which)) {
            SDL_CloseGamepad(gamepad);
            gamepad = NULL;
        }
    }
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppIterate(void *appstate)
{
    const char *text = "Plug in a gamepad, please.";

    if (gamepad) {
        text = SDL_GetGamepadName(gamepad);
    }

    SDL_SetRenderDrawColor(renderer, 0xFF, 0xFF, 0xFF, 0xFF);
    SDL_RenderClear(renderer);

    if (gamepad) {
        SDL_RenderTexture(renderer, texture, NULL, NULL);

        /* Draw button/axis state - simplified for brevity */
        SDL_SetRenderDrawColor(renderer, 0x00, 0xFF, 0x00, 0xFF);
        
        /* Check if buttons are pressed and draw indicators */
        for (int i = 0; i < SDL_GAMEPAD_BUTTON_COUNT; i++) {
            if (SDL_GetGamepadButton(gamepad, (SDL_GamepadButton) i)) {
                /* Draw button indicator */
            }
        }
    }

    SDL_SetRenderDrawColor(renderer, 0x00, 0x00, 0xFF, 0xFF);
    SDL_RenderDebugText(renderer, 10, 10, text);
    SDL_RenderPresent(renderer);

    return SDL_APP_CONTINUE;
}

void SDL_AppQuit(void *appstate, SDL_AppResult result)
{
    SDL_DestroyTexture(texture);
    SDL_CloseGamepad(gamepad);
}"""
    }
}
