"""Pytest configuration and fixtures for MCP SDL3 Server tests.

This module provides shared fixtures following FastMCP testing best practices.

Testing Pattern:
    Tools decorated with @mcp.tool are tested via client.call_tool(), not by
    calling functions directly. This ensures we test the actual MCP interface.

Example:
    async def test_my_tool(client: Client):
        result = await client.call_tool("sdl_function_reference",
                                        {"function_name": "SDL_Init"})
        assert "SDL_Init" in result.data
"""

import pytest
from fastmcp.client.client import Client

from mcp_sdl.server import mcp


@pytest.fixture
async def client():
    """
    Client fixture for testing MCP tools.
    
    Provides a FastMCP Client instance connected to the server.
    Tests should use client.call_tool() to invoke tools, not direct function calls.
    """
    async with Client(mcp) as client:
        yield client
