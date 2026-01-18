"""Main MCP SDL3 server implementation - API Reference and Examples."""

import logging

from fastmcp import FastMCP

from .tools import (
    sdl_function_reference,
    sdl_get_example,
    sdl_list_example_categories,
    sdl_list_examples,
    sdl_migration_header,
    sdl_migration_lookup,
    sdl_migration_search,
    sdl_search_examples,
    sdl_search_functions,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastMCP server
mcp = FastMCP("mcp-sdl")

# Register tools
mcp.tool(sdl_function_reference)
mcp.tool(sdl_search_functions)
mcp.tool(sdl_list_example_categories)
mcp.tool(sdl_list_examples)
mcp.tool(sdl_get_example)
mcp.tool(sdl_search_examples)
mcp.tool(sdl_migration_lookup)
mcp.tool(sdl_migration_header)
mcp.tool(sdl_migration_search)


def main():
    """MCP server entry point."""
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
