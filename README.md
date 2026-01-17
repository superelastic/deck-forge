# Deck Forge

AI-assisted presentation creation following established rhetorical and design principles.

## Overview

Deck Forge is a Claude Code project that helps create effective slide presentations by combining:

- **Rhetorical principles** — Proven patterns for structuring arguments (Pyramid Principle, assertion titles, etc.)
- **Visual design** — Marp themes adapted for different contexts
- **LLM collaboration** — Work with Claude to develop both content and design

## Quick Start

### Prerequisites

```bash
# Install Marp CLI
npm install -g @marp-team/marp-cli

# Or use npx (no install)
npx @marp-team/marp-cli --version
```

### Create a Presentation

1. **Start a conversation** with Claude in this project
2. **Describe what you need**:
   - "Create a deck explaining [topic] for [audience]"
   - "Help me build a proposal for [recommendation]"
   - "I need a project status update for [project]"
3. **Iterate** on structure, content, and design
4. **Build** the final output

### Build Commands

```bash
# Preview in browser (live reload)
./scripts/build.sh preview my-deck.md

# Export to HTML
./scripts/build.sh html my-deck.md

# Export to PDF
./scripts/build.sh pdf my-deck.md

# Export to PowerPoint
./scripts/build.sh pptx my-deck.md

# Export all formats
./scripts/build.sh all my-deck.md
```

## Project Structure

```
deck-forge/
├── SYSTEM.md              # Instructions for Claude
├── principles/            # Rhetorical and design guidelines
│   ├── rhetoric.md        # Core presentation principles
│   ├── pyramid.md         # Minto Pyramid Principle
│   └── visual-hierarchy.md # Visual design principles
├── themes/                # Marp CSS themes
│   ├── corporate/         # Professional/business themes
│   ├── technical/         # Technical/engineering themes
│   └── academic/          # Academic/research themes
├── templates/             # Structural templates by deck type
│   ├── technical-explainer.md
│   ├── project-update.md
│   ├── proposal.md
│   └── tutorial.md
├── scripts/               # Build automation
│   └── build.sh
└── examples/              # Reference presentations
```

## Templates

| Template | Use Case |
|----------|----------|
| `technical-explainer` | Explaining how a system or technology works |
| `project-update` | Status reports and progress updates |
| `proposal` | Recommendations requiring a decision |
| `tutorial` | Teaching a skill or process |

## Themes

Themes are organized by context:

- **corporate/** — Clean, professional aesthetics for business presentations
- **technical/** — Optimized for code, diagrams, and data
- **academic/** — Formal styles suitable for research and education

To use a theme, specify it in your deck's frontmatter:

```yaml
---
marp: true
theme: plato
paginate: true
---
```

## Core Principles

These are the non-negotiable guidelines encoded in this project:

1. **One idea per slide** — If you can't state the slide's idea in one sentence, split it
2. **Titles are assertions** — Not "Results" but "Treatment increased efficiency by 40%"
3. **Lead with conclusions** — Pyramid Principle: claim → evidence → implications
4. **Visual hierarchy signals importance** — Size, position, and whitespace do cognitive work
5. **Find structure beyond bullets** — Sequences, contrasts, hierarchies, causal chains

See `principles/rhetoric.md` for the complete guide.

## Working with Claude

When collaborating on a deck:

1. **Claude will ask clarifying questions** — Audience, purpose, constraints
2. **Structure comes first** — Review slide titles as an outline before filling in content
3. **Iterate in sections** — Work through one section at a time
4. **Design comes last** — Content and structure before visual polish

## Customization

### Adding Themes

Place CSS files in the appropriate `themes/` subdirectory. Theme files should start with:

```css
/* @theme my-theme-name */
@import 'default';

/* Your styles */
```

### Creating New Templates

Add markdown files to `templates/` following the existing format:
- Document the audience and use case
- Provide the structural outline with guidance
- Include a Marp skeleton that can be copy-pasted

### Modifying Principles

Edit files in `principles/` to adjust the guidelines Claude follows. Changes take effect in new conversations.

## Examples

### Technical Explainer

```markdown
---
marp: true
theme: plato
paginate: true
---

# Kubernetes pods run containers as a unit of deployment

**Containers share networking and storage within a pod**

---

# Three components define every pod

1. **Containers** — The actual workloads
2. **Volumes** — Shared storage
3. **Network namespace** — Shared IP and ports

---
```

### Proposal

```markdown
---
marp: true
theme: einstein
paginate: true
---

# We should migrate to the new API before Q3

**Current API reaches end-of-support in August**

---

# Executive Summary

| | |
|---|---|
| **Situation** | Running on legacy API v2 |
| **Problem** | End-of-support August 2025 |
| **Recommendation** | Complete migration by June |
| **Impact** | Avoid 2-week emergency migration |

---
```

## Credits

- Rhetorical principles adapted from Barbara Minto (Pyramid Principle), Garr Reynolds (Presentation Zen), and Nancy Duarte (slide:ology)
- Marp themes adapted from [marpstyle](https://github.com/cunhapaulo/marpstyle) by Paulo Cunha
- Marp ecosystem by [Yuki Hattori](https://github.com/yhatt)

## License

MIT
