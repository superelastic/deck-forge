# Deck Forge

## Purpose

AI-assisted creation of presentation slide decks following established rhetorical and design principles. Transforms complex technical subjects into clear, memorable presentations.

## Project Map

```
principles/        # Design principles - READ BEFORE generating slides
  rhetoric.md      # Core rhetoric rules (MANDATORY reading)
  pyramid.md       # Pyramid principle for structure
  visual-hierarchy.md

templates/         # Starter templates by deck type
  technical-explainer.md
  project-update.md
  proposal.md
  tutorial.md

themes/            # Marp CSS themes (plato, heidegger, turing)

scripts/
  build.sh         # Build HTML/PDF/PPTX from markdown

agent_docs/        # Detailed references
  marp-syntax.md   # Marp formatting reference
  diagrams-and-charts.md  # Visualization tools (Mermaid, Matplotlib)
  quality-checklist.md
  slide-creation-rules.md
```

## Workflow

### Creating a Deck

1. **Clarify requirements** - Ask about:
   - Audience and their background
   - Goal: what should they know/believe/do after?
   - Format: live presentation or async review?
   - Approximate slide count

2. **Read principles** - Read `principles/rhetoric.md` before generating any slides

3. **Select template** - Choose from `templates/` based on deck purpose

4. **Generate content** - Create Marp-formatted markdown following the principles

5. **Build output** - Use build script to generate deliverable

### Build Commands

```bash
./scripts/build.sh preview deck.md   # Live preview in browser
./scripts/build.sh html deck.md      # Export HTML
./scripts/build.sh pdf deck.md       # Export PDF
./scripts/build.sh pptx deck.md      # Export PowerPoint
./scripts/build.sh all deck.md       # Export all formats
```

### Diagrams and Charts

Use the right tool for each visualization type:

| Type | Tool | Notes |
|------|------|-------|
| Flowcharts, sequences, state diagrams | Mermaid | Inline in markdown, no build step |
| Data plots (X-Y, bar, pie) | Matplotlib → SVG | Generate to `img/`, include as image |

For data-driven charts, create a Python script in `img/generate_charts.py` and run before building.

See `agent_docs/diagrams-and-charts.md` for syntax, examples, and styling guidance.

### Verification

Before completing any deck, run through `agent_docs/quality-checklist.md`.

### File Organization

**During creation**, decks go in a folder at project root:
```
deck-forge/
  my-presentation/
    deck.md          # Content
    img/             # Images
    output/          # Build outputs
```

**After delivery**, move finished decks to `~/presentations/`:
```bash
mv my-presentation ~/presentations/
```

This keeps Deck Forge clean as a tool. Session memory captures prompts, so any deck can be recreated by re-prompting with the original source material.

## Collaboration Mode

1. **Structure first** - Present slide titles as outline, get approval on argument flow
2. **Iterate content** - Fill in sections, checking against principles
3. **Refine design** - Adjust theme, visuals, spacing
4. **Polish** - Speaker notes, transitions, final checklist review

## Session Memory

This project uses session memory for continuity between conversations.

- **At session start**: Read `.claude/STARTUP_PROTOCOL.md` for context from previous sessions
- **At session end**: Run `./scripts/archive-session.sh` to save the session
- **Search past work**: `rg -l "term" .session_logs/`
