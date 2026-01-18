---
name: mcp-developer
description: Guides development, updates, and refactoring across the entire MCP server codebase. Use when adding features, updating categories, refactoring code, checking test coverage, or making any code changes. Enforces consistent patterns, 100% test coverage, and principled design decisions. Essential for maintaining code quality and preventing regressions during rapid development.
---

# MCP Developer

Guides technical implementation with consistent patterns and 100% test coverage.

## Core Requirements

- **100% test coverage** for all new features
- **Design decision analysis** - Present 2-3 options with trade-offs before implementing
- **Consistency over innovation** - Follow existing patterns unless compelling reason to diverge

## Adding New Category Workflow

1. Create `src/mcp_sdl/api/sdl3/category_{name}/`
2. Add to `IMPLEMENTED_CATEGORIES` in `categories.py`
3. Create `__init__.py` using category template (see references/templates.md)
4. Add item files using function/enum templates (see references/templates.md)
5. Add to `EXPECTED_CATEGORIES` in tests
6. Verify: `uv run pytest tests/test_api_category_structure.py -v`

## File Structure

```
category_{name}/
├── __init__.py           # Category aggregator
├── SDL_FunctionName.py   # One file per SDL item
```

## Naming Rules

- **Files**: Match SDL3 exactly (`SDL_FunctionName.py`)
- **Categories**: lowercase with underscores (`category_audio`)
- **Source**: SDL3 wiki primary, headers as fallback

## References

- [Code Templates](references/templates.md) - Category and item file templates
- [Implementation Patterns](references/patterns.md) - Detailed patterns and examples
