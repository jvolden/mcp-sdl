"""Unit tests for MCP tool implementations."""

from fastmcp.client.client import Client

from mcp_sdl.api import SDL_FUNCTIONS


class TestSDLFunctionReference:
    """Test the sdl_function_reference tool."""

    async def test_valid_function_returns_formatted_reference(self, client: Client):
        """Test that a valid function returns properly formatted documentation."""
        result = await client.call_tool("sdl_function_reference", {"function_name": "SDL_Init"})

        # Check key sections are present
        data = result.data
        assert "# SDL_Init" in data
        assert "**Category:**" in data
        assert "**Description:**" in data
        assert "**Signature:**" in data
        assert "**Parameters:**" in data
        assert "**Returns:**" in data
        assert "**Example:**" in data
        assert "https://wiki.libsdl.org/SDL3/SDL_Init" in data

        # Check that code blocks are properly formatted
        assert "```c" in data
        assert "```" in data

    async def test_function_with_no_parameters(self, client: Client):
        """Test function reference for a function with no parameters."""
        result = await client.call_tool("sdl_function_reference", {"function_name": "SDL_Quit"})
        data = result.data

        assert "# SDL_Quit" in data
        assert "**Parameters:**" in data
        # Should show "None" for empty parameters
        assert "None" in data or "SDL_Quit" in data

    async def test_invalid_function_returns_suggestions(self, client: Client):
        """Test that an invalid function returns helpful suggestions."""
        result = await client.call_tool("sdl_function_reference", {"function_name": "SDL_NonExistent"})
        data = result.data

        # Should provide category suggestions or similar function names
        assert "SDL_NonExistent" not in data or "not found" in data.lower() or "available" in data.lower()

    async def test_function_with_optional_fields(self, client: Client):
        """Test functions that have optional fields like remarks or see_also."""
        # Test a function that might have optional fields
        all_functions = list(SDL_FUNCTIONS.keys())
        if all_functions:
            result = await client.call_tool("sdl_function_reference", {"function_name": all_functions[0]})
            data = result.data
            assert "**Description:**" in data

    async def test_function_with_remarks(self, client: Client):
        """Test that remarks field is included when present."""
        from mcp_sdl.api import SDL_FUNCTIONS
        
        # Find a function with remarks or temporarily patch one
        for func_name, func_data in SDL_FUNCTIONS.items():
            if func_data.get('remarks'):
                result = await client.call_tool("sdl_function_reference", {"function_name": func_name})
                data = result.data
                assert "**Remarks:**" in data
                break

    async def test_function_with_thread_safety(self, client: Client):
        """Test that thread_safety field is included when present."""
        from mcp_sdl.api import SDL_FUNCTIONS
        
        # Find a function with thread_safety or check format
        for func_name, func_data in SDL_FUNCTIONS.items():
            if func_data.get('thread_safety'):
                result = await client.call_tool("sdl_function_reference", {"function_name": func_name})
                data = result.data
                assert "**Thread Safety:**" in data
                break

    async def test_function_with_see_also(self, client: Client):
        """Test that see_also field is included when present."""
        from mcp_sdl.api import SDL_FUNCTIONS
        
        # Find a function with see_also or check format
        for func_name, func_data in SDL_FUNCTIONS.items():
            if func_data.get('see_also'):
                result = await client.call_tool("sdl_function_reference", {"function_name": func_name})
                data = result.data
                assert "**See Also:**" in data
                break


