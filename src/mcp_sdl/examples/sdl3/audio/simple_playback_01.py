"""SDL3 audio example: Simple audio playback with sine wave."""

EXAMPLE = {
    "01-simple-playback": {
        "title": "Simple Audio Playback",
        "description": "Creates an audio stream and generates a 440Hz sine wave tone",
        "difficulty": "beginner",
        "url": "https://examples.libsdl.org/SDL3/audio/01-simple-playback/",
        "code": """/*
 * This example code creates a simple audio stream for playing sound, and
 * generates a sine wave sound effect for it to play as time goes on.
 *
 * This code is public domain. Feel free to use it for any purpose!
 */

#define SDL_MAIN_USE_CALLBACKS 1
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

static SDL_Window *window = NULL;
static SDL_Renderer *renderer = NULL;
static SDL_AudioStream *stream = NULL;
static int current_sine_sample = 0;

SDL_AppResult SDL_AppInit(void **appstate, int argc, char *argv[])
{
    SDL_AudioSpec spec;

    SDL_SetAppMetadata("Example Audio Simple Playback", "1.0", "com.example.audio-simple-playback");

    if (!SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO)) {
        SDL_Log("Couldn't initialize SDL: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    if (!SDL_CreateWindowAndRenderer("examples/audio/simple-playback", 640, 480, SDL_WINDOW_RESIZABLE, &window, &renderer)) {
        SDL_Log("Couldn't create window/renderer: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }
    SDL_SetRenderLogicalPresentation(renderer, 640, 480, SDL_LOGICAL_PRESENTATION_LETTERBOX);

    spec.channels = 1;
    spec.format = SDL_AUDIO_F32;
    spec.freq = 8000;
    stream = SDL_OpenAudioDeviceStream(SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK, &spec, NULL, NULL);
    if (!stream) {
        SDL_Log("Couldn't create audio stream: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    SDL_ResumeAudioStreamDevice(stream);

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
    const int minimum_audio = (8000 * sizeof (float)) / 2;
    if (SDL_GetAudioStreamQueued(stream) < minimum_audio) {
        static float samples[512];
        int i;

        /* generate a 440Hz pure tone */
        for (i = 0; i < SDL_arraysize(samples); i++) {
            const int freq = 440;
            const float phase = current_sine_sample * freq / 8000.0f;
            samples[i] = SDL_sinf(phase * 2 * SDL_PI_F);
            current_sine_sample++;
        }

        current_sine_sample %= 8000;

        SDL_PutAudioStreamData(stream, samples, sizeof (samples));
    }

    SDL_RenderClear(renderer);
    SDL_RenderPresent(renderer);

    return SDL_APP_CONTINUE;
}

void SDL_AppQuit(void *appstate, SDL_AppResult result)
{
    /* SDL will clean up the window/renderer for us. */
}"""
    }
}
