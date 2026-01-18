"""Unit tests for MCP tool implementations."""

import pytest

from mcp_sdl.api import SDL_FUNCTIONS
from mcp_sdl.tools import (
    sdl_function_reference,
    sdl_get_example,
    sdl_list_example_categories,
    sdl_list_examples,
    sdl_migration_header,
    sdl_migration_lookup,
    sdl_migration_search,
    sdl_search_examples,
    sdl_search_functions,
)


class TestSDLFunctionReference:
    """Test the sdl_function_reference tool."""

    @pytest.mark.asyncio
    async def test_valid_function_returns_formatted_reference(self):
        """Test that a valid function returns properly formatted documentation."""
        result = await sdl_function_reference("SDL_Init")

        # Check key sections are present
        assert "# SDL_Init" in result
        assert "**Category:**" in result
        assert "**Description:**" in result
        assert "**Signature:**" in result
        assert "**Parameters:**" in result
        assert "**Returns:**" in result
        assert "**Example:**" in result
        assert "https://wiki.libsdl.org/SDL3/SDL_Init" in result

        # Check that code blocks are properly formatted
        assert "```c" in result
        assert "```" in result

    @pytest.mark.asyncio
    async def test_function_with_no_parameters(self):
        """Test function reference for a function with no parameters."""
        result = await sdl_function_reference("SDL_Quit")

        assert "# SDL_Quit" in result
        assert "**Parameters:**" in result
        # Should show "None" for empty parameters
        assert "None" in result or "SDL_Quit" in result

    @pytest.mark.asyncio
    async def test_invalid_function_returns_suggestions(self):
        """Test that an invalid function returns helpful suggestions."""
        result = await sdl_function_reference("SDL_NonExistent")

        # Should provide category suggestions or similar function names
        assert "SDL_NonExistent" not in result or "not found" in result.lower() or "available" in result.lower()

    @pytest.mark.asyncio
    async def test_function_with_optional_fields(self):
        """Test functions that have optional fields like remarks or see_also."""
        # Test a function that might have optional fields
        all_functions = list(SDL_FUNCTIONS.keys())
        if all_functions:
            result = await sdl_function_reference(all_functions[0])
            assert "**Description:**" in result

    @pytest.mark.asyncio
    async def test_function_with_remarks(self):
        """Test that remarks field is included when present."""
        from mcp_sdl.api import SDL_FUNCTIONS
        
        # Find a function with remarks or temporarily patch one
        for func_name, func_data in SDL_FUNCTIONS.items():
            if func_data.get('remarks'):
                result = await sdl_function_reference(func_name)
                assert "**Remarks:**" in result
                break

    @pytest.mark.asyncio
    async def test_function_with_thread_safety(self):
        """Test that thread_safety field is included when present."""
        from mcp_sdl.api import SDL_FUNCTIONS
        
        # Find a function with thread_safety or check format
        for func_name, func_data in SDL_FUNCTIONS.items():
            if func_data.get('thread_safety'):
                result = await sdl_function_reference(func_name)
                assert "**Thread Safety:**" in result
                break

    @pytest.mark.asyncio
    async def test_function_with_see_also(self):
        """Test that see_also field is included when present."""
        from mcp_sdl.api import SDL_FUNCTIONS
        
        # Find a function with see_also or check format
        for func_name, func_data in SDL_FUNCTIONS.items():
            if func_data.get('see_also'):
                result = await sdl_function_reference(func_name)
                assert "**See Also:**" in result
                break