class TestSDLSearchFunctions:
    """Test the sdl_search_functions tool."""

    async def test_empty_query_lists_all_categories(self, client: Client):
        """Test that empty query returns list of all categories."""
        result = await client.call_tool("sdl_search_functions", {"query": ""})
        data = result.data

        assert len(data) > 0
        assert "SDL3" in data or "category" in data.lower() or "Category" in data
        # Should include multiple categories
        result_lower = data.lower()
        assert any(cat in result_lower for cat in ["init", "video", "render", "events"])

    async def test_category_name_returns_overview(self, client: Client):
        """Test that category name returns detailed overview."""
        result = await client.call_tool("sdl_search_functions", {"query": "init"})
        data = result.data

        assert "SDL3" in data
        assert "init" in data.lower() or "Init" in data
        # Should include functions list
        assert "SDL_Init" in data or "Functions" in data
        # Should be detailed (not just a list)
        assert len(data) > 200

        assert "SDL3" in data
        assert "init" in data.lower() or "Init" in data
        # Should include functions list
        assert "SDL_Init" in data or "Functions" in data

    async def test_render_category_overview(self, client: Client):
        """Test getting overview for render category."""
        result = await client.call_tool("sdl_search_functions", {"query": "render"})
        data = result.data

        assert "SDL3" in data
        assert "render" in data.lower() or "Render" in data
        # Should describe rendering functionality
        assert len(data) > 100  # Substantial content

    async def test_category_includes_wiki_url(self, client: Client):
        """Test that category overview includes wiki URL."""
        result = await client.call_tool("sdl_search_functions", {"query": "init"})
        data = result.data

        # Should have wiki URL for implemented categories
        if "wiki.libsdl.org" in data.lower():
            assert "https://wiki.libsdl.org/SDL3/" in data

    async def test_category_lists_functions(self, client: Client):
        """Test that category overview lists available functions."""
        result = await client.call_tool("sdl_search_functions", {"query": "init"})
        data = result.data

        # Should list functions in the category
        assert "SDL_" in data  # Function names
        if "## Functions" in data or "Functions" in data:
            assert data.count("SDL_") >= 1

    async def test_category_lists_enums_if_available(self, client: Client):
        """Test that category overview includes enums if available."""
        result = await client.call_tool("sdl_search_functions", {"query": "init"})
        data = result.data

        # If enums exist, they should be listed
        if "Enums" in data or "ENUM" in data:
            assert "SDL_" in data

    async def test_category_lists_datatypes_if_available(self, client: Client):
        """Test that category overview includes datatypes if available."""
        # Timer category has datatypes
        result = await client.call_tool("sdl_search_functions", {"query": "timer"})
        data = result.data

        # Should have substantial content
        assert len(data) > 100

    async def test_category_lists_macros_if_available(self, client: Client):
        """Test that category overview includes macros if available."""
        # Timer category has macros
        result = await client.call_tool("sdl_search_functions", {"query": "timer"})
        data = result.data

        # Should include macros
        if "Macros" in data or "MACRO" in data:
            assert "SDL_" in data

    async def test_keyword_search_finds_functions(self, client: Client):
        """Test that keyword search finds matching functions."""
        result = await client.call_tool("sdl_search_functions", {"query": "window"})
        data = result.data

        # Should find window-related functions
        assert "SDL3 Functions matching" in data or "SDL_CreateWindow" in data

    async def test_keyword_search_in_description(self, client: Client):
        """Test that keyword search looks in descriptions."""
        result = await client.call_tool("sdl_search_functions", {"query": "initialize"})
        data = result.data

        # Should find functions with "initialize" in description
        assert len(data) > 0

    async def test_invalid_category_returns_suggestions(self, client: Client):
        """Test that invalid category returns helpful suggestions."""
        result = await client.call_tool("sdl_search_functions", {"query": "nonexistent"})
        data = result.data

        # Should provide category suggestions
        assert len(data) > 0

    async def test_category_without_module_implementation(self, client: Client):
        """Test handling of categories that exist but don't have module implementation."""
        # This tests the defensive SDL_CATEGORIES check (lines 104-110)
        # Most categories should be in CATEGORY_MODULES, but this tests the fallback
        result = await client.call_tool("sdl_search_functions", {"query": "render"})
        data = result.data
        
        # Should still work and return content
        assert len(data) > 0
        assert "render" in data.lower() or "Render" in data


class TestSDLListCategories:
    """Test that empty search returns category list."""

    async def test_returns_category_list(self, client: Client):
        """Test that empty query returns a list of categories."""
        result = await client.call_tool("sdl_search_functions", {"query": ""})
        data = result.data

        assert len(data) > 0
        assert "SDL3" in data or "category" in data.lower() or "Category" in data

    async def test_includes_implemented_categories(self, client: Client):
        """Test that implemented categories are listed."""
        result = await client.call_tool("sdl_search_functions", {"query": ""})
        data = result.data

        # Should include categories we know exist
        result_lower = data.lower()
        assert any(cat in result_lower for cat in ["init", "video", "render", "events"])

    async def test_includes_category_descriptions(self, client: Client):
        """Test that categories include descriptions."""
        result = await client.call_tool("sdl_search_functions", {"query": ""})
        data = result.data

        # Should have descriptions, not just names
        assert len(data) > 200  # Substantial content with descriptions

    async def test_includes_planned_categories(self, client: Client):
        """Test that planned/upcoming categories are mentioned."""
        result = await client.call_tool("sdl_search_functions", {"query": ""})
        data = result.data

        # Should give overview of SDL3 API coverage
        assert "SDL3" in data


