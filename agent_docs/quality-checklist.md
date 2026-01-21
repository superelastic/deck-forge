# Quality Checklist

Before finalizing any deck, work through this checklist. Items marked with a test have a concrete way to verify.

## Structure

- [ ] **Every title is an assertion** — complete sentence with a claim, not a label
  - *Test*: Read only the titles in sequence. Do they form a coherent argument?
- [ ] **One idea per slide** — no "and also" or "another thing"
  - *Test*: Can you state each slide's idea in one sentence?
- [ ] **Conclusion appears early** — main point in first 2-3 slides, not buried at end
- [ ] **Bullets are justified** — if using bullets, the items are genuinely parallel
  - *Test*: Is there a hidden structure (sequence, contrast, hierarchy, causal chain) that layout could reveal instead?

## Flow

- [ ] **Transitions are explicit** — audience can see structure between sections
  - Look for: "So we've established X. Now..." or transition slides
- [ ] **Repetition reinforces** — main claim echoed, key terms consistent
- [ ] **Summary slide exists** — returns to core insight, 3 things to remember

## Visuals

- [ ] **Visual hierarchy signals importance** — size, position, whitespace used intentionally
  - *Test*: Is it obvious what's most important on each slide?
- [ ] **Figures are simplified** — highlight 1-2 key data points, not everything
  - *Test*: Readable from back of room? If not, it's a handout, not a slide.
- [ ] **Consistent visual language** — same colors/styles mean same things throughout
- [ ] **Right tool for visualization** — Mermaid for flows, Matplotlib for data plots
  - *Test*: Does the diagram type match the content type? (See `agent_docs/diagrams-and-charts.md`)
- [ ] **Charts are slide-optimized** — large fonts, minimal gridlines, 2-3 data series max
  - *Test*: Can you understand the chart's message in 3 seconds?

## Content Balance

- [ ] **Not a document** — slides aren't walls of text; speaker adds value
- [ ] **Not mystery slides** — understandable without presenter (for async review)
- [ ] **Audience-appropriate depth** — trailer not movie; details in appendix/follow-up

## Presentation Mode

*Check the items relevant to your delivery format:*

### For Live Presentation
- [ ] Speaker notes added for complex slides
- [ ] Slides sparse enough that you're the authority, not the slides
- [ ] No "as you can see" with dense figures — you guide the eye

### For Async Review
- [ ] More explicit than live — reader has no presenter to fill gaps
- [ ] "Why" included, not just "what"
- [ ] Context assumptions stated — reader may have forgotten

## Marp Technical

- [ ] Frontmatter complete: `marp: true`, `theme`, `paginate`
- [ ] Theme appropriate for audience (plato/heidegger/turing)
- [ ] Slide separators (`---`) correctly placed
- [ ] Images sized appropriately (`![width:Npx]` or `![bg]`)
- [ ] Multi-column layouts render correctly
- [ ] Mermaid diagrams render (test in preview before export)
- [ ] SVG charts generated and committed to `img/`

## Final Sanity

- [ ] **Slide count reasonable** — ~1 slide per minute of presentation time
- [ ] **No orphan content** — every slide earns its place
- [ ] **Opens strong** — first 3 slides hook the audience and state the point
