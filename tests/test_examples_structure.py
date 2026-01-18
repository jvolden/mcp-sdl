"""Tests for SDL3 examples structure."""

from mcp_sdl.examples.sdl3 import CATEGORIES, EXAMPLES


class TestExamplesStructure:
    """Test SDL3 examples organization and structure."""

    def test_categories_exist(self):
        """Test that CATEGORIES is defined and not empty."""
        assert CATEGORIES is not None
        assert isinstance(CATEGORIES, dict)
        assert len(CATEGORIES) > 0

    def test_examples_exist(self):
        """Test that EXAMPLES is defined and not empty."""
        assert EXAMPLES is not None
        assert isinstance(EXAMPLES, dict)
        assert len(EXAMPLES) > 0

    def test_all_categories_have_descriptions(self):
        """Test that all categories have description strings."""
        for category, description in CATEGORIES.items():
            assert isinstance(category, str)
            assert isinstance(description, str)
            assert len(description) > 0

    def test_all_examples_in_valid_categories(self):
        """Test that all examples belong to defined categories."""
        for category in EXAMPLES:
            assert category in CATEGORIES, f"Example category '{category}' not in CATEGORIES"

    def test_example_structure(self):
        """Test that each example has required fields."""
        required_fields = ["title", "description", "difficulty", "url", "code"]

        for category, examples in EXAMPLES.items():
            assert isinstance(examples, dict), f"Category '{category}' examples must be a dict"

            for example_id, example_data in examples.items():
                assert isinstance(example_data, dict), f"Example '{example_id}' must be a dict"

                for field in required_fields:
                    assert field in example_data, f"Example '{category}/{example_id}' missing '{field}'"
                    assert example_data[field], f"Example '{category}/{example_id}' has empty '{field}'"

    def test_example_difficulty_levels(self):
        """Test that difficulty levels are valid."""
        valid_difficulties = ["beginner", "intermediate", "advanced"]

        for category, examples in EXAMPLES.items():
            for example_id, example_data in examples.items():
                difficulty = example_data["difficulty"]
                assert difficulty in valid_difficulties, \
                    f"Example '{category}/{example_id}' has invalid difficulty '{difficulty}'"

    def test_example_urls_format(self):
        """Test that example URLs follow expected format."""
        for category, examples in EXAMPLES.items():
            for example_id, example_data in examples.items():
                url = example_data["url"]
                assert url.startswith("https://examples.libsdl.org/SDL3/"), \
                    f"Example '{category}/{example_id}' has invalid URL format"
                assert category in url, \
                    f"Example '{category}/{example_id}' URL doesn't contain category"

    def test_example_code_not_empty(self):
        """Test that all examples have non-empty code."""
        for category, examples in EXAMPLES.items():
            for example_id, example_data in examples.items():
                code = example_data["code"]
                assert len(code) > 100, \
                    f"Example '{category}/{example_id}' has suspiciously short code"
                assert "#include" in code, \
                    f"Example '{category}/{example_id}' code doesn't look like C code"

    def test_example_ids_format(self):
        """Test that example IDs follow naming convention."""
        for _category, examples in EXAMPLES.items():
            for example_id in examples:
                # IDs should be like "01-clear" or "03-gamepad-polling"
                assert "-" in example_id or example_id.isalnum(), \
                    f"Example ID '{example_id}' doesn't follow naming convention"


class TestExamplesContent:
    """Test specific examples content."""

    def test_renderer_examples_exist(self):
        """Test that renderer category has examples."""
        assert "renderer" in EXAMPLES
        assert len(EXAMPLES["renderer"]) > 0

    def test_audio_examples_exist(self):
        """Test that audio category has examples."""
        assert "audio" in EXAMPLES
        assert len(EXAMPLES["audio"]) > 0

    def test_input_examples_exist(self):
        """Test that input category has examples."""
        assert "input" in EXAMPLES
        assert len(EXAMPLES["input"]) > 0

    def test_clear_example_exists(self):
        """Test that the clear rendering example exists."""
        assert "renderer" in EXAMPLES
        assert "01-clear" in EXAMPLES["renderer"]
        example = EXAMPLES["renderer"]["01-clear"]
        assert "SDL_RenderClear" in example["code"]
        assert "SDL_RenderPresent" in example["code"]

    def test_textures_example_exists(self):
        """Test that the textures rendering example exists."""
        assert "renderer" in EXAMPLES
        assert "06-textures" in EXAMPLES["renderer"]
        example = EXAMPLES["renderer"]["06-textures"]
        assert "SDL_Texture" in example["code"]
        assert "SDL_RenderTexture" in example["code"]

    def test_audio_playback_example_exists(self):
        """Test that the simple audio playback example exists."""
        assert "audio" in EXAMPLES
        assert "01-simple-playback" in EXAMPLES["audio"]
        example = EXAMPLES["audio"]["01-simple-playback"]
        assert "SDL_AudioStream" in example["code"]
        assert "SDL_OpenAudioDeviceStream" in example["code"]

    def test_gamepad_example_exists(self):
        """Test that the gamepad polling example exists."""
        assert "input" in EXAMPLES
        assert "03-gamepad-polling" in EXAMPLES["input"]
        example = EXAMPLES["input"]["03-gamepad-polling"]
        assert "SDL_Gamepad" in example["code"]
        assert "SDL_GetGamepadButton" in example["code"]
