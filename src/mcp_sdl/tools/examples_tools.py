"""MCP tools for SDL3 examples and code snippets."""

from ..examples.sdl3 import CATEGORIES as EXAMPLE_CATEGORIES
from ..examples.sdl3 import EXAMPLES as SDL3_EXAMPLES
from ..server import mcp


@mcp.tool
async def sdl_examples(
    category: str | None = None,
    example_id: str | None = None,
    query: str | None = None,
) -> str:
    """Access SDL3 example code and documentation.
    
    Usage patterns:
    - No params: List all example categories
    - category only: List examples in that category
    - category + example_id: Get full source code for specific example
    - query only: Search examples by keyword
    
    Args:
        category: Category name (e.g., 'renderer', 'audio', 'input')
        example_id: Example identifier (e.g., '01-clear', '06-textures')
        query: Search term (e.g., 'texture', 'audio', 'gamepad')
    """
    # Search mode
    if query is not None:
        query_lower = query.lower()
        matches = []

        for cat, examples in SDL3_EXAMPLES.items():
            for ex_id, example_data in examples.items():
                if (query_lower in ex_id.lower() or
                    query_lower in example_data['title'].lower() or
                    query_lower in example_data['description'].lower() or
                    query_lower in cat.lower()):
                    matches.append((cat, ex_id, example_data))

        if not matches:
            return f"No examples found matching '{query}'. Try broader search terms."

        result = f"# SDL3 Examples matching '{query}'\n\n"
        for cat, ex_id, example_data in matches:
            result += f"- **{cat}/{ex_id}**: {example_data['title']}\n"
            result += f"  - {example_data['description']}\n"
            result += f"  - Difficulty: {example_data['difficulty']}\n\n"

        result += "\nTo get source code, call with category and example_id.\n"
        return result

    # Get specific example
    if category is not None and example_id is not None:
        category_lower = category.lower()

        if category_lower not in SDL3_EXAMPLES:
            available = ", ".join(EXAMPLE_CATEGORIES.keys())
            return f"Category '{category}' not found. Available: {available}"

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

        return str(result)

    # List examples in category
    if category is not None:
        category_lower = category.lower()

        if category_lower not in SDL3_EXAMPLES:
            available = ", ".join(EXAMPLE_CATEGORIES.keys())
            return f"Category '{category}' not found. Available: {available}"

        examples = SDL3_EXAMPLES[category_lower]
        result = f"# SDL3 {category.title()} Examples\n\n"
        result += f"{EXAMPLE_CATEGORIES[category_lower]}\n\n"

        for ex_id, example_data in examples.items():
            result += f"- **{ex_id}**: {example_data['title']}\n"
            result += f"  - {example_data['description']}\n"
            result += f"  - Difficulty: {example_data['difficulty']}\n"
            result += f"  - URL: {example_data['url']}\n\n"

        result += f"Call with category='{category_lower}' and example_id to get source code.\n"
        return result

    # List all categories (default)
    result = "# SDL3 Example Categories\n\n"
    result += "Complete, working example programs from examples.libsdl.org:\n\n"

    for cat, description in EXAMPLE_CATEGORIES.items():
        example_count = len(SDL3_EXAMPLES.get(cat, {}))
        result += f"- **{cat}**: {description} ({example_count} examples)\n"

    result += "\nCall with category parameter to see examples in a specific category.\n"
    return result
