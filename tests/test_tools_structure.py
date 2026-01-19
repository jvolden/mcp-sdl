"""Tests for refactored tools structure."""

from fastmcp.client.client import Client
from fastmcp.tools import FunctionTool


class TestToolsStructure:
    """Test that all tools are properly exposed from the tools package."""

    def test_api_tools_importable(self):
        """Test that API tools can be imported from tools package."""
        from mcp_sdl.tools import sdl_function_reference, sdl_search_functions

        # With @mcp.tool decorator, these become FunctionTool objects
        assert isinstance(sdl_function_reference, FunctionTool)
        assert isinstance(sdl_search_functions, FunctionTool)

    def test_example_tools_importable(self):
        """Test that example tools can be imported from tools package."""
        from mcp_sdl.tools import sdl_examples

        # With @mcp.tool decorator, this becomes a FunctionTool object
        assert isinstance(sdl_examples, FunctionTool)

    def test_migration_tools_importable(self):
        """Test that migration tools can be imported from tools package."""
        from mcp_sdl.tools import sdl_migration

        # With @mcp.tool decorator, this becomes a FunctionTool object
        assert isinstance(sdl_migration, FunctionTool)

    def test_all_tools_registered(self):
        """Test that all tools are registered with proper names."""
        from mcp_sdl.tools import (
            sdl_examples,
            sdl_function_reference,
            sdl_migration,
            sdl_search_functions,
        )

        all_tools = [
            sdl_function_reference,
            sdl_search_functions,
            sdl_examples,
            sdl_migration,
        ]

        for tool in all_tools:
            assert isinstance(tool, FunctionTool)
            assert tool.name is not None
            assert tool.description is not None

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

        assert hasattr(examples_tools, "sdl_examples")

    def test_migration_tools_module_exports(self):
        """Test that migration_tools module exports expected functions."""
        from mcp_sdl.tools import migration_tools

        assert hasattr(migration_tools, "sdl_migration")

    def test_tools_package_has_dunder_all(self):
        """Test that tools package defines __all__ for explicit exports."""
        from mcp_sdl import tools

        assert hasattr(tools, "__all__")
        assert isinstance(tools.__all__, list)
        assert len(tools.__all__) == 4  # Total number of tools

    def test_all_exports_in_dunder_all(self):
        """Test that all expected tool names are in __all__."""
        from mcp_sdl import tools

        expected = [
            "sdl_function_reference",
            "sdl_search_functions",
            "sdl_examples",
            "sdl_migration",
        ]

        for tool_name in expected:
            assert tool_name in tools.__all__, f"{tool_name} should be in __all__"


class TestToolsBackwardCompatibility:
    """Test that tools still work through the MCP interface after refactoring."""

    async def test_api_tool_still_works(self, client: Client):
        """Test that API tools still work after refactoring."""
        result = await client.call_tool("sdl_function_reference", {"function_name": "SDL_Init"})
        data = result.data
        assert "SDL_Init" in data
        assert "Initialize" in data
        assert "SDL" in data

    async def test_migration_tool_still_works(self, client: Client):
        """Test that migration tools still work after refactoring."""
        result = await client.call_tool("sdl_migration", {"header_name": "SDL_audio.h"})
        data = result.data
        assert "SDL_audio.h" in data
        assert "SDL2" in data or "SDL3" in data