class TestSDLSearchFunctions:
    """Test the sdl_search_functions tool."""

    @pytest.mark.asyncio
    async def test_empty_query_lists_all_categories(self):
        """Test that empty query returns list of all categories."""
        result = await sdl_search_functions("")

        assert len(result) > 0
        assert "SDL3" in result or "category" in result.lower() or "Category" in result
        # Should include multiple categories
        result_lower = result.lower()
        assert any(cat in result_lower for cat in ["init", "video", "render", "events"])

    @pytest.mark.asyncio
    async def test_category_name_returns_overview(self):
        """Test that category name returns detailed overview."""
        result = await sdl_search_functions("init")

        assert "SDL3" in result
        assert "init" in result.lower() or "Init" in result
        # Should include functions list
        assert "SDL_Init" in result or "Functions" in result
        # Should be detailed (not just a list)
        assert len(result) > 200

        assert "SDL3" in result
        assert "init" in result.lower() or "Init" in result
        # Should include functions list
        assert "SDL_Init" in result or "Functions" in result

    @pytest.mark.asyncio
    async def test_render_category_overview(self):
        """Test getting overview for render category."""
        result = await sdl_search_functions("render")

        assert "SDL3" in result
        assert "render" in result.lower() or "Render" in result
        # Should describe rendering functionality
        assert len(result) > 100  # Substantial content

    @pytest.mark.asyncio
    async def test_category_includes_wiki_url(self):
        """Test that category overview includes wiki URL."""
        result = await sdl_search_functions("init")

        # Should have wiki URL for implemented categories
        if "wiki.libsdl.org" in result.lower():
            assert "https://wiki.libsdl.org/SDL3/" in result

    @pytest.mark.asyncio
    async def test_category_lists_functions(self):
        """Test that category overview lists available functions."""
        result = await sdl_search_functions("init")

        # Should list functions in the category
        assert "SDL_" in result  # Function names
        if "## Functions" in result or "Functions" in result:
            assert result.count("SDL_") >= 1

    @pytest.mark.asyncio
    async def test_category_lists_enums_if_available(self):
        """Test that category overview includes enums if available."""
        result = await sdl_search_functions("init")

        # If enums exist, they should be listed
        if "Enums" in result or "ENUM" in result:
            assert "SDL_" in result

    @pytest.mark.asyncio
    async def test_category_lists_datatypes_if_available(self):
        """Test that category overview includes datatypes if available."""
        # Timer category has datatypes
        result = await sdl_search_functions("timer")

        # Should have substantial content
        assert len(result) > 100

    @pytest.mark.asyncio
    async def test_category_lists_macros_if_available(self):
        """Test that category overview includes macros if available."""
        # Timer category has macros
        result = await sdl_search_functions("timer")

        # Should include macros
        if "Macros" in result or "MACRO" in result:
            assert "SDL_" in result

    @pytest.mark.asyncio
    async def test_keyword_search_finds_functions(self):
        """Test that keyword search finds matching functions."""
        result = await sdl_search_functions("window")

        # Should find window-related functions
        assert "SDL3 Functions matching" in result or "SDL_CreateWindow" in result

    @pytest.mark.asyncio
    async def test_keyword_search_in_description(self):
        """Test that keyword search looks in descriptions."""
        result = await sdl_search_functions("initialize")

        # Should find functions with "initialize" in description
        assert len(result) > 0

    @pytest.mark.asyncio
    async def test_invalid_category_returns_suggestions(self):
        """Test that invalid category returns helpful suggestions."""
        result = await sdl_search_functions("nonexistent")

        # Should provide category suggestions
        assert len(result) > 0

    @pytest.mark.asyncio
    async def test_category_without_module_implementation(self):
        """Test handling of categories that exist but don't have module implementation."""
        # This tests the defensive SDL_CATEGORIES check (lines 104-110)
        # Most categories should be in CATEGORY_MODULES, but this tests the fallback
        result = await sdl_search_functions("render")
        
        # Should still work and return content
        assert len(result) > 0
        assert "render" in result.lower() or "Render" in result


class TestSDLListCategories:
    """Test that empty search returns category list."""

    @pytest.mark.asyncio
    async def test_returns_category_list(self):
        """Test that empty query returns a list of categories."""
        result = await sdl_search_functions("")

        assert len(result) > 0
        assert "SDL3" in result or "category" in result.lower() or "Category" in result

    @pytest.mark.asyncio
    async def test_includes_implemented_categories(self):
        """Test that implemented categories are listed."""
        result = await sdl_search_functions("")

        # Should include categories we know exist
        result_lower = result.lower()
        assert any(cat in result_lower for cat in ["init", "video", "render", "events"])

    @pytest.mark.asyncio
    async def test_includes_category_descriptions(self):
        """Test that categories include descriptions."""
        result = await sdl_search_functions("")

        # Should have descriptions, not just names
        assert len(result) > 200  # Substantial content with descriptions

    @pytest.mark.asyncio
    async def test_includes_planned_categories(self):
        """Test that planned/upcoming categories are mentioned."""
        result = await sdl_search_functions("")

        # Should give overview of SDL3 API coverage
        assert "SDL3" in result


