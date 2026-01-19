# MCP SDL3 Server Roadmap

## 0.1.0 Release - COMPLETE (January 18, 2026)

**[Released as v0.1.0](https://github.com/jvolden/mcp-sdl/releases/tag/v0.1.0)** - Early prerelease of MCP SDL3 server with basic functionality!

### Core Improvements
- [x] **Explore FastMCP** - Migrated to FastMCP, reduced code by ~78%
- [x] **Basic MCP server** - Functional SDL3 documentation server with 9 tools
- [x] **Tool structure** - Function reference, search, examples browsing/retrieval, and migration guides
- [x] **Dynamic imports** - File structure as code, automatic discovery of new functions

### API Structure
- [x] **Category-based organization** - Individual files for functions, enums, datatypes, macros
- [x] **Wiki alignment** - Categories match SDL3 wiki naming (init, render, etc.)
- [x] **Metadata consistency** - Unified format across all categories
- [x] **Complete category catalog** - List of all 50+ SDL3 categories with descriptions

### Documentation
- [x] **README** - Complete setup and usage documentation
- [x] **Contributing guidelines** - CONTRIBUTING.md with development setup and AI assistant support
- [x] **License file** - MIT License
- [x] **Copilot instructions** - Project guidelines for AI-assisted development

### Testing
- [x] **Category structure tests** - 17 tests validating consistent category format
- [x] **Tool function tests** - 61 tests covering all 9 MCP tool implementations
- [x] **100% business logic coverage** - 95.75% total coverage, 94.76% tools coverage (uncovered lines are defensive edge cases)
- [x] **Integration smoke tests** - 2 tests validating FastMCP protocol compatibility across version bumps

### Publishing
- [x] **GitHub repository setup** - Public repo at https://github.com/jvolden/mcp-sdl with professional structure
- [x] **Publishing to GitHub** - Users can install with `uvx --from git+https://github.com/jvolden/mcp-sdl mcp-sdl`
- [x] **CI/CD pipeline** - GitHub Actions for testing (Python 3.10-3.12), linting, type checking, coverage
- [x] **PR requirements workflow** - Enforces issue linking for all pull requests
- [x] **Repository templates** - Issue templates (bug/feature) and PR template with checklists
- [x] **VS Code developer setup** - Template configuration and setup instructions

### Enhancement
- [x] **Expand SDL3 function coverage** - Added 50 items across init and render categories (119 total)
- [x] **Complete init category** - All 17 items from SDL wiki
- [x] **Core render category functions** - 52 items for essential 2D rendering
- [x] **Organize examples** - Structured examples from examples.libsdl.org with 4 browsing/retrieval tools
- [x] **Add SDL2 to SDL3 migration guide** - Migration directory with 3 headers and 3 query tools

## 0.2.0 Release

### Repository Management
- [ ] **Version tagging system** - Manual git tagging for releases (no automated versioning)
- [ ] **Release notes** - Manual creation of GitHub releases with changelogs
- [ ] **Branch protection** - Configure GitHub branch protection rules and required status checks

### SDL3 Function Coverage
- [ ] **Complete render category** - Add remaining ~50 advanced rendering functions (geometry, GPU API, platform-specific)
- [ ] **Complete video category** - Finish window and display management
- [ ] **Complete events category** - Add all event handling functions
- [ ] **Complete keyboard/mouse categories** - Finish input handling
- [ ] **Add audio category** - Implement audio subsystem functions
- [ ] **Add filesystem category** - Implement file operations
- [ ] **Add threading category** - Implement threading primitives

### SDL2 to SDL3 Migration Guide
- [x] **Complete all migration headers** - Add remaining ~40 SDL2 header migration guides (events, input, threading, etc.)
- [x] **Migration guide tests** - 100% test coverage for migration structure

### Tool Organization
- [x] **Refactor tools.py into modules** - Split 675-line tools.py into api_tools, examples_tools, migration_tools

### Tool Optimization
- [x] **Consolidate tools with smart routing** - Reduced from 9 tools to 4 smart tools using optional parameters (sdl_examples, sdl_migration unified)
- [ ] **Review and standardize method names** - Audit all method names across codebase for clarity and consistent naming conventions (e.g., format_category_suggestions)
- [ ] **Performance optimization** - Optimize tool response times and memory usage
- [ ] **Tool documentation** - Enhanced inline documentation and examples for each tool

### Example Enhancement
- [ ] **Expand SDL3 examples** - Add remaining renderer, audio, input, camera, asyncio, pen, misc, and demo examples
- [ ] **Multi-language examples** - Add examples in C++, Rust, and other SDL3 bindings
- [ ] **Interactive example finder** - Smart example discovery based on user intent

### SDL Satellite Libraries
- [ ] **Add SDL satellite library placeholders** - Create structure in api/ for extension libraries
  - [ ] SDL_image placeholder directory and structure
  - [ ] SDL_ttf placeholder directory and structure  
  - [ ] SDL_mixer placeholder directory and structure
- [ ] **Implement SDL_image** - Full API coverage for image file loading (PNG, JPG, WebP, etc.)
- [ ] **Add SDL_ttf** - TrueType font rendering support
- [ ] **Add SDL_mixer** - Audio mixing, multiple streams, and advanced audio features

## 0.3.0 Release (Future)

### Advanced Features
- [ ] **Smart assistant integration** - Enhanced AI assistant interactions with context awareness
- [ ] **Advanced search capabilities** - Semantic search across all SDL3 documentation
- [ ] **Performance benchmarking** - Tools for comparing SDL3 vs SDL2 performance
- [ ] **Code generation** - AI-assisted SDL3 code generation for common patterns