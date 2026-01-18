"""MCP tools for SDL3 examples and code snippets."""

from ..examples.sdl3 import CATEGORIES as EXAMPLE_CATEGORIES
from ..examples.sdl3 import EXAMPLES as SDL3_EXAMPLES


async def sdl_list_example_categories() -> str:
    """List all available SDL3 example categories.
    
    Returns categories like 'renderer', 'audio', 'input', etc. with descriptions.
    """
    result = "# SDL3 Example Categories\n\n"
    result += "Complete, working example programs from examples.libsdl.org:\n\n"

    for category, description in EXAMPLE_CATEGORIES.items():
        example_count = len(SDL3_EXAMPLES.get(category, {}))
        result += f"- **{category}**: {description} ({example_count} examples)\n"

    result += "\nUse `sdl_list_examples(category)` to see examples in a specific category.\n"
    return result


async def sdl_list_examples(category: str) -> str:
    """List all examples in a specific category.
    
    Args:
        category: Category name (e.g., 'renderer', 'audio', 'input')
    """
    category_lower = category.lower()

    if category_lower not in SDL3_EXAMPLES:
        available = ", ".join(EXAMPLE_CATEGORIES.keys())
        return f"Category '{category}' not found. Available categories: {available}"

    examples = SDL3_EXAMPLES[category_lower]
    result = f"# SDL3 {category.title()} Examples\n\n"
    result += f"{EXAMPLE_CATEGORIES[category_lower]}\n\n"

    for example_id, example_data in examples.items():
        result += f"- **{example_id}**: {example_data['title']}\n"
        result += f"  - {example_data['description']}\n"
        result += f"  - Difficulty: {example_data['difficulty']}\n"
        result += f"  - URL: {example_data['url']}\n\n"

    result += f"Use `sdl_get_example('{category_lower}', 'example-id')` to get the full source code.\n"
    return result


async def sdl_get_example(category: str, example_id: str) -> str:
    """Get the complete source code for a specific SDL3 example.
    
    Args:
        category: Category name (e.g., 'renderer', 'audio', 'input')
        example_id: Example identifier (e.g., '01-clear', '06-textures')
    """
    category_lower = category.lower()

    if category_lower not in SDL3_EXAMPLES:
        available = ", ".join(EXAMPLE_CATEGORIES.keys())
        return f"Category '{category}' not found. Available categories: {available}"

    examples = SDL3_EXAMPLES[category_lower]

    if example_id not in examples:
        available = ", ".join(examples.keys())
        return f"Example '{example_id}' not found in '{category}'. Available: {available}"

    example = examples[example_id]

    result = f"# {example['title']}\n\n"
    result += f"**Category:** {category}\n"
    result += f"**Difficulty:** {example['difficulty']}\n"
    result += f"**Description:** {example['description']}\n"
    result += f"**URL:** {example['url']}\n\n"
    result += "## Source Code\n\n"
    result += "```c\n"
    result += example['code']
    result += "\n```\n"

    return result


async def sdl_search_examples(query: str) -> str:
    """Search for SDL3 examples by keyword.
    
    Args:
        query: Search term (e.g., 'texture', 'audio', 'gamepad')
    """
    query_lower = query.lower()
    matches = []

    for category, examples in SDL3_EXAMPLES.items():
        for example_id, example_data in examples.items():
            if (query_lower in example_id.lower() or
                query_lower in example_data['title'].lower() or
                query_lower in example_data['description'].lower() or
                query_lower in category.lower()):
                matches.append((category, example_id, example_data))

    if not matches:
        return f"No examples found matching '{query}'. Use `sdl_list_example_categories()` to see all categories."

    result = f"# SDL3 Examples matching '{query}'\n\n"
    for category, example_id, example_data in matches:
        result += f"- **{category}/{example_id}**: {example_data['title']}\n"
        result += f"  - {example_data['description']}\n"
        result += f"  - Difficulty: {example_data['difficulty']}\n\n"

    result += "\nUse `sdl_get_example('category', 'example-id')` to get the full source code.\n"
    return result