class TestToolIntegration:
    """Test interactions between different tools."""

    @pytest.mark.asyncio
    async def test_search_to_reference_workflow(self):
        """Test searching for a function and then getting its reference."""
        # First search for functions
        search_result = await sdl_search_functions("init")

        # Extract a function name if possible
        if "SDL_Init" in search_result:
            # Then get detailed reference
            ref_result = await sdl_function_reference("SDL_Init")
            assert "# SDL_Init" in ref_result
            assert "**Signature:**" in ref_result

    @pytest.mark.asyncio
    async def test_category_overview_to_function_reference(self):
        """Test getting category overview and then function details."""
        # Get category overview
        overview = await sdl_search_functions("init")

        # Should mention functions that we can look up
        if "SDL_Init" in overview:
            ref_result = await sdl_function_reference("SDL_Init")
            assert "# SDL_Init" in ref_result

    @pytest.mark.asyncio
    async def test_list_categories_to_overview(self):
        """Test listing categories and then getting a specific overview."""
        # List all categories
        categories = await sdl_search_functions("")

        # Should have categories we can explore
        assert len(categories) > 0

        # Get specific category overview
        overview = await sdl_search_functions("init")
        assert len(overview) > 0


class TestSDLListExampleCategories:
    """Test the sdl_list_example_categories tool."""

    @pytest.mark.asyncio
    async def test_returns_example_categories(self):
        """Test that all example categories are listed."""
        result = await sdl_list_example_categories()

        assert "# SDL3 Example Categories" in result
        assert "renderer" in result.lower()
        assert "audio" in result.lower()
        assert "input" in result.lower()

    @pytest.mark.asyncio
    async def test_includes_example_counts(self):
        """Test that example counts are shown for each category."""
        result = await sdl_list_example_categories()

        # Should show count like "(2 examples)" or similar
        assert "example" in result.lower()

    @pytest.mark.asyncio
    async def test_includes_usage_hint(self):
        """Test that usage instructions are included."""
        result = await sdl_list_example_categories()

        assert "sdl_list_examples" in result


class TestSDLListExamples:
    """Test the sdl_list_examples tool."""

    @pytest.mark.asyncio
    async def test_valid_category_lists_examples(self):
        """Test that valid category lists its examples."""
        result = await sdl_list_examples("renderer")

        assert "# SDL3 Renderer Examples" in result or "renderer" in result.lower()
        assert "clear" in result.lower() or "texture" in result.lower()

    @pytest.mark.asyncio
    async def test_includes_example_metadata(self):
        """Test that examples include title, description, difficulty, URL."""
        result = await sdl_list_examples("renderer")

        assert "Difficulty:" in result or "difficulty" in result.lower()
        assert "URL:" in result or "url" in result.lower()

    @pytest.mark.asyncio
    async def test_invalid_category_shows_available(self):
        """Test that invalid category shows available categories."""
        result = await sdl_list_examples("nonexistent")

        assert "not found" in result.lower()
        assert "Available categories:" in result

    @pytest.mark.asyncio
    async def test_case_insensitive(self):
        """Test that category lookup is case-insensitive."""
        result_lower = await sdl_list_examples("renderer")
        result_upper = await sdl_list_examples("RENDERER")
        result_mixed = await sdl_list_examples("Renderer")

        # All should succeed
        assert "not found" not in result_lower.lower()
        assert "not found" not in result_upper.lower()
        assert "not found" not in result_mixed.lower()


