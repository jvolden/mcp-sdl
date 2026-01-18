"""Tests for refactored tools structure."""

import pytest

from mcp_sdl.tools import (
    # API tools
    sdl_function_reference,
    # Example tools
    sdl_get_example,
    sdl_list_example_categories,
    sdl_list_examples,
    # Migration tools
    sdl_migration_header,
    sdl_migration_lookup,
    sdl_migration_search,
    sdl_search_examples,
    sdl_search_functions,
)


class TestToolsStructure:
    """Test that all tools are properly exposed from the tools package."""

    def test_api_tools_importable(self):
        """Test that API tools can be imported from tools package."""
        assert callable(sdl_function_reference)
        assert callable(sdl_search_functions)

    def test_example_tools_importable(self):
        """Test that example tools can be imported from tools package."""
        assert callable(sdl_list_example_categories)
        assert callable(sdl_list_examples)
        assert callable(sdl_get_example)
        assert callable(sdl_search_examples)

    def test_migration_tools_importable(self):
        """Test that migration tools can be imported from tools package."""
        assert callable(sdl_migration_lookup)
        assert callable(sdl_migration_header)
        assert callable(sdl_migration_search)

    def test_all_tools_are_async(self):
        """Test that all tools are async functions."""
        import inspect

        all_tools = [
            sdl_function_reference,
            sdl_search_functions,
            sdl_list_example_categories,
            sdl_list_examples,
            sdl_get_example,
            sdl_search_examples,
            sdl_migration_lookup,
            sdl_migration_header,
            sdl_migration_search,
        ]

        for tool in all_tools:
            assert inspect.iscoroutinefunction(tool), f"{tool.__name__} should be async"

    def test_tool_modules_exist(self):
        """Test that tool modules exist and are importable."""
        from mcp_sdl.tools import api_tools, examples_tools, migration_tools

        assert api_tools is not None
        assert examples_tools is not None
        assert migration_tools is not None

    def test_api_tools_module_exports(self):
        """Test that api_tools module exports expected functions."""
        from mcp_sdl.tools import api_tools

        assert hasattr(api_tools, "sdl_function_reference")
        assert hasattr(api_tools, "sdl_search_functions")

    def test_examples_tools_module_exports(self):
        """Test that examples_tools module exports expected functions."""
        from mcp_sdl.tools import examples_tools

        assert hasattr(examples_tools, "sdl_list_example_categories")
        assert hasattr(examples_tools, "sdl_list_examples")
        assert hasattr(examples_tools, "sdl_get_example")
        assert hasattr(examples_tools, "sdl_search_examples")

    def test_migration_tools_module_exports(self):
        """Test that migration_tools module exports expected functions."""
        from mcp_sdl.tools import migration_tools

        assert hasattr(migration_tools, "sdl_migration_lookup")
        assert hasattr(migration_tools, "sdl_migration_header")
        assert hasattr(migration_tools, "sdl_migration_search")

    def test_tools_package_has_dunder_all(self):
        """Test that tools package defines __all__ for explicit exports."""
        from mcp_sdl import tools

        assert hasattr(tools, "__all__")
        assert isinstance(tools.__all__, list)
        assert len(tools.__all__) == 9  # Total number of tools

    def test_all_exports_in_dunder_all(self):
        """Test that all expected tool names are in __all__."""
        from mcp_sdl import tools

        expected = [
            "sdl_function_reference",
            "sdl_search_functions",
            "sdl_get_example",
            "sdl_list_example_categories",
            "sdl_list_examples",
            "sdl_search_examples",
            "sdl_migration_header",
            "sdl_migration_lookup",
            "sdl_migration_search",
        ]

        for tool_name in expected:
            assert tool_name in tools.__all__, f"{tool_name} should be in __all__"


class TestToolsBackwardCompatibility:
    """Test that tools still work the same way after refactoring."""

    @pytest.mark.asyncio
    async def test_api_tool_still_works(self):
        """Test that API tools still work after refactoring."""
        result = await sdl_function_reference("SDL_Init")
        assert "SDL_Init" in result
        assert "Initialize" in result
        assert "SDL" in result

    @pytest.mark.asyncio
    async def test_migration_tool_still_works(self):
        """Test that migration tools still work after refactoring."""
        result = await sdl_migration_header("SDL_audio.h")
        assert "SDL_audio.h" in result
        assert "SDL2" in result or "SDL3" in result
