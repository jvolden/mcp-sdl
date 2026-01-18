"""SDL3 API reference - aggregates all SDL3 function categories."""

from . import (
    category_error,
    category_events,
    category_init,
    category_keyboard,
    category_mouse,
    category_render,
    category_surface,
    category_timer,
    category_video,
)

# Aggregate all SDL3 functions from category modules
SDL3_FUNCTIONS = {}
SDL3_FUNCTIONS.update(category_init.FUNCTIONS)
SDL3_FUNCTIONS.update(category_video.FUNCTIONS)
SDL3_FUNCTIONS.update(category_render.FUNCTIONS)
SDL3_FUNCTIONS.update(category_events.FUNCTIONS)
SDL3_FUNCTIONS.update(category_keyboard.FUNCTIONS)
SDL3_FUNCTIONS.update(category_mouse.FUNCTIONS)
SDL3_FUNCTIONS.update(category_error.FUNCTIONS)
SDL3_FUNCTIONS.update(category_surface.FUNCTIONS)
SDL3_FUNCTIONS.update(category_timer.FUNCTIONS)

# Category organization for SDL3
SDL3_CATEGORIES = {
    "init": category_init.FUNCTION_NAMES,
    "video": category_video.FUNCTION_NAMES,
    "render": category_render.FUNCTION_NAMES,
    "events": category_events.FUNCTION_NAMES,
    "keyboard": category_keyboard.FUNCTION_NAMES,
    "mouse": category_mouse.FUNCTION_NAMES,
    "error": category_error.FUNCTION_NAMES,
    "surface": category_surface.FUNCTION_NAMES,
    "timer": category_timer.FUNCTION_NAMES,
}

# Export for easy access
__all__ = ["SDL3_FUNCTIONS", "SDL3_CATEGORIES"]