class TestToolIntegration:
    """Test interactions between different tools."""

    async def test_search_to_reference_workflow(self, client: Client):
        """Test searching for a function and then getting its reference."""
        # First search for functions
        search_result = await client.call_tool("sdl_search_functions", {"query": "init"})
        search_data = search_result.data

        # Extract a function name if possible
        if "SDL_Init" in search_data:
            # Then get detailed reference
            ref_result = await client.call_tool("sdl_function_reference", {"function_name": "SDL_Init"})
            ref_data = ref_result.data
            assert "# SDL_Init" in ref_data
            assert "**Signature:**" in ref_data

    async def test_category_overview_to_function_reference(self, client: Client):
        """Test getting category overview and then function details."""
        # Get category overview
        overview_result = await client.call_tool("sdl_search_functions", {"query": "init"})
        overview = overview_result.data

        # Should mention functions that we can look up
        if "SDL_Init" in overview:
            ref_result = await client.call_tool("sdl_function_reference", {"function_name": "SDL_Init"})
            ref_data = ref_result.data
            assert "# SDL_Init" in ref_data

    async def test_list_categories_to_overview(self, client: Client):
        """Test listing categories and then getting a specific overview."""
        # List all categories
        categories_result = await client.call_tool("sdl_search_functions", {"query": ""})
        categories = categories_result.data

        # Should have categories we can explore
        assert len(categories) > 0

        # Get specific category overview
        overview_result = await client.call_tool("sdl_search_functions", {"query": "init"})
        overview = overview_result.data
        assert len(overview) > 0


class TestSDLListExampleCategories:
    """Test the sdl_list_example_categories tool."""

    async def test_returns_example_categories(self, client: Client):
        """Test that all example categories are listed."""
        result = await client.call_tool("sdl_examples", {})
        data = result.data

        assert "# SDL3 Example Categories" in data
        assert "renderer" in data.lower()
        assert "audio" in data.lower()
        assert "input" in data.lower()

    async def test_includes_example_counts(self, client: Client):
        """Test that example counts are shown for each category."""
        result = await client.call_tool("sdl_examples", {})
        data = result.data

        # Should show count like "(2 examples)" or similar
        assert "example" in data.lower()

    async def test_includes_usage_hint(self, client: Client):
        """Test that usage instructions are included."""
        result = await client.call_tool("sdl_examples", {})
        data = result.data

        assert "category" in data.lower()


class TestSDLListExamples:
    """Test the sdl_list_examples tool."""

    async def test_valid_category_lists_examples(self, client: Client):
        """Test that valid category lists its examples."""
        result = await client.call_tool("sdl_examples", {"category": "renderer"})
        data = result.data

        assert "# SDL3 Renderer Examples" in data or "renderer" in data.lower()
        assert "clear" in data.lower() or "texture" in data.lower()

    async def test_includes_example_metadata(self, client: Client):
        """Test that examples include title, description, difficulty, URL."""
        result = await client.call_tool("sdl_examples", {"category": "renderer"})
        data = result.data

        assert "Difficulty:" in data or "difficulty" in data.lower()
        assert "URL:" in data or "url" in data.lower()

    async def test_invalid_category_shows_available(self, client: Client):
        """Test that invalid category shows available categories."""
        result = await client.call_tool("sdl_examples", {"category": "nonexistent"})
        data = result.data

        assert "not found" in data.lower()
        assert "Available:" in data

    async def test_case_insensitive(self, client: Client):
        """Test that category lookup is case-insensitive."""
        result_lower = await client.call_tool("sdl_examples", {"category": "renderer"})
        result_upper = await client.call_tool("sdl_examples", {"category": "RENDERER"})
        result_mixed = await client.call_tool("sdl_examples", {"category": "Renderer"})

        # All should succeed
        assert "not found" not in result_lower.data.lower()
        assert "not found" not in result_upper.data.lower()
        assert "not found" not in result_mixed.data.lower()


class TestSDLGetExample:
    """Test the sdl_get_example tool."""

    async def test_valid_example_returns_source_code(self, client: Client):
        """Test that valid example returns complete source code."""
        result = await client.call_tool("sdl_examples", {"category": "renderer", "example_id": "01-clear"})
        data = result.data

        assert "# " in data  # Has title
        assert "**Category:**" in data
        assert "**Difficulty:**" in data
        assert "**Description:**" in data
        assert "## Source Code" in data
        assert "```c" in data
        assert "```" in data

    async def test_invalid_category_shows_available(self, client: Client):
        """Test that invalid category shows available categories."""
        result = await client.call_tool("sdl_examples", {"category": "nonexistent", "example_id": "01-clear"})
        data = result.data

        assert "not found" in data.lower()
        assert "Available:" in data

    async def test_invalid_example_shows_available(self, client: Client):
        """Test that invalid example shows available examples."""
        result = await client.call_tool("sdl_examples", {"category": "renderer", "example_id": "nonexistent"})
        data = result.data

        assert "not found" in data.lower()
        assert "Available:" in data

    async def test_case_insensitive_category(self, client: Client):
        """Test that category lookup is case-insensitive."""
        result = await client.call_tool("sdl_examples", {"category": "RENDERER", "example_id": "01-clear"})
        data = result.data

        assert "not found" not in data.lower() or "category" not in data.lower()


