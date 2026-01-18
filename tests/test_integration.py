"""Integration smoke tests for MCP protocol compatibility.

These tests validate that FastMCP protocol integration works correctly
and catch breaking changes in FastMCP version updates.
"""

import pytest

from mcp_sdl.server import mcp


class TestMCPProtocolIntegration:
    """Smoke tests for MCP protocol compatibility."""

    @pytest.mark.asyncio
    async def test_server_exposes_all_tools(self):
        """Test that server properly registers and exposes all 9 tools."""
        # Get all registered tool names from FastMCP server
        tool_names = await mcp.get_tools()

        # Verify we have all 9 expected tools
        expected_tools = [
            "sdl_function_reference",
            "sdl_search_functions",
            "sdl_list_example_categories",
            "sdl_list_examples",
            "sdl_get_example",
            "sdl_search_examples",
            "sdl_migration_lookup",
            "sdl_migration_header",
            "sdl_migration_search",
        ]

        assert len(tool_names) == 9, f"Expected 9 tools, got {len(tool_names)}"
        for expected_tool in expected_tools:
            assert expected_tool in tool_names, f"Missing tool: {expected_tool}"

    @pytest.mark.asyncio
    async def test_tool_can_be_retrieved(self):
        """Test that individual tools can be retrieved through MCP interface."""
        # Retrieve a specific tool
        tool = await mcp.get_tool("sdl_function_reference")

        # Verify tool structure (FastMCP returns FunctionTool objects)
        assert tool is not None, "Tool not found"
        assert tool.name == "sdl_function_reference"
        assert tool.description, "Tool missing description"
        assert hasattr(tool, 'fn'), "Tool missing function reference"
        
        # Verify the tool is callable
        assert callable(tool.fn), "Tool function is not callable"
