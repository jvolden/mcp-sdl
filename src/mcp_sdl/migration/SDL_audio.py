"""SDL_audio.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_audio.h"

MIGRATION_DATA = """
# SDL_audio.h Migration Guide

The audio subsystem in SDL3 is dramatically different than SDL2. The primary way
to play audio is no longer an audio callback; instead you bind SDL_AudioStreams
to devices; however, there is still a callback method available if needed.

The SDL 1.2 audio compatibility API has also been removed, as it was a
simplified version of the audio callback interface.

SDL3 will not implicitly initialize the audio subsystem on your behalf if you
open a device without doing so. Please explicitly call SDL_Init(SDL_INIT_AUDIO) at
some point.

SDL2 referred to audio devices that record sound as "capture" devices, and ones
that play sound to speakers as "output" devices. In SDL3, we've changed this
terminology to be "recording" devices and "playback" devices, which we hope is more
clear.

## Simple Migration Path

The simplest migration path from SDL2 looks something like this:

In SDL2, you might have done something like this to play audio:

```c
void SDLCALL MyAudioCallback(void *userdata, Uint8 * stream, int len)
{
    /* Calculate a little more audio here, maybe using `userdata`, write it to `stream` */
}

/* ...somewhere near startup... */
SDL_AudioSpec my_desired_audio_format;
SDL_zero(my_desired_audio_format);
my_desired_audio_format.format = AUDIO_S16;
my_desired_audio_format.channels = 2;
my_desired_audio_format.freq = 44100;
my_desired_audio_format.samples = 1024;
my_desired_audio_format.callback = MyAudioCallback;
my_desired_audio_format.userdata = &my_audio_callback_user_data;
SDL_AudioDeviceID my_audio_device = SDL_OpenAudioDevice(NULL, 0, &my_desired_audio_format, NULL, 0);
SDL_PauseAudioDevice(my_audio_device, 0);
```

In SDL3, you can do this:

```c
void SDLCALL MyNewAudioCallback(void *userdata, SDL_AudioStream *stream, int additional_amount, int total_amount)
{
    /* Calculate a little more audio here, maybe using `userdata`, write it to `stream`
     *
     * If you want to use the original callback, you could do something like this:
     */
    if (additional_amount > 0) {
        Uint8 *data = SDL_stack_alloc(Uint8, additional_amount);
        if (data) {
            MyAudioCallback(userdata, data, additional_amount);
            SDL_PutAudioStreamData(stream, data, additional_amount);
            SDL_stack_free(data);
        }
    }
}

/* ...somewhere near startup... */
const SDL_AudioSpec spec = { SDL_AUDIO_S16, 2, 44100 };
SDL_AudioStream *stream = SDL_OpenAudioDeviceStream(SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK, &spec, MyNewAudioCallback, &my_audio_callback_user_data);
SDL_ResumeAudioDevice(SDL_GetAudioStreamDevice(stream));
```

If you used SDL_QueueAudio instead of a callback in SDL2, this is also straightforward:

```c
/* ...somewhere near startup... */
const SDL_AudioSpec spec = { SDL_AUDIO_S16, 2, 44100 };
SDL_AudioStream *stream = SDL_OpenAudioDeviceStream(SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK, &spec, NULL, NULL);
SDL_ResumeAudioDevice(SDL_GetAudioStreamDevice(stream));

/* ...in your main loop... */
/* calculate a little more audio into `buf`, add it to `stream` */
SDL_PutAudioStreamData(stream, buf, buflen);
```

## Key API Changes

SDL_AudioInit() and SDL_AudioQuit() have been removed. Instead you can call
SDL_InitSubSystem() and SDL_QuitSubSystem() with SDL_INIT_AUDIO, which will properly
refcount the subsystems. You can choose a specific audio driver using
SDL_AUDIO_DRIVER hint.

The `SDL_AUDIO_ALLOW_*` symbols have been removed; now one may request the format they desire from the
audio device, but ultimately SDL_AudioStream will manage the difference. One can
use SDL_GetAudioDeviceFormat() to see what the final format is, if any
"allowed" changes should be accomodated by the app.

SDL_AudioDeviceID now represents both an open audio device's handle (a "logical"
device) and the instance ID that the hardware owns as long as it exists on the
system (a "physical" device). The separation between device instances and device
indexes is gone, and logical and physical devices are almost entirely
interchangeable at the API level.