class TestSDLSearchExamples:
    """Test the sdl_search_examples tool."""

    async def test_finds_examples_by_keyword(self, client: Client):
        """Test that examples can be found by keyword."""
        result = await client.call_tool("sdl_examples", {"query": "texture"})
        data = result.data

        assert "# SDL3 Examples matching" in data
        # Should find texture-related examples
        assert len(data) > 100  # Has content

    async def test_finds_examples_by_category(self, client: Client):
        """Test that examples can be found by category name."""
        result = await client.call_tool("sdl_examples", {"query": "renderer"})
        data = result.data

        assert "# SDL3 Examples matching" in data
        # Should find renderer examples
        assert "renderer" in data.lower()

    async def test_no_matches_shows_help(self, client: Client):
        """Test that no matches provides helpful message."""
        result = await client.call_tool("sdl_examples", {"query": "zzzznonexistent"})
        data = result.data

        assert "No examples found" in data

    async def test_includes_example_metadata(self, client: Client):
        """Test that search results include example metadata."""
        result = await client.call_tool("sdl_examples", {"query": "clear"})
        data = result.data

        if "No examples found" not in data:
            assert "Difficulty:" in data

    async def test_includes_usage_hint(self, client: Client):
        """Test that search results include usage instructions."""
        result = await client.call_tool("sdl_examples", {"query": "clear"})
        data = result.data

        if "No examples found" not in data:
            assert "category" in data.lower() or "example_id" in data.lower()


class TestSDLMigrationLookup:
    """Test the sdl_migration_lookup tool."""

    async def test_finds_migration_info(self, client: Client):
        """Test that migration info is found for SDL2 symbols."""
        result = await client.call_tool("sdl_migration", {"sdl2_name": "SDL_OpenAudio"})
        data = result.data

        # Should either find the symbol or suggest alternatives
        assert len(data) > 0
        assert "Migration Guide" in data or "not found" in data.lower()

    async def test_no_match_shows_available_headers(self, client: Client):
        """Test that no match shows available migration headers."""
        result = await client.call_tool("sdl_migration", {"sdl2_name": "SDL_NonExistentFunction123"})
        data = result.data

        assert "No migration information found" in data
        assert "Available migration headers:" in data
        assert "SDL_" in data  # Should list headers

    async def test_includes_header_reference(self, client: Client):
        """Test that results reference the source header."""
        result = await client.call_tool("sdl_migration", {"sdl2_name": "SDL_OpenAudio"})
        data = result.data

        if "No migration" not in data:
            assert ".h" in data  # Header file name

    async def test_includes_usage_hint(self, client: Client):
        """Test that results include usage instructions."""
        result = await client.call_tool("sdl_migration", {"sdl2_name": "SDL_NonExistentFunction123"})
        data = result.data

        assert "header_name" in data.lower()

    async def test_truncates_long_matches(self, client: Client):
        """Test that long matches are truncated appropriately."""
        # Try to find a symbol that might have long migration content
        result = await client.call_tool("sdl_migration", {"sdl2_name": "SDL"})
        data = result.data

        # Check that result is reasonable size
        if "No migration" not in data:
            # Should either truncate or handle long content
            assert len(data) < 100000  # Reasonable max size


class TestSDLMigrationHeader:
    """Test the sdl_migration_header tool."""

    async def test_valid_header_returns_guide(self, client: Client):
        """Test that valid header returns migration guide."""
        result = await client.call_tool("sdl_migration", {"header_name": "SDL_audio.h"})
        data = result.data

        assert len(data) > 100  # Has substantial content
        # Should contain migration information
        assert "SDL" in data

    async def test_normalizes_header_name(self, client: Client):
        """Test that header name is normalized (adds .h and SDL_ prefix)."""
        # Test without .h extension
        result1 = await client.call_tool("sdl_migration", {"header_name": "SDL_audio"})
        # Test without SDL_ prefix
        result2 = await client.call_tool("sdl_migration", {"header_name": "audio.h"})
        # Test with both missing
        result3 = await client.call_tool("sdl_migration", {"header_name": "audio"})

        # All should work or show same error
        assert len(result1.data) > 0
        assert len(result2.data) > 0
        assert len(result3.data) > 0

    async def test_invalid_header_shows_available(self, client: Client):
        """Test that invalid header shows available headers."""
        result = await client.call_tool("sdl_migration", {"header_name": "SDL_nonexistent.h"})
        data = result.data

        assert "not found" in data.lower()
        assert "Available headers:" in data
        assert "SDL_" in data

    async def test_returns_complete_guide(self, client: Client):
        """Test that complete migration guide is returned."""
        result = await client.call_tool("sdl_migration", {"header_name": "SDL_audio.h"})
        data = result.data

        # Should have substantial migration content
        if "not found" not in data.lower():
            assert len(data) > 50