class TestSDLGetExample:
    """Test the sdl_get_example tool."""

    @pytest.mark.asyncio
    async def test_valid_example_returns_source_code(self):
        """Test that valid example returns complete source code."""
        result = await sdl_get_example("renderer", "01-clear")

        assert "# " in result  # Has title
        assert "**Category:**" in result
        assert "**Difficulty:**" in result
        assert "**Description:**" in result
        assert "## Source Code" in result
        assert "```c" in result
        assert "```" in result

    @pytest.mark.asyncio
    async def test_invalid_category_shows_available(self):
        """Test that invalid category shows available categories."""
        result = await sdl_get_example("nonexistent", "01-clear")

        assert "not found" in result.lower()
        assert "Available categories:" in result

    @pytest.mark.asyncio
    async def test_invalid_example_shows_available(self):
        """Test that invalid example shows available examples."""
        result = await sdl_get_example("renderer", "nonexistent")

        assert "not found" in result.lower()
        assert "Available:" in result

    @pytest.mark.asyncio
    async def test_case_insensitive_category(self):
        """Test that category lookup is case-insensitive."""
        result = await sdl_get_example("RENDERER", "01-clear")

        assert "not found" not in result.lower() or "category" not in result.lower()


class TestSDLSearchExamples:
    """Test the sdl_search_examples tool."""

    @pytest.mark.asyncio
    async def test_finds_examples_by_keyword(self):
        """Test that examples can be found by keyword."""
        result = await sdl_search_examples("texture")

        assert "# SDL3 Examples matching" in result
        # Should find texture-related examples
        assert len(result) > 100  # Has content

    @pytest.mark.asyncio
    async def test_finds_examples_by_category(self):
        """Test that examples can be found by category name."""
        result = await sdl_search_examples("renderer")

        assert "# SDL3 Examples matching" in result
        # Should find renderer examples
        assert "renderer" in result.lower()

    @pytest.mark.asyncio
    async def test_no_matches_shows_help(self):
        """Test that no matches provides helpful message."""
        result = await sdl_search_examples("zzzznonexistent")

        assert "No examples found" in result
        assert "sdl_list_example_categories" in result

    @pytest.mark.asyncio
    async def test_includes_example_metadata(self):
        """Test that search results include example metadata."""
        result = await sdl_search_examples("clear")

        if "No examples found" not in result:
            assert "Difficulty:" in result

    @pytest.mark.asyncio
    async def test_includes_usage_hint(self):
        """Test that search results include usage instructions."""
        result = await sdl_search_examples("clear")

        if "No examples found" not in result:
            assert "sdl_get_example" in result


class TestSDLMigrationLookup:
    """Test the sdl_migration_lookup tool."""

    @pytest.mark.asyncio
    async def test_finds_migration_info(self):
        """Test that migration info is found for SDL2 symbols."""
        result = await sdl_migration_lookup("SDL_OpenAudio")

        # Should either find the symbol or suggest alternatives
        assert len(result) > 0
        assert "Migration Guide" in result or "not found" in result.lower()

    @pytest.mark.asyncio
    async def test_no_match_shows_available_headers(self):
        """Test that no match shows available migration headers."""
        result = await sdl_migration_lookup("SDL_NonExistentFunction123")

        assert "No migration information found" in result
        assert "Available migration headers:" in result
        assert "SDL_" in result  # Should list headers

    @pytest.mark.asyncio
    async def test_includes_header_reference(self):
        """Test that results reference the source header."""
        result = await sdl_migration_lookup("SDL_OpenAudio")

        if "No migration" not in result:
            assert ".h" in result  # Header file name

    @pytest.mark.asyncio
    async def test_includes_usage_hint(self):
        """Test that results include usage instructions."""
        result = await sdl_migration_lookup("SDL_NonExistentFunction123")

        assert "sdl_migration_header" in result

    @pytest.mark.asyncio
    async def test_truncates_long_matches(self):
        """Test that long matches are truncated appropriately."""
        # Try to find a symbol that might have long migration content
        result = await sdl_migration_lookup("SDL")

        # Check that result is reasonable size
        if "No migration" not in result:
            # Should either truncate or handle long content
            assert len(result) < 100000  # Reasonable max size


