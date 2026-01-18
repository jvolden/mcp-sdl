# MCP SDL3 Server Roadmap

## 0.1.0 Release

### Core Improvements
- [x] **Explore FastMCP** - Migrated to FastMCP, reduced code by ~78%
- [x] **Basic MCP server** - Functional SDL3 documentation server with 12 tools
- [x] **Tool structure** - Function reference, search, examples, category overviews, category listing, and migration guides
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
- [ ] **GitHub repository setup** - Create public repo with proper structure
- [ ] **Publishing to GitHub** - Publish so others can run with uvx
- [ ] **CI/CD pipeline** - Automated testing and releases

### Enhancement
- [x] **Expand SDL3 function coverage** - Added 50 items across init and render categories (119 total)
- [x] **Complete init category** - All 17 items from SDL wiki
- [x] **Core render category functions** - 52 items for essential 2D rendering
- [x] **Organize examples** - Structured examples from examples.libsdl.org with 4 browsing/retrieval tools
- [x] **Add SDL2 to SDL3 migration guide** - Migration directory with 3 headers and 3 query tools

## 0.2.0 Release

### SDL3 Function Coverage
- [ ] **Complete render category** - Add remaining ~50 advanced rendering functions (geometry, GPU API, platform-specific)
- [ ] **Complete video category** - Finish window and display management
- [ ] **Complete events category** - Add all event handling functions
- [ ] **Complete keyboard/mouse categories** - Finish input handling
- [ ] **Add audio category** - Implement audio subsystem functions
- [ ] **Add filesystem category** - Implement file operations
- [ ] **Add threading category** - Implement threading primitives

### SDL2 to SDL3 Migration Guide
- [ ] **Complete all migration headers** - Add remaining ~40 SDL2 header migration guides (events, input, threading, etc.)
- [ ] **Migration guide tests** - 100% test coverage for migration structure

### Tool Organization
- [x] **Refactor tools.py into modules** - Split 675-line tools.py into api_tools, examples_tools, migration_tools

### Tool Optimization
- [ ] **Design combined "smart" tools** - Reduce token usage by consolidating tools with intelligent routing (target: 3-4 smart tools instead of 12)

### SDL Satellite Libraries
- [ ] **Add SDL satellite library placeholders** - Create structure in api/ for extension libraries
  - [ ] SDL_image placeholder directory and structure
  - [ ] SDL_ttf placeholder directory and structure
  - [ ] SDL_mixer placeholder directory and structure
- [ ] **Implement SDL_image** - Full API coverage for image file loading (PNG, JPG, WebP, etc.)
- [ ] **Impleme_image** - Image file loading (PNG, JPG, WebP, etc.)
- [ ] **Add SDL_ttf** - TrueType font rendering
- [ ] **Add SDL_mixer** - Av, multiple-streams, planar-data)
  - [ ] Add remaining input examples (joystick-polling, joystick-events, gamepad-events)
  - [ ] Expand SDL3 examples** - Add remaining renderer, audio, input, camera, asyncio, pen, misc, and demo examples