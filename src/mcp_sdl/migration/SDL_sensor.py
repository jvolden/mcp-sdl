"""SDL_sensor.h migration guide - SDL2 to SDL3."""

HEADER = "SDL_sensor.h"

MIGRATION_DATA = """
# SDL_sensor.h Migration Guide

## ID Type Changes

SDL_SensorID has changed from Sint32 to Uint32, with an invalid ID being 0.

## Device Enumeration

Rather than iterating over sensors using device index, there is a new function
SDL_GetSensors() to get the current list of sensors, and new functions to get
information about sensors from their instance ID.

## Timestamp Changes

Removed SDL_SensorGetDataWithTimestamp(), if you want timestamps for the sensor
data, you should use the sensor_timestamp member of SDL_EVENT_SENSOR_UPDATE
events.

## Function Renames

The following functions have been renamed:

• SDL_SensorClose() => SDL_CloseSensor()
• SDL_SensorFromInstanceID() => SDL_GetSensorFromID()
• SDL_SensorGetData() => SDL_GetSensorData(), returns bool
• SDL_SensorGetInstanceID() => SDL_GetSensorID()
• SDL_SensorGetName() => SDL_GetSensorName()
• SDL_SensorGetNonPortableType() => SDL_GetSensorNonPortableType()
• SDL_SensorGetType() => SDL_GetSensorType()
• SDL_SensorOpen() => SDL_OpenSensor()
• SDL_SensorUpdate() => SDL_UpdateSensors()

## Removed Functions

The following functions have been removed:

• SDL_LockSensors()
• SDL_NumSensors() - replaced with SDL_GetSensors()
• SDL_SensorGetDeviceInstanceID()
• SDL_SensorGetDeviceName() - replaced with SDL_GetSensorNameForID()
• SDL_SensorGetDeviceNonPortableType() - replaced with
SDL_GetSensorNonPortableTypeForID()
• SDL_SensorGetDeviceType() - replaced with SDL_GetSensorTypeForID()
• SDL_UnlockSensors()
"""
