"""Unit tests for SDL3 API category structure and format consistency."""

import importlib
from pathlib import Path

import pytest

# Expected categories and their wiki names
EXPECTED_CATEGORIES = {
    "init": "CategoryInit",
    "video": "CategoryVideo",
    "render": "CategoryRender",
    "events": "CategoryEvents",
    "keyboard": "CategoryKeyboard",
    "mouse": "CategoryMouse",
    "error": "CategoryError",
    "surface": "CategorySurface",
    "timer": "CategoryTimer",
}


class TestCategoryStructure:
    """Test that all categories have consistent structure."""

    @pytest.fixture
    def category_modules(self):
        """Load all category modules."""
        modules = {}
        for category_name in EXPECTED_CATEGORIES:
            module_name = f"mcp_sdl.api.sdl3.category_{category_name}"
            modules[category_name] = importlib.import_module(module_name)
        return modules

    def test_all_categories_exist(self, category_modules):
        """Test that all expected category modules can be imported."""
        assert len(category_modules) == len(EXPECTED_CATEGORIES)
        for category_name in EXPECTED_CATEGORIES:
            assert category_name in category_modules

    def test_category_has_required_constants(self, category_modules):
        """Test that each category has all required module-level constants."""
        required_constants = [
            "WIKI_URL",
            "OVERVIEW",
            "FUNCTIONS",
            "ENUMS",
            "DATATYPES",
            "MACROS",
            "CATEGORY",
            "FUNCTION_NAMES",
            "ENUM_NAMES",
            "DATATYPE_NAMES",
            "MACRO_NAMES",
        ]

        for category_name, module in category_modules.items():
            for constant in required_constants:
                assert hasattr(module, constant), (
                    f"Category '{category_name}' missing constant '{constant}'"
                )

    def test_category_wiki_url_format(self, category_modules):
        """Test that WIKI_URL follows the correct format."""
        for category_name, module in category_modules.items():
            expected_category_name = EXPECTED_CATEGORIES[category_name]
            expected_url = f"https://wiki.libsdl.org/SDL3/{expected_category_name}"
            assert expected_url == module.WIKI_URL, (
                f"Category '{category_name}' has incorrect WIKI_URL. "
                f"Expected: {expected_url}, Got: {module.WIKI_URL}"
            )

    def test_category_constant_matches_name(self, category_modules):
        """Test that CATEGORY constant matches the expected category name."""
        for category_name, module in category_modules.items():
            assert category_name == module.CATEGORY, (
                f"Category '{category_name}' has incorrect CATEGORY constant. "
                f"Expected: {category_name}, Got: {module.CATEGORY}"
            )

    def test_overview_is_non_empty_string(self, category_modules):
        """Test that OVERVIEW is a non-empty string."""
        for category_name, module in category_modules.items():
            assert isinstance(module.OVERVIEW, str), (
                f"Category '{category_name}' OVERVIEW is not a string"
            )
            assert len(module.OVERVIEW) > 0, (
                f"Category '{category_name}' OVERVIEW is empty"
            )

    def test_metadata_dicts_are_dicts(self, category_modules):
        """Test that FUNCTIONS, ENUMS, DATATYPES, MACROS are dictionaries."""
        for category_name, module in category_modules.items():
            assert isinstance(module.FUNCTIONS, dict), (
                f"Category '{category_name}' FUNCTIONS is not a dict"
            )
            assert isinstance(module.ENUMS, dict), (
                f"Category '{category_name}' ENUMS is not a dict"
            )
            assert isinstance(module.DATATYPES, dict), (
                f"Category '{category_name}' DATATYPES is not a dict"
            )
            assert isinstance(module.MACROS, dict), (
                f"Category '{category_name}' MACROS is not a dict"
            )

    def test_name_lists_are_lists(self, category_modules):
        """Test that all *_NAMES constants are lists."""
        for category_name, module in category_modules.items():
            assert isinstance(module.FUNCTION_NAMES, list), (
                f"Category '{category_name}' FUNCTION_NAMES is not a list"
            )
            assert isinstance(module.ENUM_NAMES, list), (
                f"Category '{category_name}' ENUM_NAMES is not a list"
            )
            assert isinstance(module.DATATYPE_NAMES, list), (
                f"Category '{category_name}' DATATYPE_NAMES is not a list"
            )
            assert isinstance(module.MACRO_NAMES, list), (
                f"Category '{category_name}' MACRO_NAMES is not a list"
            )

    def test_name_lists_match_dict_keys(self, category_modules):
        """Test that *_NAMES lists match the keys of their corresponding dicts."""
        for category_name, module in category_modules.items():
            # Test FUNCTION_NAMES matches FUNCTIONS.keys()
            assert set(module.FUNCTION_NAMES) == set(module.FUNCTIONS.keys()), (
                f"Category '{category_name}' FUNCTION_NAMES doesn't match FUNCTIONS keys"
            )
            # Test ENUM_NAMES matches ENUMS.keys()
            assert set(module.ENUM_NAMES) == set(module.ENUMS.keys()), (
                f"Category '{category_name}' ENUM_NAMES doesn't match ENUMS keys"
            )
            # Test DATATYPE_NAMES matches DATATYPES.keys()
            assert set(module.DATATYPE_NAMES) == set(module.DATATYPES.keys()), (
                f"Category '{category_name}' DATATYPE_NAMES doesn't match DATATYPES keys"
            )
            # Test MACRO_NAMES matches MACROS.keys()
            assert set(module.MACRO_NAMES) == set(module.MACROS.keys()), (
                f"Category '{category_name}' MACRO_NAMES doesn't match MACROS keys"
            )

    def test_category_has_content(self, category_modules):
        """Test that each category has at least some content (functions, enums, datatypes, or macros)."""
        for category_name, module in category_modules.items():
            total_items = (
                len(module.FUNCTIONS)
                + len(module.ENUMS)
                + len(module.DATATYPES)
                + len(module.MACROS)
            )
            assert total_items > 0, (
                f"Category '{category_name}' has no content "
                f"(no functions, enums, datatypes, or macros)"
            )