APIs that use channel counts used to use a Uint8 for the channel; now they use int.

SDL_AudioSpec has been reduced; now it only holds format, channel, and sample
rate. The other SDL2 SDL_AudioSpec fields aren't relevant anymore.

## Function Renames

The following functions have been renamed:

• SDL_AudioStreamAvailable() => SDL_GetAudioStreamAvailable()
• SDL_AudioStreamClear() => SDL_ClearAudioStream(), returns bool
• SDL_AudioStreamFlush() => SDL_FlushAudioStream(), returns bool
• SDL_AudioStreamGet() => SDL_GetAudioStreamData()
• SDL_AudioStreamPut() => SDL_PutAudioStreamData(), returns bool
• SDL_FreeAudioStream() => SDL_DestroyAudioStream()
• SDL_LoadWAV_RW() => SDL_LoadWAV_IO(), returns bool
• SDL_MixAudioFormat() => SDL_MixAudio(), returns bool
• SDL_NewAudioStream() => SDL_CreateAudioStream()

## Removed Functions

The following functions have been removed:

• SDL_GetNumAudioDevices()
• SDL_GetAudioDeviceSpec()
• SDL_ConvertAudio()
• SDL_BuildAudioCVT()
• SDL_OpenAudio()
• SDL_CloseAudio()
• SDL_PauseAudio()
• SDL_GetAudioStatus()
• SDL_GetAudioDeviceStatus()
• SDL_GetDefaultAudioInfo()
• SDL_LockAudio()
• SDL_LockAudioDevice()
• SDL_UnlockAudio()
• SDL_UnlockAudioDevice()
• SDL_MixAudio()
• SDL_QueueAudio()
• SDL_DequeueAudio()
• SDL_ClearAudioQueue()
• SDL_GetQueuedAudioSize()

## Symbol Renames

The following symbols have been renamed:

• AUDIO_F32 => SDL_AUDIO_F32LE
• AUDIO_F32LSB => SDL_AUDIO_F32LE
• AUDIO_F32MSB => SDL_AUDIO_F32BE
• AUDIO_F32SYS => SDL_AUDIO_F32
• AUDIO_S16 => SDL_AUDIO_S16LE
• AUDIO_S16LSB => SDL_AUDIO_S16LE
• AUDIO_S16MSB => SDL_AUDIO_S16BE
• AUDIO_S16SYS => SDL_AUDIO_S16
• AUDIO_S32 => SDL_AUDIO_S32LE
• AUDIO_S32LSB => SDL_AUDIO_S32LE
• AUDIO_S32MSB => SDL_AUDIO_S32BE
• AUDIO_S32SYS => SDL_AUDIO_S32
• AUDIO_S8 => SDL_AUDIO_S8
• AUDIO_U8 => SDL_AUDIO_U8

## Symbol Removals

The following symbols have been removed:

• SDL_MIX_MAXVOLUME - mixer volume is now a float between 0.0 and 1.0

## Audio Conversion

SDL_AudioCVT interface has been removed, the SDL_AudioStream interface (for
audio supplied in pieces) or the new SDL_ConvertAudioSamples() function (for
converting a complete audio buffer in one call) can be used instead.

Code that used to look like this:

```c
SDL_AudioCVT cvt;
SDL_BuildAudioCVT(&cvt, src_format, src_channels, src_rate, dst_format, dst_channels, dst_rate);
cvt.len = src_len;
cvt.buf = (Uint8 *) SDL_malloc(src_len * cvt.len_mult);
SDL_memcpy(cvt.buf, src_data, src_len);
SDL_ConvertAudio(&cvt);
do_something(cvt.buf, cvt.len_cvt);
```

should be changed to:

```c
Uint8 *dst_data = NULL;
int dst_len = 0;
const SDL_AudioSpec src_spec = { src_format, src_channels, src_rate };
const SDL_AudioSpec dst_spec = { dst_format, dst_channels, dst_rate };
if (!SDL_ConvertAudioSamples(&src_spec, src_data, src_len, &dst_spec, &dst_data, &dst_len)) {
    /* error */
}
do_something(dst_data, dst_len);
SDL_free(dst_data);
```
"""
