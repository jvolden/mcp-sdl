# Best Practices

Detailed guidelines for maintaining clean, scannable roadmaps.

## Content Guidelines

### 1. Be Brief
Keep descriptions concise and high-level. Focus on the "what" not the "how".

**Good**: "Add audio category" 
**Bad**: "Implement all SDL3 audio functions including SDL_OpenAudioDevice, SDL_PlayAudioDevice, etc."

### 2. Avoid Sub-tasks
Use single-level tasks only - no nested bullets under features.

**Good**:
```markdown
- [ ] **Unit tests** - Test tool functions in isolation
- [ ] **Integration tests** - Test MCP protocol interactions
```

**Bad**:
```markdown
- [ ] **Testing** - Add comprehensive tests
  - [ ] Unit tests
  - [ ] Integration tests
```

### 3. Be Specific
Clear, actionable feature descriptions that communicate intent.

**Good**: "Interactive code examples"
**Bad**: "Better examples"

### 4. One Feature Per Line
Don't combine multiple features in single entries.

**Good**:
```markdown
- [ ] **README updates** - Improve installation instructions
- [ ] **API documentation** - Add function reference guide
```

**Bad**:
```markdown
- [ ] **Documentation** - Update README and add API docs
```

### 5. Keep It Scannable
Quick to read at a glance, even for completed tasks. Avoid verbose descriptions.

### 6. No Emojis or Decorative Elements
Keep documentation professional and clean. Avoid emojis, decorative symbols, or visual flourishes in roadmap text.

**Good**: "0.1.0 Release - COMPLETE"
**Bad**: "🎉 0.1.0 Release - COMPLETE ✅"

## Formatting Standards

### 7. Use Standard Checkboxes
- Planned: `- [ ] **Name** - Description`
- Completed: `- [x] **Name** - Description`
- Never mix checkbox styles

### 8. Bold Feature Names
Always use `**Feature Name**` for the main feature name, followed by ` - description`.

### 9. Consistent Categorization
Group related features in the same category. Don't split related work across categories.

## Workflow Practices

### 10. Update Regularly
Mark completed items immediately with `[x]` when work finishes.

### 11. Version Planning
Choose version numbers based on content:
- **Features** → MINOR versions (0.X.0)
- **Bug fixes only** → PATCH versions (0.0.X)  
- **Breaking changes** → MAJOR versions (X.0.0)

### 12. Order Matters
- List versions in chronological order (oldest to newest)
- Within versions, group by logical category
- Within categories, no specific order needed

### 13. Review Before Adding
Before adding new features:
1. Check if similar work is already planned
2. Ensure the feature fits the version scope
3. Verify category choice makes sense
4. Confirm description is clear and actionable

## Common Mistakes

### Don't:
- Use vague descriptions ("improve X", "better Y")
- Use emojis or decorative symbols
- Create nested task lists
- Mix completed and planned items randomly
- Create categories for single items
- Include implementation details in descriptions
- Use inconsistent checkbox formatting

### Do:
- Keep descriptions outcome-focused
- Use flat task structure
- Group completed items together when possible
- Reuse existing categories when appropriate
- Focus on user/developer value
- Maintain consistent formatting throughout