# Project Scratchpad

Last updated: 2026-01-25

## Currently Working On

(Nothing active)

## Open Items

### PDF Extraction and Transposition (Deferred)

**Goal:** Extract charts/diagrams from input PDFs and transpose to slides when they already have visual representation.

**Decision tree:**
```
Input has existing visual for concept?
├── Yes → Extract and transpose (preserve author intent)
└── No → Generate with Mermaid/Matplotlib
```

**Requirements:**
- PDF parsing library (pymupdf or pdfplumber)
- Image extraction with quality detection (vector vs raster)
- Association logic: link extracted images to relevant slide content
- Format conversion if needed (embedded format → slide-compatible)

**Open questions:**
- How to identify decorative images vs. meaningful charts?
- Quality threshold for extraction vs. regeneration?
- How to handle multi-page diagrams?

### MermaidSeqBench Integration (Deferred)

**Resource:** [MermaidSeqBench](https://huggingface.co/datasets/ibm-research/MermaidSeqBench) (IBM Research)
- 132 validated natural language → Mermaid sequence diagram pairs
- Ready-to-use golden files for sequence diagram testing
- Could expand test coverage beyond flowcharts

### LLM-as-Judge Semantic Validation (Deferred)

For cases where structural validation isn't enough:
- Second Claude call evaluates "does this diagram represent this prose?"
- Useful for spot-checking or complex diagrams
- Adds cost but catches semantic mismatches

## Completed

- [x] Fixed broken `{principles,themes` directory (failed brace expansion artifact)
- [x] Created DriveNets explainer deck (12 slides, turing theme) - moved to ~/presentations/
- [x] Validated Marp build pipeline works correctly
- [x] Tested deck creation workflow end-to-end
- [x] Established deck delivery workflow: create → review → move to ~/presentations/
- [x] Updated CLAUDE.md with delivery workflow documentation
- [x] Updated STARTUP_PROTOCOL.md with orphan deck check (step 3)
- [x] Reviewed and refined quality checklist (comprehensive rewrite with tests)
- [x] Created diagram generation test suite (tests/diagrams/) with PASS/FAIL feedback
- [x] Added visualization heuristics to agent_docs/diagrams-and-charts.md
- [x] Created 7 test fixtures (4 Mermaid, 3 Matplotlib) based on DiagramGenBenchmark patterns
- [x] **2026-01-25: Diagram workflow overhaul**
  - Discovered Mermaid does NOT render natively in Marp (docs were incorrect)
  - Created `scripts/render-mermaid.sh` to pre-render Mermaid → SVG
  - Established two-file workflow: `deck.md` (source) → `deck.rendered.md` (for preview/build)
  - Tested with DriveNets deck (13 diagrams rendered successfully)
  - Documented `![bg right:50% contain]` syntax for split layouts
  - Updated themes with improved `.columns` CSS (flexbox right-justify)
  - Updated `agent_docs/diagrams-and-charts.md` with corrected workflow
  - Updated `agent_docs/marp-syntax.md` with split layout syntax

## Before Session End

- [ ] Clean up test deck: `rm -rf drivenets-network-cloud/`
- [ ] Run `./scripts/archive-session.sh` to save session to .session_logs/
- [ ] Commit documentation changes

## Notes

- Project uses Marp for markdown-to-slides conversion
- Three themes available: plato, heidegger, turing (in themes/{corporate,technical,academic}/)
- Principles in `principles/` should be read before creating slides
- Finished decks go to `~/presentations/`, not kept in project
- Session memory enables deck recreation via re-prompting
- Diagram tests: `.venv/bin/python tests/diagrams/run_tests.py` (matplotlib installed in .venv)
- **Mermaid workflow**: Write in deck.md → render-mermaid.sh → preview deck.rendered.md
