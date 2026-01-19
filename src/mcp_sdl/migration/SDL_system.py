"""SDL_system.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_system.h"

MIGRATION_DATA = """
# SDL_system.h Migration Guide

## Windows Message Hook Changes

SDL_WindowsMessageHook has changed signatures so the message may be modified and
it can block further message processing.

## Android Permission Changes

SDL_RequestAndroidPermission is no longer a blocking call; the caller now
provides a callback function that fires when a response is available.

## iOS Function Renames

SDL_iPhoneSetAnimationCallback() and SDL_iPhoneSetEventPump() have been renamed
to SDL_SetiOSAnimationCallback() and SDL_SetiOSEventPump(), respectively. SDL2
has had macros to provide this new name with the old symbol since the
introduction of the iPad, but now the correctly-named symbol is the only option.

## TV Detection

SDL_IsAndroidTV() has been renamed SDL_IsTV() and is no longer Android-specific;
an app running on an Apple TV device will also return true, for example.

## Removed Functions

The following functions have been removed:

• SDL_GetWinRTFSPathUNICODE() - WinRT support was removed in SDL3.
• SDL_GetWinRTFSPathUTF8() - WinRT support was removed in SDL3.
• SDL_RenderGetD3D11Device() - replaced with the "SDL.renderer.d3d11.device"
property
• SDL_RenderGetD3D12Device() - replaced with the "SDL.renderer.d3d12.device"
property
• SDL_RenderGetD3D9Device() - replaced with the "SDL.renderer.d3d9.device"
property
• SDL_WinRTGetDeviceFamily() - WinRT support was removed in SDL3.

## Function Renames

The following functions have been renamed:

• SDL_AndroidBackButton() => SDL_SendAndroidBackButton()
• SDL_AndroidGetActivity() => SDL_GetAndroidActivity()
• SDL_AndroidGetExternalStoragePath() => SDL_GetAndroidExternalStoragePath()
• SDL_AndroidGetExternalStorageState() => SDL_GetAndroidExternalStorageState()
• SDL_AndroidGetInternalStoragePath() => SDL_GetAndroidInternalStoragePath()
• SDL_AndroidGetJNIEnv() => SDL_GetAndroidJNIEnv()
• SDL_AndroidRequestPermission() => SDL_RequestAndroidPermission(), returns bool
• SDL_AndroidRequestPermissionCallback() => SDL_RequestAndroidPermissionCallback()
• SDL_AndroidSendMessage() => SDL_SendAndroidMessage(), returns bool
• SDL_AndroidShowToast() => SDL_ShowAndroidToast(), returns bool
• SDL_DXGIGetOutputInfo() => SDL_GetDXGIOutputInfo(), returns bool
• SDL_Direct3D9GetAdapterIndex() => SDL_GetDirect3D9AdapterIndex()
• SDL_GDKGetDefaultUser() => SDL_GetGDKDefaultUser(), returns bool
• SDL_GDKGetTaskQueue() => SDL_GetGDKTaskQueue(), returns bool
• SDL_IsAndroidTV() => SDL_IsTV()
• SDL_LinuxSetThreadPriority() => SDL_SetLinuxThreadPriority(), returns bool
• SDL_LinuxSetThreadPriorityAndPolicy() => SDL_SetLinuxThreadPriorityAndPolicy(),
returns bool
• SDL_OnApplicationDidBecomeActive() => SDL_OnApplicationDidEnterForeground()
• SDL_OnApplicationWillResignActive() => SDL_OnApplicationWillEnterBackground()
• SDL_iOSSetAnimationCallback() => SDL_SetiOSAnimationCallback(), returns bool
• SDL_iOSSetEventPump() => SDL_SetiOSEventPump()
• SDL_iPhoneSetAnimationCallback() => SDL_SetiOSAnimationCallback(), returns bool
• SDL_iPhoneSetEventPump() => SDL_SetiOSEventPump()
"""