class TestCategoryMetadataFormat:
    """Test the format of individual metadata items."""

    @pytest.fixture
    def category_modules(self):
        """Load all category modules."""
        modules = {}
        for category_name in EXPECTED_CATEGORIES:
            module_name = f"mcp_sdl.api.sdl3.category_{category_name}"
            modules[category_name] = importlib.import_module(module_name)
        return modules

    def test_function_metadata_format(self, category_modules):
        """Test that function metadata has required fields."""
        required_fields = ["category", "description", "signature", "parameters", "returns", "example"]

        for category_name, module in category_modules.items():
            for func_name, func_data in module.FUNCTIONS.items():
                assert isinstance(func_data, dict), (
                    f"Function '{func_name}' in '{category_name}' is not a dict"
                )
                for field in required_fields:
                    assert field in func_data, (
                        f"Function '{func_name}' in '{category_name}' missing field '{field}'"
                    )
                # Category should match the module's category
                assert func_data["category"] == category_name, (
                    f"Function '{func_name}' category mismatch. "
                    f"Expected: {category_name}, Got: {func_data['category']}"
                )

    def test_enum_metadata_format(self, category_modules):
        """Test that enum metadata has required fields."""
        required_fields = ["description"]

        for category_name, module in category_modules.items():
            for enum_name, enum_data in module.ENUMS.items():
                assert isinstance(enum_data, dict), (
                    f"Enum '{enum_name}' in '{category_name}' is not a dict"
                )
                for field in required_fields:
                    assert field in enum_data, (
                        f"Enum '{enum_name}' in '{category_name}' missing field '{field}'"
                    )

    def test_datatype_metadata_format(self, category_modules):
        """Test that datatype metadata has required fields."""
        required_fields = ["description"]

        for category_name, module in category_modules.items():
            for datatype_name, datatype_data in module.DATATYPES.items():
                assert isinstance(datatype_data, dict), (
                    f"Datatype '{datatype_name}' in '{category_name}' is not a dict"
                )
                for field in required_fields:
                    assert field in datatype_data, (
                        f"Datatype '{datatype_name}' in '{category_name}' missing field '{field}'"
                    )

    def test_macro_metadata_format(self, category_modules):
        """Test that macro metadata has required fields."""
        required_fields = ["description"]

        for category_name, module in category_modules.items():
            for macro_name, macro_data in module.MACROS.items():
                assert isinstance(macro_data, dict), (
                    f"Macro '{macro_name}' in '{category_name}' is not a dict"
                )
                for field in required_fields:
                    assert field in macro_data, (
                        f"Macro '{macro_name}' in '{category_name}' missing field '{field}'"
                    )


