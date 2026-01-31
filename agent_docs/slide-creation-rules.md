# Slide Creation Rules

Detailed rules with examples. For principles and rationale, see `principles/rhetoric.md`.

## Titles Must Be Assertions

Every slide title must be a complete claim, not a label.

| Bad (Label) | Good (Assertion) |
|-------------|------------------|
| Results | Treatment increased distance by 61 miles on average |
| Architecture Overview | Three components handle all network traffic |
| Key Findings | Customer churn dropped 23% after redesign |
| Next Steps | We recommend launching in Q2 with limited rollout |

**Test:** Can someone understand your main point from the title alone?

## One Idea Per Slide

If you find yourself writing "and also" or "another thing," create another slide.

**Test:** Can you state the slide's idea in one sentence? If not, split it.

## Lead with Conclusions (Pyramid Principle)

Structure every slide as:
1. State the claim (title)
2. Provide evidence (body)
3. Explain implications (if needed)

**Never** build up through: background → analysis → finding. Start with the finding.

## Minimize Bullets

Bullets confess "I couldn't figure out the relationship between these ideas."

Find the hidden structure:
- **Sequence** → use numbers or "First... Then... Finally..."
- **Contrast** → use two-column layout
- **Hierarchy** → use heading levels
- **Causal chain** → use arrows or flow diagram

## Explicit Transitions

Help the audience see structure between sections:
- "So we've established X. Now the question is Y."
- "That's the theory. What about the evidence?"
- "So far I've shown A and B. The last piece is C."

## Visual Hierarchy

What's big is important. What's first is important. What's isolated by white space is important.

Use Marp directives (`_class`, sizing, columns) to create clear hierarchy.

## Content Density and Overflow Prevention

Marp slides have fixed dimensions. Content that exceeds the slide area will overflow into headers/footers or get cut off. **You cannot see the rendered output**, so follow these conservative limits:

### Global Defaults (in frontmatter)

Always include bottom padding and conservative table sizing:

```yaml
style: |
  section {
    padding: 50px 50px 80px 50px;
  }
  table {
    font-size: 0.8em;
  }
```

### Table Guidelines

| Table Size | Font Size | Notes |
|------------|-----------|-------|
| 1-5 rows | `0.9em` | Default is fine |
| 6-8 rows | `0.8em` | Use global default |
| 9-12 rows | `0.75em` | Add scoped style |
| 13+ rows | Split | Break into multiple slides |

For tables with many columns or long cell content, go one size smaller.

### Content Limits Per Slide

- **Max ~8 lines of body text** (excluding title)
- **Max 5-6 bullet points** (prefer fewer)
- **Tables + text**: reduce one or the other
- **Code blocks**: max ~10-12 lines

### When in Doubt

1. Use smaller font sizes preemptively
2. Split content across slides (slides are cheap)
3. Move detail to appendix slides
4. After build, user flags overflow → fix reactively
