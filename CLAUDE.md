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

### Verification

Before completing any deck, run through `agent_docs/quality-checklist.md`.

### File Organization

New decks go in their own folder:
```
my-presentation/
  deck.md          # Content
  img/             # Images
  output/          # Build outputs
```

## Collaboration Mode

1. **Structure first** - Present slide titles as outline, get approval on argument flow
2. **Iterate content** - Fill in sections, checking against principles
3. **Refine design** - Adjust theme, visuals, spacing
4. **Polish** - Speaker notes, transitions, final checklist review