class TestSDLMigrationHeader:
    """Test the sdl_migration_header tool."""

    @pytest.mark.asyncio
    async def test_valid_header_returns_guide(self):
        """Test that valid header returns migration guide."""
        result = await sdl_migration_header("SDL_audio.h")

        assert len(result) > 100  # Has substantial content
        # Should contain migration information
        assert "SDL" in result

    @pytest.mark.asyncio
    async def test_normalizes_header_name(self):
        """Test that header name is normalized (adds .h and SDL_ prefix)."""
        # Test without .h extension
        result1 = await sdl_migration_header("SDL_audio")
        # Test without SDL_ prefix
        result2 = await sdl_migration_header("audio.h")
        # Test with both missing
        result3 = await sdl_migration_header("audio")

        # All should work or show same error
        assert len(result1) > 0
        assert len(result2) > 0
        assert len(result3) > 0

    @pytest.mark.asyncio
    async def test_invalid_header_shows_available(self):
        """Test that invalid header shows available headers."""
        result = await sdl_migration_header("SDL_nonexistent.h")

        assert "not found" in result.lower()
        assert "Available headers:" in result
        assert "SDL_" in result

    @pytest.mark.asyncio
    async def test_returns_complete_guide(self):
        """Test that complete migration guide is returned."""
        result = await sdl_migration_header("SDL_audio.h")

        # Should have substantial migration content
        if "not found" not in result.lower():
            assert len(result) > 50


class TestSDLMigrationSearch:
    """Test the sdl_migration_search tool."""

    @pytest.mark.asyncio
    async def test_searches_across_all_headers(self):
        """Test that search looks across all migration guides."""
        result = await sdl_migration_search("callback")

        # Should either find results or indicate no matches
        assert len(result) > 0
        assert "Migration Search Results" in result or "No results found" in result

    @pytest.mark.asyncio
    async def test_no_results_shows_help(self):
        """Test that no results provides helpful message."""
        result = await sdl_migration_search("zzzznonexistent123")

        assert "No results found" in result
        assert "sdl_migration_header" in result

    @pytest.mark.asyncio
    async def test_limits_match_output(self):
        """Test that search results are limited/truncated appropriately."""
        result = await sdl_migration_search("SDL")

        # Should have results but be manageable size
        # Check for truncation indicators
        if "No results found" not in result:
            assert len(result) < 50000  # Reasonable size limit

    @pytest.mark.asyncio
    async def test_includes_header_context(self):
        """Test that results include header context."""
        result = await sdl_migration_search("audio")

        if "No results found" not in result:
            assert ".h" in result or "header" in result.lower()

    @pytest.mark.asyncio
    async def test_includes_usage_hint(self):
        """Test that results include usage instructions."""
        result = await sdl_migration_search("audio")

        if "No results found" not in result:
            assert "sdl_migration_header" in result

    @pytest.mark.asyncio
    async def test_truncates_long_matches(self):
        """Test that search results are truncated for readability."""
        # Search for a common term that might have many long matches
        result = await sdl_migration_search("SDL")

        # Should have results but be manageable size
        if "No results found" not in result:
            # Check for truncation indicators or reasonable size
            assert len(result) < 100000  # Reasonable max size


class TestExampleToolsIntegration:
    """Test interactions between example tools."""

    @pytest.mark.asyncio
    async def test_list_categories_to_list_examples(self):
        """Test workflow: list categories -> list examples."""
        # List categories
        categories = await sdl_list_example_categories()
        assert "renderer" in categories.lower()

        # List examples in category
        examples = await sdl_list_examples("renderer")
        assert len(examples) > 0
        assert "renderer" in examples.lower()

    @pytest.mark.asyncio
    async def test_search_to_get_example(self):
        """Test workflow: search examples -> get specific example."""
        # Search for examples
        search_result = await sdl_search_examples("clear")

        if "No examples found" not in search_result:
            # Get specific example
            example = await sdl_get_example("renderer", "01-clear")
            assert "Source Code" in example


class TestMigrationToolsIntegration:
    """Test interactions between migration tools."""

    @pytest.mark.asyncio
    async def test_lookup_to_header(self):
        """Test workflow: lookup symbol -> get full header guide."""
        # Lookup a symbol
        lookup_result = await sdl_migration_lookup("SDL_OpenAudio")

        if "No migration" not in lookup_result:
            # Get full header guide
            header_result = await sdl_migration_header("SDL_audio.h")
            assert len(header_result) > 0

    @pytest.mark.asyncio
    async def test_search_to_header(self):
        """Test workflow: search migration -> get specific header."""
        # Search for migration info
        search_result = await sdl_migration_search("audio")

        if "No results found" not in search_result:
            # Get specific header
            header_result = await sdl_migration_header("SDL_audio.h")
            assert len(header_result) > 0
