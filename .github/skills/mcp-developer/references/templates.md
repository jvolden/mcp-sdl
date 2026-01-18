# Code Templates

Detailed templates for implementing SDL3 categories and functions.

## Category Template (`__init__.py`)

```python
"""SDL3 {description} functions."""
import importlib
from pathlib import Path

WIKI_URL = "https://wiki.libsdl.org/SDL3/Category{Name}"
OVERVIEW = """Multi-line description from official SDL3 wiki."""

# Dynamic imports
current_dir = Path(__file__).parent
module_files = [f.stem for f in current_dir.glob("*.py") if f.stem != "__init__"]

FUNCTIONS = {}
ENUMS = {}
DATATYPES = {}
MACROS = {}

for module_name in module_files:
    module = importlib.import_module(f".{module_name}", package=__name__)
    
    if hasattr(module, "FUNCTION"):
        FUNCTIONS.update(module.FUNCTION)
    if hasattr(module, "ENUM"):
        ENUMS.update(module.ENUM)
    if hasattr(module, "DATATYPE"):
        DATATYPES.update(module.DATATYPE)
    if hasattr(module, "MACRO"):
        MACROS.update(module.MACRO)

CATEGORY = "{category_key}"
FUNCTION_NAMES = list(FUNCTIONS.keys())
ENUM_NAMES = list(ENUMS.keys())
DATATYPE_NAMES = list(DATATYPES.keys())
MACRO_NAMES = list(MACROS.keys())
```

## Function Template

```python
"""SDL_FunctionName function definition."""

FUNCTION = {
    "SDL_FunctionName": {
        "category": "category_key",
        "description": "Brief description of what the function does",
        "signature": "ReturnType SDL_FunctionName(ParamType param1, ParamType param2)",
        "parameters": [
            {
                "name": "param1",
                "type": "ParamType",
                "description": "Description of parameter 1"
            },
            {
                "name": "param2", 
                "type": "ParamType",
                "description": "Description of parameter 2"
            }
        ],
        "returns": "Description of return value",
        "example": """// C code example
ReturnType result = SDL_FunctionName(param1, param2);
if (result != expected) {
    SDL_Log("Error: %s", SDL_GetError());
}""",
        "remarks": "Additional usage notes (optional)",
        "thread_safety": "Thread safety information (optional)",
        "see_also": ["SDL_RelatedFunction1", "SDL_RelatedFunction2"]
    }
}
```

## Enum Template

```python
"""SDL_EnumName enum definition."""

ENUM = {
    "SDL_EnumName": {
        "category": "category_key",
        "description": "Enum description",
        "values": [
            {
                "name": "SDL_ENUM_VALUE1",
                "value": "0x00000001",
                "description": "Description of value 1"
            },
            {
                "name": "SDL_ENUM_VALUE2",
                "value": "0x00000002", 
                "description": "Description of value 2"
            }
        ],
        "example": """// Usage example
SDL_EnumName flags = SDL_ENUM_VALUE1 | SDL_ENUM_VALUE2;
if (flags & SDL_ENUM_VALUE1) {
    // Handle value 1
}"""
    }
}
```

## Datatype Template

```python
"""SDL_TypeName datatype definition."""

DATATYPE = {
    "SDL_TypeName": {
        "category": "category_key",
        "description": "Opaque structure representing...",
        "definition": "typedef struct SDL_TypeName SDL_TypeName;",
        "fields": [
            {
                "name": "field1",
                "type": "FieldType",
                "description": "Description of field 1"
            }
        ],
        "notes": "Additional usage notes and lifetime management"
    }
}
```

## Macro Template

```python
"""SDL_MACRO_NAME macro definition."""

MACRO = {
    "SDL_MACRO_NAME": {
        "category": "category_key",
        "description": "Macro description",
        "definition": "#define SDL_MACRO_NAME value",
        "example": """// Usage example
int result = SDL_MACRO_NAME;
if (result == expected_value) {
    // Success
}"""
    }
}
```

## Example Guidelines

- Keep examples under 10 lines when possible
- Show "minimal viable demonstration" of the function's purpose
- Include basic error checking when relevant
- Use realistic parameter values
- Focus on the specific function, not complex setup