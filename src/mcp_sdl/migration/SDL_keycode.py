"""SDL_keycode.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_keycode.h"

MIGRATION_DATA = """
# SDL_keycode.h Migration Guide

## Keycode Type Changes

SDL_Keycode is now Uint32 and the SDLK_* constants are now defines instead of an
enum, to more clearly reflect that they are a subset of the possible values of
an SDL_Keycode.

In addition to the `SDLK_SCANCODE_MASK` bit found on key codes that directly map to scancodes, there is now the `SDLK_EXTENDED_MASK` bit used to denote key codes that don't have a corresponding scancode, and
aren't a unicode value.

## Removed Symbols

The following symbols have been removed:

• KMOD_RESERVED
• SDLK_WWW
• SDLK_MAIL
• SDLK_CALCULATOR
• SDLK_COMPUTER
• SDLK_BRIGHTNESSDOWN
• SDLK_BRIGHTNESSUP
• SDLK_DISPLAYSWITCH
• SDLK_KBDILLUMTOGGLE
• SDLK_KBDILLUMDOWN
• SDLK_KBDILLUMUP
• SDLK_APP1
• SDLK_APP2

## Symbol Renames

The following symbols have been renamed:

• KMOD_ALT => SDL_KMOD_ALT
• KMOD_CAPS => SDL_KMOD_CAPS
• KMOD_CTRL => SDL_KMOD_CTRL
• KMOD_GUI => SDL_KMOD_GUI
• KMOD_LALT => SDL_KMOD_LALT
• KMOD_LCTRL => SDL_KMOD_LCTRL
• KMOD_LGUI => SDL_KMOD_LGUI
• KMOD_LSHIFT => SDL_KMOD_LSHIFT
• KMOD_MODE => SDL_KMOD_MODE
• KMOD_NONE => SDL_KMOD_NONE
• KMOD_NUM => SDL_KMOD_NUM
• KMOD_RALT => SDL_KMOD_RALT
• KMOD_RCTRL => SDL_KMOD_RCTRL
• KMOD_RGUI => SDL_KMOD_RGUI
• KMOD_RSHIFT => SDL_KMOD_RSHIFT
• KMOD_SCROLL => SDL_KMOD_SCROLL
• KMOD_SHIFT => SDL_KMOD_SHIFT
• SDLK_AUDIOFASTFORWARD => SDLK_MEDIA_FAST_FORWARD
• SDLK_AUDIOMUTE => SDLK_MUTE
• SDLK_AUDIONEXT => SDLK_MEDIA_NEXT_TRACK
• SDLK_AUDIOPLAY => SDLK_MEDIA_PLAY
• SDLK_AUDIOPREV => SDLK_MEDIA_PREVIOUS_TRACK
• SDLK_AUDIOREWIND => SDLK_MEDIA_REWIND
• SDLK_AUDIOSTOP => SDLK_MEDIA_STOP
• SDLK_BACKQUOTE => SDLK_GRAVE
• SDLK_EJECT => SDLK_MEDIA_EJECT
• SDLK_MEDIASELECT => SDLK_MEDIA_SELECT
• SDLK_QUOTE => SDLK_APOSTROPHE
• SDLK_QUOTEDBL => SDLK_DBLAPOSTROPHE
• SDLK_a => SDLK_A
• SDLK_b => SDLK_B
• SDLK_c => SDLK_C
• SDLK_d => SDLK_D
• SDLK_e => SDLK_E
• SDLK_f => SDLK_F
• SDLK_g => SDLK_G
• SDLK_h => SDLK_H
• SDLK_i => SDLK_I
• SDLK_j => SDLK_J
• SDLK_k => SDLK_K
• SDLK_l => SDLK_L
• SDLK_m => SDLK_M
• SDLK_n => SDLK_N
• SDLK_o => SDLK_O
• SDLK_p => SDLK_P
• SDLK_q => SDLK_Q
• SDLK_r => SDLK_R
• SDLK_s => SDLK_S
• SDLK_t => SDLK_T
• SDLK_u => SDLK_U
• SDLK_v => SDLK_V
• SDLK_w => SDLK_W
• SDLK_x => SDLK_X
• SDLK_y => SDLK_Y
• SDLK_z => SDLK_Z
"""
