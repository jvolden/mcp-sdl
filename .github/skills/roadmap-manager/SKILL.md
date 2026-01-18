---
name: roadmap-manager
description: Manages project roadmap structure, version planning, and feature tracking. Use when the user wants to add features to the roadmap, update roadmap status, create new version sections, reorganize roadmap items, or when addressing/implementing items that are listed on the roadmap. Ensures proper semantic versioning (major.minor.patch) and clear feature categorization.
---

# Roadmap Manager

Manages ROADMAP.md structure, version planning, and feature tracking.

## Basic Structure

```markdown
## [Version] Release

### [Category]
- [ ] **[Feature Name]** - [Description]
- [x] **[Completed Feature]** - [Description]
```

## Semantic Versioning

- **MAJOR (X.0.0)**: Breaking changes, API redesigns
- **MINOR (0.X.0)**: New features (backward compatible)  
- **PATCH (0.0.X)**: Bug fixes, security patches, docs only

**Rule**: New features require MINOR version minimum.

## Core Operations

**Add Feature**: Add to existing category or create new category
**Mark Complete**: Change `[ ]` to `[x]`
**New Version**: Create `## X.Y.Z Release` section

## Common Categories

- **Core Improvements**, **Documentation**, **Testing**, **Publishing**
- **Enhancement**, **SDL3 Coverage**, **Bug Fixes**, **Performance**

(See [references/categories.md](references/categories.md) for full list and descriptions)

## References

- [Category Guidelines](references/categories.md) - Complete category list and usage
- [Best Practices](references/best-practices.md) - Detailed formatting and workflow guidelines
- [Examples](references/examples.md) - Detailed examples and patterns
