"""MCP tool implementations for SDL3 API reference."""

# Import all tools from submodules
from .api_tools import (
    sdl_function_reference,
    sdl_search_functions,
)
from .examples_tools import (
    sdl_get_example,
    sdl_list_example_categories,
    sdl_list_examples,
    sdl_search_examples,
)
from .migration_tools import (
    sdl_migration_header,
    sdl_migration_lookup,
    sdl_migration_search,
)

__all__ = [
    # API tools
    "sdl_function_reference",
    "sdl_search_functions",
    # Example tools
    "sdl_get_example",
    "sdl_list_example_categories",
    "sdl_list_examples",
    "sdl_search_examples",
    # Migration tools
    "sdl_migration_header",
    "sdl_migration_lookup",
    "sdl_migration_search",
]
