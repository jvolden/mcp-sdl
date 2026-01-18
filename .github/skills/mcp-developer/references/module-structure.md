# SDL API Module Structure Reference

This document defines the structural patterns for SDL3 API implementation. It serves as the design reference—not a catalog of what exists.

## API Directory Pattern

```
src/mcp_sdl/api/
├── __init__.py
└── sdl3/
    ├── __init__.py
    ├── categories.py                      # Category catalog and discovery
    ├── category_{name}/                   # Pattern: One folder per SDL3 category
    │   ├── __init__.py                    # Category aggregator (required exports)
    │   ├── SDL_FunctionName.py           # One file per function
    │   ├── SDL_EnumName.py               # One file per enum
    │   ├── SDL_TypeName.py               # One file per datatype
    │   └── SDL_MACRO_NAME.py             # One file per macro
    └── category_{another}/                # Repeat pattern for each category
        ├── __init__.py
        ├── SDL_*.py
        └── ...
```

**Key principle**: Each SDL3 category gets its own folder. Each SDL3 item (function/enum/datatype/macro) gets its own file.

## Future MCP Structure

As the MCP server expands, the top-level structure will include:

```
src/mcp_sdl/
├── api/                    # SDL3 API documentation (this reference)
│   └── sdl3/              # Structured SDL3 API data
├── examples/              # Code examples and snippets (future)
├── migration/             # SDL2 to SDL3 migration help (future)
├── server.py              # MCP server implementation
├── tools.py               # MCP tool definitions
└── ...
```

This reference focuses on the `api/sdl3/` structure. Other directories follow their own patterns.

## Naming Conventions

### Category Folder Naming
- **Format**: `category_{name}`
- **Case**: All lowercase
- **Separator**: Underscore
- **Examples**: `category_init`, `category_video`, `category_render`

### Item File Naming
- **Format**: Exact SDL3 naming from official documentation
- **Case**: Preserve SDL's CamelCase (functions/types) or UPPER_CASE (macros)
- **Extension**: `.py`
- **Examples**:
  - Functions: `SDL_Init.py`, `SDL_CreateWindow.py`
  - Enums: `SDL_InitFlags.py`, `SDL_EventType.py`
  - Datatypes: `SDL_Window.py`, `SDL_Renderer.py`
  - Macros: `SDL_TOUCH_MOUSEID.py`, `SDL_MS_PER_SECOND.py`

### Category Module Exports

Each `category_{name}/__init__.py` must export:

```python
WIKI_URL: str           # SDL3 wiki category URL
OVERVIEW: str           # Multi-line category description
FUNCTIONS: dict         # {name: definition}
ENUMS: dict            # {name: definition}
DATATYPES: dict        # {name: definition}
MACROS: dict           # {name: definition}
CATEGORY: str          # Category key (without "category_" prefix)
FUNCTION_NAMES: list   # List of function names
ENUM_NAMES: list       # List of enum names
DATATYPE_NAMES: list   # List of datatype names
MACRO_NAMES: list      # List of macro names
```

### Item File Exports

Each item file exports a single dictionary:

- Function files: `FUNCTION = {name: {...}}`
- Enum files: `ENUM = {name: {...}}`
- Datatype files: `DATATYPE = {name: {...}}`
- Macro files: `MACRO = {name: {...}}`

## Import Chain

```
User/MCP Tool
    ↓
src/mcp_sdl/tools.py
    ↓
src/mcp_sdl/api/sdl3/__init__.py
    ↓
src/mcp_sdl/api/sdl3/category_{name}/__init__.py
    ↓
src/mcp_sdl/api/sdl3/category_{name}/SDL_Item.py
```

## Dynamic Discovery

The system uses dynamic imports to automatically discover all functions, enums, datatypes, and macros within each category:

```python
# In category_{name}/__init__.py
current_dir = Path(__file__).parent
module_files = [f.stem for f in current_dir.glob("*.py") if f.stem != "__init__"]

for module_name in module_files:
    module = importlib.import_module(f".{module_name}", package=__name__)
    if hasattr(module, "FUNCTION"):
        FUNCTIONS.update(module.FUNCTION)
    # ... repeat for ENUM, DATATYPE, MACRO
```

