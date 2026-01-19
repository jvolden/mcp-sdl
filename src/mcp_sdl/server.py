"""Main MCP SDL3 server implementation - API Reference and Examples."""

import logging

from fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastMCP server
mcp = FastMCP("mcp-sdl")

# Import tool modules to register decorators
from . import tools  # noqa: F401, E402


def main() -> None:
    """MCP server entry point."""
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