class TestCategoryDynamicImports:
    """Test that dynamic imports work correctly."""

    def test_category_directories_exist(self):
        """Test that all category directories exist."""
        base_path = Path(__file__).parent.parent / "src" / "mcp_sdl" / "api" / "sdl3"

        for category_name in EXPECTED_CATEGORIES:
            category_dir = base_path / f"category_{category_name}"
            assert category_dir.exists(), f"Category directory '{category_dir}' does not exist"
            assert category_dir.is_dir(), f"Category path '{category_dir}' is not a directory"

            # Check that __init__.py exists
            init_file = category_dir / "__init__.py"
            assert init_file.exists(), f"Category '{category_name}' missing __init__.py"

    def test_individual_files_have_correct_exports(self):
        """Test that individual metadata files export the correct constant."""
        base_path = Path(__file__).parent.parent / "src" / "mcp_sdl" / "api" / "sdl3"

        for category_name in EXPECTED_CATEGORIES:
            category_dir = base_path / f"category_{category_name}"

            # Get all .py files except __init__.py
            py_files = [f for f in category_dir.glob("*.py") if f.name != "__init__.py"]

            for py_file in py_files:
                module_name = f"mcp_sdl.api.sdl3.category_{category_name}.{py_file.stem}"
                module = importlib.import_module(module_name)

                # Each file should export exactly one of: FUNCTION, ENUM, DATATYPE, or MACRO
                exports = [
                    hasattr(module, "FUNCTION"),
                    hasattr(module, "ENUM"),
                    hasattr(module, "DATATYPE"),
                    hasattr(module, "MACRO"),
                ]
                assert sum(exports) == 1, (
                    f"File '{py_file.name}' in '{category_name}' should export exactly one of "
                    f"FUNCTION, ENUM, DATATYPE, or MACRO"
                )


class TestCategoryIntegration:
    """Test that categories integrate correctly with the main SDL3 module."""

    def test_sdl3_module_aggregation(self):
        """Test that SDL3 module correctly aggregates all categories."""
        from mcp_sdl.api.sdl3 import SDL3_CATEGORIES, SDL3_FUNCTIONS

        # SDL3_FUNCTIONS should be a dict
        assert isinstance(SDL3_FUNCTIONS, dict)
        assert len(SDL3_FUNCTIONS) > 0

        # SDL3_CATEGORIES should be a dict with category names as keys
        assert isinstance(SDL3_CATEGORIES, dict)
        for category_name in EXPECTED_CATEGORIES:
            assert category_name in SDL3_CATEGORIES, (
                f"Category '{category_name}' not in SDL3_CATEGORIES"
            )
            assert isinstance(SDL3_CATEGORIES[category_name], list), (
                f"SDL3_CATEGORIES['{category_name}'] is not a list"
            )

    def test_no_duplicate_functions_across_categories(self):
        """Test that function names are unique across all categories."""
        from mcp_sdl.api.sdl3 import SDL3_CATEGORIES

        all_function_names = []
        for _category_name, function_names in SDL3_CATEGORIES.items():
            all_function_names.extend(function_names)

        # Check for duplicates
        duplicates = [name for name in all_function_names if all_function_names.count(name) > 1]
        assert len(duplicates) == 0, f"Duplicate function names found: {set(duplicates)}"
