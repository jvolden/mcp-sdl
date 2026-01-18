# Examples

Detailed examples and patterns for common roadmap operations.

## Adding Features

### Add to Existing Category

```markdown
## 0.1.0 Release

### Testing
- [ ] **Unit tests** - Test tool functions in isolation
- [ ] **Integration tests** - Test MCP protocol interactions
- [ ] **Code coverage reporting** - Track test coverage metrics  ← NEW
```

### Add to New Category

```markdown
## 0.2.0 Release

### Performance  ← NEW CATEGORY
- [ ] **Caching system** - Cache SDL3 function lookups
- [ ] **Lazy loading** - Load categories on demand
```

## Version Management

### Create New Minor Version

```markdown
## 0.2.0 Release

### New Features
- [ ] **Interactive examples** - Live code examples in documentation
- [ ] **Advanced search** - Filter and search capabilities
- [ ] **Export functionality** - Export documentation to different formats
```

### Create Patch Version

```markdown
## 0.1.1 Release

### Bug Fixes
- [ ] **Function search bug** - Fix case sensitivity in search
- [ ] **Memory leak** - Fix SDL3 category loading memory issue

### Documentation
- [ ] **Installation guide** - Fix broken installation steps
```

## Completion Tracking

### Mark Multiple Items Complete

```markdown
### Documentation
- [x] **README** - Complete setup and usage documentation
- [x] **Contributing guidelines** - Development setup guide  
- [x] **License file** - MIT License
- [ ] **API reference** - Comprehensive function documentation
```

### Mixed Status Example

```markdown
### Testing
- [x] **Basic unit tests** - Core functionality tests
- [x] **Integration tests** - MCP protocol tests
- [ ] **Performance tests** - Benchmark suite
- [ ] **End-to-end tests** - Full workflow validation
```

## Complex Scenarios

### Large Feature Set

```markdown
## 0.3.0 Release

### SDL3 Coverage
- [ ] **Audio category** - Complete audio subsystem functions
- [ ] **Input category** - Keyboard, mouse, and gamepad input
- [ ] **File I/O category** - File system operations
- [ ] **Threading category** - Threading primitives and synchronization

### Developer Experience
- [ ] **VS Code extension** - Syntax highlighting for SDL3
- [ ] **Debug tools** - Category validation utilities
- [ ] **Auto-completion** - IDE support for function lookup
```

### Maintenance Release

```markdown
## 0.2.1 Release

### Bug Fixes
- [ ] **Search crash** - Fix null pointer in category search
- [ ] **Memory optimization** - Reduce category loading overhead

### Security
- [ ] **Input validation** - Sanitize user queries
- [ ] **Dependency updates** - Update to latest FastMCP version
```

## Anti-Patterns (Don't Do These)

### ❌ Too Granular

```markdown
### Testing
- [ ] **Write test for SDL_Init** - Test SDL_Init function
- [ ] **Write test for SDL_Quit** - Test SDL_Quit function
- [ ] **Write test for SDL_GetError** - Test SDL_GetError function
```

**Better**:
```markdown
### Testing
- [ ] **Init category tests** - Test all initialization functions
```

### ❌ Too Vague

```markdown
### Enhancement
- [ ] **Improve documentation** - Make docs better
- [ ] **Add more features** - Expand functionality
```

**Better**:
```markdown
### Enhancement
- [ ] **Interactive examples** - Live code examples with syntax highlighting
- [ ] **Advanced search** - Filter by category, parameter type, and complexity
```

### ❌ Implementation Details

```markdown
### Core Improvements
- [ ] **Refactor tools.py** - Split into modules, add type hints, improve error handling
```

**Better**:
```markdown
### Core Improvements
- [ ] **Modular tool architecture** - Improve code organization and maintainability
```

## Workflow Examples

### Planning New Version

1. **Assess current state** - Check completion of current version
2. **Gather requirements** - What features are needed next?
3. **Determine version type** - Features = MINOR, fixes = PATCH
4. **Group by category** - Organize features logically
5. **Write clear descriptions** - Focus on user value

### Updating During Development

1. **Mark completed immediately** - Change `[ ]` to `[x]` when done
2. **Adjust scope if needed** - Move features between versions
3. **Add discovered work** - New items found during development
4. **Update descriptions** - Clarify based on implementation learnings

### Release Preparation

1. **Verify all items complete** - Everything should be `[x]`
2. **Plan next version** - Start planning what's next
3. **Review scope** - Did version deliver what was planned?
4. **Update version numbers** - Bump according to semantic versioning