This means:
1. No manual registration of new items
2. Just create a properly formatted file in the category folder
3. It will be automatically discovered and included

## File Size Guidelines

- **Category __init__.py**: 30-80 lines (mostly boilerplate)
- **Function file**: 10-25 lines (definition + example)
- **Enum file**: 15-50 lines (depends on number of values)
- **Datatype file**: 15-40 lines (depends on field count)
- **Macro file**: 8-15 lines (simple definition + example)

## Test Structure

```
tests/
├── __init__.py
└── test_api_category_structure.py    # Structural validation tests
```

### Test Coverage

Tests verify:
- All expected categories exist and can be imported
- Each category has required module-level constants
- Category constants have correct types
- CATEGORY constant matches directory name
- Function/enum/datatype/macro dictionaries are properly formed
- Import paths work correctly

### Adding Category to Tests

When adding a new category, update `EXPECTED_CATEGORIES` in `tests/test_api_category_structure.py`:

```python
EXPECTED_CATEGORIES = {
    "init": "CategoryInit",
    # ... existing categories ...
    "{new_category}": "Category{NewCategory}",  # Add your new category
}
```

## Categories Catalog Structure

The `categories.py` file maintains two key structures:

### IMPLEMENTED_CATEGORIES (set)
Tracks which categories have implementation:
```python
IMPLEMENTED_CATEGORIES = {
    "category_key1",
    "category_key2",
    # Add new category keys here
}
```

### SDL3_CATEGORY_CATALOG (dict)
Complete catalog of all SDL3 categories (both implemented and planned):
```python
SDL3_CATEGORY_CATALOG = {
    "{category_key}": {
        "name": "Display Name",
        "description": "Brief description",
        "wiki": "https://wiki.libsdl.org/SDL3/Category{Name}",
        "implemented": True,  # or False for planned categories
    },
}
```

## Workflow Example: Adding a New Category

1. **Create directory**: `src/mcp_sdl/api/sdl3/category_{name}/`
2. **Create __init__.py**: Follow the category module pattern (see SKILL.md)
3. **Add to catalog**: Edit `categories.py`
   - Add `"{name}"` to `IMPLEMENTED_CATEGORIES`
   - Update `SDL3_CATEGORY_CATALOG["{name}"]["implemented"] = True`
4. **Add item files**: Create `SDL_*.py` files for functions/enums/datatypes/macros
5. **Update tests**: Add to `EXPECTED_CATEGORIES` in test file
6. **Verify**: Run `uv run pytest -v`

## Common SDL3 Patterns

### Boolean Returns
SDL3 functions typically return `bool`:
```python
"returns": "true on success, false on failure"
```

### Bitwise Flag Parameters
Use `|` operator for combining flags:
```python
"example": """SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO);"""
```

### Opaque Handle Types
SDL uses opaque pointers for most types:
```python
"SDL_Window": {
    "definition": "typedef struct SDL_Window SDL_Window;",
}
```

### Error Checking Pattern
Always demonstrate error handling:
```python
"example": """if (!SDL_Init(SDL_INIT_VIDEO)) {
    SDL_Log("Error: %s", SDL_GetError());
    return 1;
}"""
```

## Integration Points

### MCP Server
The API data integrates with the MCP server through:
- `src/mcp_sdl/tools.py` - Tool definitions that use the API data
- `src/mcp_sdl/server.py` - Server that exposes tools to MCP clients

### Testing
Module structure is validated by:
- `tests/test_api_category_structure.py` - Structural validation tests

When adding a category, update `EXPECTED_CATEGORIES` in the test file.

## Design Philosophy

This structure prioritizes:

1. **Discoverability** - Dynamic imports automatically find new items
2. **Git-friendliness** - One file per item creates clean diffs
3. **Maintainability** - Consistent patterns reduce cognitive load
4. **Isolation** - Changes to one function don't affect others
5. **Testability** - Structure can be validated programmatically

**This document describes patterns, not inventory**. You don't need to update this file when adding new categories or items—the patterns remain constant.
