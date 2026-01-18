# Contributing to MCP SDL3 Server

Thank you for your interest in contributing to the MCP SDL3 Server project!

## AI Assistant Support

If you're using VS Code with GitHub Copilot, we provide skills for easier development:

1. **For general contributions**: The **contributor** skill guides you through:
   - Quick start and development setup
   - Project structure and organization
   - Testing requirements and coverage
   - Contribution workflow and best practices

2. **For any code changes**: The **mcp-developer** skill automatically guides you through:
   - Consistent module structure and naming conventions
   - Proper test coverage (100% required)
   - Design decision frameworks with trade-off analysis
   - File and folder organization patterns
   - Refactoring and update workflows

These skills ensure all changes follow project patterns and maintain quality standards.

**AI Resources**:
- Contributor skill: [`.github/skills/contributor/SKILL.md`](.github/skills/contributor/SKILL.md)
- MCP Developer skill: [`.github/skills/mcp-developer/SKILL.md`](.github/skills/mcp-developer/SKILL.md)

## Quick Start

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jvolden/mcp-sdl.git
   cd mcp-sdl
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Test the server**:
   ```bash
   uv run mcp-sdl --help
   ```

## Project Structure

```
mcp-sdl/
├── src/
│   └── mcp_sdl/
│       ├── server.py      # FastMCP server setup
│       ├── tools.py       # Tool implementations
│       └── api/           # SDL3 function database organized by category
├── .github/
│   ├── skills/
│   │   ├── contributor/   # Contributing guidance skill
│   │   └── mcp-developer/ # Development and code quality skill
│   └── copilot-instructions.md     # Project-wide guidelines
└── README.md
```

## Making Changes

### Adding SDL3 Functions

1. Update the appropriate category file in `api/` with the new function documentation
2. Test your changes: `uv run mcp-sdl --help`
3. Update documentation if needed

### Adding New Tools

1. Define the tool function in `tools.py` with type hints and docstring
2. Register it in `server.py` using `mcp.tool(your_function)`
3. Test the tool works correctly
4. Update the README's "Available Tools" section

## Development Guidelines

- **Keep it simple**: Follow FastMCP patterns (decorators, docstrings)
- **Type everything**: Use type hints for all parameters
- **Document clearly**: Tools use docstrings for schema generation
- **Test changes**: Run the server locally before submitting
- **100% test coverage required**: All new code must include comprehensive tests

### Testing

Run tests before submitting:

```bash
# Run all tests
uv run pytest

# Check test coverage
uv run pytest --cov --cov-report=term-missing

# Generate HTML coverage report for detailed analysis
uv run pytest --cov --cov-report=html
# Then open htmlcov/index.html in your browser
```

**Coverage Requirements**:
- Minimum: 95% overall coverage
- Goal: 100% coverage for all new code
- All new features require corresponding tests
- Tests should validate functionality and edge cases

## Contribution Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes following the guidelines
4. Test your changes locally
5. Commit with clear messages: `git commit -m "Add: description"`
6. Push to your fork: `git push origin feature/your-feature`
7. Open a Pull Request

## Getting Help

- Review existing code in `tools.py` for implementation patterns
- Use the **contributor** skill for AI-assisted guidance (optional)
- See [copilot-instructions.md](.github/copilot-instructions.md) for detailed project conventions
- Open an issue for questions or discussions

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the project and community

## License

By contributing, you agree that your contributions will be licensed under the same [MIT License](LICENSE) that covers this project.

---

**Note**: These guidelines are intentionally minimal and will expand as patterns emerge and best practices are established. For AI-assisted development, the **contributor** skill provides interactive, context-aware guidance.
