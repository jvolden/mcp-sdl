# Implementation Patterns

Detailed patterns and best practices for SDL3 category implementation.

## Design Decision Framework

When implementing something new:

1. **Identify options** - List 2-3 different approaches
2. **Analyze trade-offs** - For each option, explicitly state:
   - Pros (what it does well)
   - Cons (what it sacrifices) 
   - Impact on: maintainability, scalability, user experience, consistency
3. **Present options** - Show the analysis to the user
4. **Let user decide** - Or recommend with clear reasoning if choices are obvious

### Example Analysis

```
Option 1: Store examples inline in function definitions
  Pros: Single source of truth, no extra files
  Cons: Makes Python files longer, harder to diff
  
Option 2: Store examples in separate examples/ directory
  Pros: Cleaner separation, easier to update
  Cons: Harder to keep synchronized, more files to manage
  
Option 3: Generate examples from templates
  Pros: Consistency, reduced maintenance
  Cons: Less flexibility, added complexity
```

## Information Sourcing

**Primary source**: SDL3 wiki (wiki.libsdl.org/SDL3/)
- Most reliable and up-to-date
- Includes usage examples and best practices
- Consistent formatting and structure

**Fallback source**: SDL3 headers
- Use when wiki documentation is incomplete
- Extract function signatures and parameter types
- Look for comments that explain behavior

**Version handling**: Document current SDL3 API without version tracking. Add `"since": "SDL 3.x.y"` field if versioning becomes necessary.

## Quality Standards

### Testing Requirements

- **100% test coverage** for all new categories
- Add to `EXPECTED_CATEGORIES` in `tests/test_api_category_structure.py`
- Structural tests validate:
  - Module structure (category has all required constants)
  - Import paths work correctly
  - Function/enum/datatype definitions are well-formed
  - Category registration in discovery systems

### File Organization

- **One file per SDL item**: Function, enum, datatype, or macro gets its own file
- **Exact naming**: Match SDL3 documentation precisely
- **Category folders**: Use `category_{name}` with lowercase and underscores

### Content Standards

- **Examples**: Minimal viable demonstration, <10 lines preferred
- **Descriptions**: Clear and concise, focus on purpose not implementation
- **Type names**: Use SDL's official types (e.g., `SDL_bool`, `SDL_Window*`)
- **Deprecated items**: Include with `[DEPRECATED]` prefix in description

## Integration Points

### Category Catalog

Add new categories to `src/mcp_sdl/api/sdl3/categories.py`:

```python
IMPLEMENTED_CATEGORIES = {
    "init",
    "video", 
    # ... existing ...
    "new_category",  # Add here
}

SDL3_CATEGORY_CATALOG = {
    # ... existing ...
    "new_category": {
        "name": "Display Name",
        "description": "Brief description",
        "wiki": "https://wiki.libsdl.org/SDL3/CategoryNewCategory",
        "implemented": True,
    },
}
```

### MCP Tools

If adding functionality that needs MCP tool exposure:
- Edit `src/mcp_sdl/tools.py` for tool definitions
- Edit `src/mcp_sdl/server.py` for tool registration
- Follow existing FastMCP patterns (decorators, docstrings)

## Common Scenarios

### Large Categories

For categories with 50+ functions:
- Consider logical sub-groupings in documentation
- Maintain single category structure for consistency
- Focus on most commonly used functions first

### Overlapping Functionality

When functions could belong to multiple categories:
- Follow SDL3 wiki categorization
- Add cross-references in descriptions
- Avoid duplicating definitions

### Complex Data Structures

For structures with many fields:
- Document all public fields
- Note which fields are read-only
- Explain typical usage patterns
- Include lifecycle management notes