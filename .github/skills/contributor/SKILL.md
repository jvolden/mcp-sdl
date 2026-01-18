---
name: contributor
description: Guides external contributors through the MCP SDL3 Server contribution process. Use when someone wants to contribute to the project, add SDL3 functions, implement new features, or understand the contribution workflow. Covers quick start, project structure, testing requirements, and submission guidelines.
---

# Contributor Skill

Guides external contributors through the MCP SDL3 Server contribution workflow.

## Quick Start

1. Fork and clone the repository
2. Install dependencies: `uv sync`
3. Test the server: `uv run mcp-sdl --help`

## Making Contributions

### Adding SDL3 Functions
1. Update the appropriate category file in `api/` with new function documentation
2. Test changes: `uv run mcp-sdl --help`
3. Update documentation if needed

### Adding New Tools
1. Define the tool function in `tools.py` with type hints and docstring
2. Register it in `server.py` using `mcp.tool(your_function)`
3. Test the tool works correctly
4. Update the README's "Available Tools" section

## Testing

Run tests before submitting:
```bash
uv run pytest --cov --cov-report=term-missing
```

**Requirements**: 100% test coverage for all new code.

## Contribution Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Test your changes locally
5. Commit with clear messages: `git commit -m "Add: description"`
6. Push to your fork: `git push origin feature/your-feature`
7. Open a Pull Request

## Getting Help

- Review existing code in `tools.py` for implementation patterns
- See [copilot-instructions.md](../../copilot-instructions.md) for detailed project conventions
- Open an issue for questions or discussions

---

**Note**: For detailed implementation patterns and code quality standards, the AI will automatically use the **mcp-developer** skill when making code changes.
