"""MCP tools for SDL2 to SDL3 migration guides."""

from ..migration import get_all_headers, get_migration_data, search_migrations


async def sdl_migration_lookup(sdl2_name: str) -> str:
    """Find how to migrate a specific SDL2 function, constant, or type to SDL3.
    
    Args:
        sdl2_name: SDL2 symbol name (e.g., 'SDL_OpenAudio', 'SDL_INIT_VIDEO', 'SDL_AudioSpec')
    """
    results = search_migrations(sdl2_name)

    if not results:
        available_headers = ", ".join(get_all_headers())
        return f"No migration information found for '{sdl2_name}'.\n\nAvailable migration headers: {available_headers}\n\nUse `sdl_migration_header('SDL_xxx.h')` to browse a specific header."

    output = f"# Migration Guide for '{sdl2_name}'\n\n"
    output += f"Found in {len(results)} header(s):\n\n"

    for result in results:
        output += f"## {result['header']}\n\n"
        # Show first match with context, limit length
        first_match = result['matches'][0]
        if len(first_match) > 1000:
            first_match = first_match[:1000] + "\n...(truncated)"
        output += first_match + "\n\n"

        if len(result['matches']) > 1:
            output += f"(Plus {len(result['matches']) - 1} more match(es) in this header)\n\n"

        output += f"Use `sdl_migration_header('{result['header']}')` to see the complete migration guide.\n\n"

    return output


async def sdl_migration_header(header_name: str) -> str:
    """Get the complete SDL2 to SDL3 migration guide for a specific header file.
    
    Args:
        header_name: SDL2 header name (e.g., 'SDL_audio.h', 'SDL_render.h', 'SDL_video.h')
    """
    # Normalize header name
    if not header_name.endswith('.h'):
        header_name = f"{header_name}.h"

    if not header_name.startswith('SDL_'):
        header_name = f"SDL_{header_name}"

    data = get_migration_data(header_name)

    if not data:
        available = "\n".join([f"- {h}" for h in get_all_headers()])
        return f"Migration guide for '{header_name}' not found.\n\nAvailable headers:\n{available}"

    return data


async def sdl_migration_search(query: str) -> str:
    """Search across all SDL2 to SDL3 migration guides for functions, concepts, or changes.
    
    Args:
        query: Search term (e.g., 'callback', 'removed', 'renamed', 'bool')
    """
    results = search_migrations(query)

    if not results:
        return f"No results found for '{query}' in migration guides.\n\nUse `sdl_migration_header('SDL_xxx.h')` to browse specific headers."

    output = f"# Migration Search Results for '{query}'\n\n"
    output += f"Found matches in {len(results)} header(s):\n\n"

    for result in results:
        output += f"## {result['header']}\n\n"
        output += f"Found {len(result['matches'])} match(es):\n\n"

        # Show up to 3 matches per header
        for i, match in enumerate(result['matches'][:3]):
            if len(match) > 500:
                match = match[:500] + "...(truncated)"
            output += f"### Match {i + 1}\n```\n{match}\n```\n\n"

        if len(result['matches']) > 3:
            output += f"(Plus {len(result['matches']) - 3} more match(es) in this header)\n\n"

        output += f"Use `sdl_migration_header('{result['header']}')` to see the complete guide.\n\n"

    return output
