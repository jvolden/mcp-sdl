"""SDL3 renderer example: Load and render textures."""

EXAMPLE = {
    "06-textures": {
        "title": "Load and Render Textures",
        "description": "Creates window and renderer, loads a texture from PNG, and draws it multiple times",
        "difficulty": "beginner",
        "url": "https://examples.libsdl.org/SDL3/renderer/06-textures/",
        "code": """/*
 * This example creates an SDL window and renderer, and then draws some
 * textures to it every frame.
 *
 * This code is public domain. Feel free to use it for any purpose!
 */

#define SDL_MAIN_USE_CALLBACKS 1
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

static SDL_Window *window = NULL;
static SDL_Renderer *renderer = NULL;
static SDL_Texture *texture = NULL;
static int texture_width = 0;
static int texture_height = 0;

#define WINDOW_WIDTH 640
#define WINDOW_HEIGHT 480

SDL_AppResult SDL_AppInit(void **appstate, int argc, char *argv[])
{
    SDL_Surface *surface = NULL;
    char *png_path = NULL;

    SDL_SetAppMetadata("Example Renderer Textures", "1.0", "com.example.renderer-textures");

    if (!SDL_Init(SDL_INIT_VIDEO)) {
        SDL_Log("Couldn't initialize SDL: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    if (!SDL_CreateWindowAndRenderer("examples/renderer/textures", WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_RESIZABLE, &window, &renderer)) {
        SDL_Log("Couldn't create window/renderer: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }
    SDL_SetRenderLogicalPresentation(renderer, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_LOGICAL_PRESENTATION_LETTERBOX);

    SDL_asprintf(&png_path, "%ssample.png", SDL_GetBasePath());
    surface = SDL_LoadPNG(png_path);
    if (!surface) {
        SDL_Log("Couldn't load png: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    SDL_free(png_path);

    texture_width = surface->w;
    texture_height = surface->h;

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
    }
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppIterate(void *appstate)
{
    SDL_FRect dst_rect;
    const Uint64 now = SDL_GetTicks();
    const float direction = ((now % 2000) >= 1000) ? 1.0f : -1.0f;
    const float scale = ((float) (((int) (now % 1000)) - 500) / 500.0f) * direction;

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
    SDL_RenderClear(renderer);

    /* top left */
    dst_rect.x = (100.0f * scale);
    dst_rect.y = 0.0f;
    dst_rect.w = (float) texture_width;
    dst_rect.h = (float) texture_height;
    SDL_RenderTexture(renderer, texture, NULL, &dst_rect);

    /* center */
    dst_rect.x = ((float) (WINDOW_WIDTH - texture_width)) / 2.0f;
    dst_rect.y = ((float) (WINDOW_HEIGHT - texture_height)) / 2.0f;
    dst_rect.w = (float) texture_width;
    dst_rect.h = (float) texture_height;
    SDL_RenderTexture(renderer, texture, NULL, &dst_rect);

    /* bottom right */
    dst_rect.x = ((float) (WINDOW_WIDTH - texture_width)) - (100.0f * scale);
    dst_rect.y = (float) (WINDOW_HEIGHT - texture_height);
    dst_rect.w = (float) texture_width;
    dst_rect.h = (float) texture_height;
    SDL_RenderTexture(renderer, texture, NULL, &dst_rect);

    SDL_RenderPresent(renderer);

    return SDL_APP_CONTINUE;
}

void SDL_AppQuit(void *appstate, SDL_AppResult result)
{
    SDL_DestroyTexture(texture);
}"""
    }
}
