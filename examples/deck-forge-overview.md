---
marp: true
theme: plato
paginate: true
header: 'Deck Forge Overview'
---

<!-- _class: title -->

# Deck Forge

**AI-assisted presentations that follow proven rhetorical principles**

---

# Deck Forge helps you create effective presentations faster

- **Problem**: Most AI slide generators focus on formatting, not rhetoric
- **Solution**: Combine rhetorical principles + visual design + LLM collaboration
- **Outcome**: Decks that communicate clearly, even without a presenter

---

# Three capabilities make this work

1. **Codified principles** — Rhetoric and design guidelines Claude follows
2. **Structural templates** — Proven patterns for common deck types
3. **Collaborative workflow** — Iterate on both content and design

---

<!-- _class: transition -->

# Codified Principles

---

# Every slide title is an assertion, not a label

| ❌ Weak (Label) | ✅ Strong (Assertion) |
|----------------|----------------------|
| Results | Treatment increased efficiency by 40% |
| Architecture | Three services handle all network traffic |
| Q3 Performance | Revenue exceeded forecast despite headcount freeze |

If someone reads only titles, they understand your argument.

---

# Lead with conclusions, then support them

**The Pyramid Principle** (Barbara Minto, McKinsey):

```
        ┌─────────────────┐
        │   CONCLUSION    │  ← State this FIRST
        └────────┬────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
 Point 1      Point 2      Point 3
    │            │            │
 Evidence    Evidence    Evidence
```

Don't build to a conclusion. Start with it.

---

<!-- _class: transition -->

# Structural Templates

---

# Four templates cover most presentation needs

| Template | Use Case |
|----------|----------|
| **Technical Explainer** | How a system or process works |
| **Project Update** | Status reports and progress |
| **Proposal** | Recommendations requiring decisions |
| **Tutorial** | Teaching a skill step-by-step |

Each template encodes the pyramid structure for its purpose.

---

# Templates provide structural scaffolding

```markdown
# Executive Summary

| | |
|---|---|
| **Situation** | [Current state] |
| **Problem** | [The challenge] |
| **Recommendation** | [What you propose] |
| **Impact** | [Expected outcome] |
```

Claude fills in the content following the structure.

---

<!-- _class: transition -->

# Collaborative Workflow

---

# Work with Claude in four phases

1. **Understand** — Clarify audience, purpose, constraints
2. **Structure** — Review slide titles as outline (get the argument right)
3. **Content** — Fill in evidence and supporting material
4. **Design** — Apply theme, refine visuals

Content and structure before visual polish.

---

# The result: Decks that work

- ✅ Clear argument visible in titles alone
- ✅ Conclusions stated early
- ✅ One idea per slide
- ✅ Visual hierarchy that guides attention
- ✅ Readable without the presenter

---

<!-- _class: transition -->

# Getting Started

---

# Setup takes five minutes

```bash
# Install Marp CLI
npm install -g @marp-team/marp-cli

# Clone deck-forge to your projects
# Open with Claude Code

# Build a deck
./scripts/build.sh preview my-deck.md
```

---

# Summary: Three things to remember

1. **Principles are non-negotiable** — Assertion titles, pyramid structure, one idea per slide

2. **Templates encode structure** — Don't start from scratch; adapt a pattern

3. **Iterate on argument first** — Get the outline right before filling in details

---

# Resources

- **Principles**: `principles/` directory
- **Templates**: `templates/` directory  
- **Themes**: `themes/` directory
- **Build**: `./scripts/build.sh --help`

**Questions?** Open an issue or start a discussion.
