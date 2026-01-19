"""SDL2 to SDL3 migration guides organized by header file."""

import importlib
from pathlib import Path
from typing import TypedDict


class MigrationSearchResult(TypedDict):
    """Result from migration search."""
    header: str
    matches: list[str]


# Discover all migration header modules
current_dir = Path(__file__).parent
header_files = [
    f.stem for f in current_dir.glob("SDL_*.py")
    if f.is_file() and not f.name.startswith('_')
]

HEADERS = {}

for header_name in sorted(header_files):
    try:
        module = importlib.import_module(f".{header_name}", package=__name__)
        if hasattr(module, "HEADER") and hasattr(module, "MIGRATION_DATA"):
            HEADERS[module.HEADER] = module.MIGRATION_DATA
    except ImportError:
        pass

def get_all_headers() -> list[str]:
    """Get list of all available migration headers."""
    return sorted(HEADERS.keys())

def get_migration_data(header: str) -> str | None:
    """Get migration data for a specific header."""
    return HEADERS.get(header)

def search_migrations(query: str) -> list[MigrationSearchResult]:
    """Search across all migration data for a query string."""
    results: list[MigrationSearchResult] = []
    query_lower = query.lower()

    for header, data in HEADERS.items():
        if query_lower in data.lower():
            # Find context around matches
            lines = data.split('\n')
            matching_lines = []
            for i, line in enumerate(lines):
                if query_lower in line.lower():
                    # Get some context
                    start = max(0, i - 2)
                    end = min(len(lines), i + 3)
                    context = '\n'.join(lines[start:end])
                    matching_lines.append(context)

            if matching_lines:
                results.append({
                    'header': header,
                    'matches': matching_lines
                })

    return results

__all__ = ["HEADERS", "get_all_headers", "get_migration_data", "search_migrations"]
