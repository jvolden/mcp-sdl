"""MCP tools for SDL3 API reference queries."""

from ..api import SDL_CATEGORIES, SDL_FUNCTIONS
from ..api.sdl3 import CATEGORY_MODULES
from ..api.sdl3.categories import format_category_suggestions, get_category_list
from ..server import mcp


@mcp.tool
async def sdl_function_reference(function_name: str) -> str:
    """Get API reference documentation for a specific SDL3 function
    
    Args:
        function_name: Name of the SDL3 function (e.g., 'SDL_Init', 'SDL_CreateWindow')
    """
    func = SDL_FUNCTIONS.get(function_name)
    if not func:
        return format_category_suggestions(function_name)

    params = "\n".join([f"  - {p['name']} ({p['type']}): {p['description']}" for p in func["parameters"]])
    if not params:
        params = "  None"

    result = f"""# {function_name}

**Category:** {func['category']}

**Description:** {func['description']}

**Signature:**
```c
{func['signature']}
```

**Parameters:**
{params}

**Returns:** {func['returns']}
"""

    # Add optional fields if present
    if func.get('remarks'):
        result += f"\n**Remarks:** {func['remarks']}\n"

    if func.get('thread_safety'):
        result += f"\n**Thread Safety:** {func['thread_safety']}\n"

    result += f"""
**Example:**
```c
{func['example']}
```
"""

    if func.get('see_also'):
        result += "\n**See Also:**\n"
        for related in func['see_also']:
            result += f"- {related}\n"

    result += f"\n**Documentation:** https://wiki.libsdl.org/SDL3/{function_name}\n"

    return result


@mcp.tool
async def sdl_search_functions(query: str = "") -> str:
    """Search for SDL3 functions by category or keyword. Can also list all categories or get category overviews.
    
    Args:
        query: Search query, category name, or empty string to list all categories (e.g., 'window', 'init', 'render', '')
    """
    # If empty query, list all categories
    if not query or query.strip() == "":
        return get_category_list()

    query_lower = query.lower()

    # Check if it's an exact category match - return detailed overview
    if query_lower in CATEGORY_MODULES:
        return await _get_category_overview(query_lower)

    # Check if it's a category (list functions in that category)
    if query_lower in SDL_CATEGORIES:
        functions = SDL_CATEGORIES[query_lower]
        result = f"# SDL3 Functions in '{query}' category:\n\n"
        for func_name in functions:
            if func_name in SDL_FUNCTIONS:
                func = SDL_FUNCTIONS[func_name]
                result += f"- **{func_name}**: {func['description']}\n"
        return result

    # Search by keyword
    matches = []
    for func_name, func in SDL_FUNCTIONS.items():
        if (query_lower in func_name.lower() or
            query_lower in func['description'].lower() or
            query_lower in func['category'].lower()):
            matches.append((func_name, func))

    if matches:
        result = f"# SDL3 Functions matching '{query}':\n\n"
        for func_name, func in matches:
            result += f"- **{func_name}** ({func['category']}): {func['description']}\n"
        return result

    # No matches found - provide category suggestions
    return format_category_suggestions(query)


async def _get_category_overview(category: str) -> str:
    """Internal function to get an overview of SDL3 functionality by category.
    
    Args:
        category: Category name (e.g., 'init', 'video', 'render')
    """
    category_lower = category.lower()

    # Get module for category
    module = CATEGORY_MODULES.get(category_lower)
    if module and hasattr(module, 'OVERVIEW'):
        result = f"# SDL3 {category.title()} Category\n\n"

        # Add wiki URL if available
        if hasattr(module, 'WIKI_URL'):
            result += f"**Wiki:** {module.WIKI_URL}\n\n"

        result += f"{module.OVERVIEW}\n\n"

        # Add functions list
        if category_lower in SDL_CATEGORIES:
            result += "## Functions\n"
            for func_name in SDL_CATEGORIES[category_lower]:
                if func_name in SDL_FUNCTIONS:
                    func = SDL_FUNCTIONS[func_name]
                    result += f"- **{func_name}**: {func['description']}\n"

        # Add enums if available
        if hasattr(module, 'ENUMS') and module.ENUMS:
            result += "\n## Enums\n"
            for enum_name, enum_info in module.ENUMS.items():
                result += f"- **{enum_name}**: {enum_info['description']}\n"
                if 'values' in enum_info:
                    for value in enum_info['values']:
                        result += f"  - `{value['name']}`: {value['description']}\n"

        # Add datatypes if available
        if hasattr(module, 'DATATYPES') and module.DATATYPES:
            result += "\n## Datatypes\n"
            for type_name, type_info in module.DATATYPES.items():
                result += f"- **{type_name}**: {type_info['description']}\n"
                if 'values' in type_info:
                    for value in type_info['values']:
                        result += f"  - `{value['name']}`: {value['description']}\n"

        # Add macros if available
        if hasattr(module, 'MACROS') and module.MACROS:
            result += "\n## Macros\n"
            for macro_name, macro_info in module.MACROS.items():
                result += f"- **{macro_name}**: {macro_info['description']}\n"

        return result

    # Category not found - provide suggestions
    return format_category_suggestions()
