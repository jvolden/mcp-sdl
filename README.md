# MCP SDL3 Server

A Model Context Protocol (MCP) server that provides SDL3 API documentation, code examples, and reference information for AI assistants. Built with [FastMCP](https://github.com/jlowin/fastmcp) for a clean, maintainable codebase.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Quick Start](#quick-start)
- [Available Tools](#available-tools)
- [Usage with AI Assistants](#usage-with-ai-assistants)
- [Development](#development)
- [Contributing](#contributing)
  - [For AI-Assisted Development](#for-ai-assisted-development)
- [Resources](#resources)
- [License](#license)

## Features

- **SDL3 Function Reference**: Look up any SDL3 function with detailed API documentation
- **Function Search**: Search for functions by category or keyword  
- **Code Examples**: Get practical code examples for common SDL3 tasks
- **Complete Example Programs**: Browse and retrieve full working examples from examples.libsdl.org
- **Category Overviews**: Learn about SDL3 subsystems (video, audio, rendering, etc.)
- **Multi-language Support**: Examples available in C, C++, and other languages

## Installation

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager (see [installation guide](https://docs.astral.sh/uv/getting-started/installation/))

### Quick Start

Add to your AI assistant's MCP configuration:

```json
{
  "mcpServers": {
    "mcp-sdl": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/jvolden/mcp-sdl",
        "mcp-sdl"
      ]
    }
  }
}
```

Restart your AI assistant, and the SDL3 tools will be available.

## Available Tools

- **sdl_function_reference**
  - Get detailed API documentation for a specific SDL3 function
  - Inputs:
    - `function_name` (string, required): Name of the SDL3 function (e.g., "SDL_Init", "SDL_CreateWindow")
  - Returns complete function signature, parameters, description, and code example

- **sdl_search_functions**
  - Search for SDL3 functions by category or keyword
  - Inputs:
    - `query` (string, required): Search term or category name (e.g., "window", "audio", "render", "event")
  - Returns list of matching functions with descriptions

- **sdl_code_example**
  - Get practical code examples for common SDL3 tasks
  - Inputs:
    - `task` (string, required): Description of the task (e.g., "create window", "event loop", "render")
    - `language` (string, optional): Programming language (default: "c")
  - Returns complete working code example for the requested task

- **sdl_category_overview**
  - Get a comprehensive overview of SDL3 functionality by category
  - Inputs:
    - `category` (string, required): Category name (e.g., "initialization", "video", "audio", "rendering")
  - Returns overview of the category with key functions and concepts

- **sdl_list_categories**
  - List all available SDL3 API categories (both implemented and planned)
  - Returns comprehensive list of categories with descriptions and implementation status

- **sdl_list_example_categories**
  - List all available SDL3 example categories from examples.libsdl.org
  - Returns categories like "renderer", "audio", "input" with example counts

- **sdl_list_examples**
  - List all examples in a specific category
  - Inputs:
    - `category` (string, required): Category name (e.g., "renderer", "audio", "input")
  - Returns list of examples with titles, descriptions, and difficulty levels

- **sdl_get_example**
  - Get the complete source code for a specific SDL3 example
  - Inputs:
    - `category` (string, required): Category name (e.g., "renderer", "audio")
    - `example_id` (string, required): Example identifier (e.g., "01-clear", "06-textures")
  - Returns full working C source code with detailed comments

- **sdl_search_examples**
  - Search for SDL3 examples by keyword
  - Inputs:
    - `query` (string, required): Search term (e.g., "texture", "gamepad", "audio")
  - Returns matching examples across all categories

## Usage with AI Assistants

Once configured, AI assistants can use this server to:

1. **Look up SDL3 functions**: "What does SDL_CreateRenderer do?"
2. **Search for functions**: "Show me SDL3 functions for handling events"
3. **Get code examples**: "Give me an example of creating an SDL3 window"
4. **Learn about categories**: "Explain SDL3's rendering system"

The server provides accurate API documentation based on SDL3's official API.

## Development

```bash
# Clone and setup
git clone https://github.com/jvolden/mcp-sdl.git
cd mcp-sdl
uv sync

# Test the server
uv run mcp-sdl --help

# Run tests
uv run pytest

# Check test coverage
uv run pytest --cov --cov-report=term-missing

# Generate HTML coverage report
uv run pytest --cov --cov-report=html
# Open htmlcov/index.html in browser

# Lint code with ruff
uv run ruff check .

# Auto-fix linting issues
uv run ruff check --fix .

# Format code with ruff
uv run ruff format .
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

For AI-assisted contributions, use the **contributor** skill in VS Code with GitHub Copilot.

**Quick ways to contribute:**
- Add more SDL3 functions to the reference database
- Expand code examples for different languages
- Improve documentation and examples
- Report issues or suggest features

### For AI-Assisted Development

When using GitHub Copilot or other AI assistants in VS Code:

- Use **contributor** skill for general contribution guidance
- The **mcp-developer** skill automatically activates for any code changes
  - Ensures consistent module structure and patterns
  - Enforces 100% test coverage
  - Guides design decisions with trade-off analysis
  - Handles SDL3 API, examples, tests, and refactoring

See [`.github/skills/mcp-developer/`](.github/skills/mcp-developer/) for implementation patterns.

## Resources

- [SDL3 Official Documentation](https://wiki.libsdl.org/SDL3/)
- [SDL3 GitHub Repository](https://github.com/libsdl-org/SDL)
- [SDL3 Migration Guide](https://github.com/libsdl-org/SDL/blob/main/docs/README-migration.md)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [FastMCP Framework](https://github.com/jlowin/fastmcp)

## License

MIT License - See LICENSE file for details