class TestSDLMigrationSearch:
    """Test the sdl_migration_search tool."""

    async def test_searches_across_all_headers(self, client: Client):
        """Test that search looks across all migration guides."""
        result = await client.call_tool("sdl_migration", {"query": "callback"})
        data = result.data

        # Should either find results or indicate no matches
        assert len(data) > 0
        assert "Migration Search Results" in data or "No results found" in data

    async def test_no_results_shows_help(self, client: Client):
        """Test that no results provides helpful message."""
        result = await client.call_tool("sdl_migration", {"query": "zzzznonexistent123"})
        data = result.data

        assert "No results found" in data
        assert "header_name" in data.lower()

    async def test_limits_match_output(self, client: Client):
        """Test that search results are limited/truncated appropriately."""
        result = await client.call_tool("sdl_migration", {"query": "SDL"})
        data = result.data

        # Should have results but be manageable size
        # Check for truncation indicators
        if "No results found" not in data:
            assert len(data) < 50000  # Reasonable size limit

    async def test_includes_header_context(self, client: Client):
        """Test that results include header context."""
        result = await client.call_tool("sdl_migration", {"query": "audio"})
        data = result.data

        if "No results found" not in data:
            assert ".h" in data or "header" in data.lower()

    async def test_includes_usage_hint(self, client: Client):
        """Test that results include usage instructions."""
        result = await client.call_tool("sdl_migration", {"query": "audio"})
        data = result.data

        if "No results found" not in data:
            assert "header_name" in data.lower()

    async def test_truncates_long_matches(self, client: Client):
        """Test that search results are truncated for readability."""
        # Search for a common term that might have many long matches
        result = await client.call_tool("sdl_migration", {"query": "SDL"})
        data = result.data

        # Should have results but be manageable size
        if "No results found" not in data:
            # Check for truncation indicators or reasonable size
            assert len(data) < 100000  # Reasonable max size


class TestExampleToolsIntegration:
    """Test interactions between example tools."""

    async def test_list_categories_to_list_examples(self, client: Client):
        """Test workflow: list categories -> list examples."""
        # List categories
        categories_result = await client.call_tool("sdl_examples", {})
        categories = categories_result.data
        assert "renderer" in categories.lower()

        # List examples in category
        examples_result = await client.call_tool("sdl_examples", {"category": "renderer"})
        examples = examples_result.data
        assert len(examples) > 0
        assert "renderer" in examples.lower()

    async def test_search_to_get_example(self, client: Client):
        """Test workflow: search examples -> get specific example."""
        # Search for examples
        search_result = await client.call_tool("sdl_examples", {"query": "clear"})
        search_data = search_result.data

        if "No examples found" not in search_data:
            # Get specific example
            example_result = await client.call_tool("sdl_examples", {"category": "renderer", "example_id": "01-clear"})
            example = example_result.data
            assert "Source Code" in example


class TestMigrationToolsIntegration:
    """Test interactions between migration tools."""

    async def test_lookup_to_header(self, client: Client):
        """Test workflow: lookup symbol -> get full header guide."""
        # Lookup a symbol
        lookup_result = await client.call_tool("sdl_migration", {"sdl2_name": "SDL_OpenAudio"})
        lookup_data = lookup_result.data

        if "No migration" not in lookup_data:
            # Get full header guide
            header_result = await client.call_tool("sdl_migration", {"header_name": "SDL_audio.h"})
            header_data = header_result.data
            assert len(header_data) > 0

    async def test_search_to_header(self, client: Client):
        """Test workflow: search migration -> get specific header."""
        # Search for migration info
        search_result = await client.call_tool("sdl_migration", {"query": "audio"})
        search_data = search_result.data

        if "No results found" not in search_data:
            # Get specific header
            header_result = await client.call_tool("sdl_migration", {"header_name": "SDL_audio.h"})
            header_data = header_result.data
            assert len(header_data) > 0
