# Template: Technical Explainer

Use this template when explaining how a system, technology, or process works to an audience that needs to understand it for the first time or as a refresher.

---

## Audience Profile

- May have adjacent technical knowledge but not this specific domain
- Needs mental model more than implementation details
- Will use this understanding to make decisions or collaborate

---

## Structure

### Section 1: The Punchline (Slides 1-2)

**Slide 1 — Title**
- Clear statement of what you're explaining
- One-sentence summary of what it is/does

**Slide 2 — The Core Insight**
- In one sentence: what is this thing and why does it matter?
- What problem does it solve?
- How is it different from alternatives?

### Section 2: The Mental Model (Slides 3-5)

**Slide 3 — High-Level Architecture**
- Visual diagram showing major components
- No more than 5-7 boxes
- Show relationships/data flow

**Slide 4-5 — Key Components**
- One slide per major component (or group)
- Title: What this component does (assertion)
- Content: How it works at appropriate abstraction level

### Section 3: How It Actually Works (Slides 6-9)

**Slide 6 — Walkthrough Introduction**
- "Let's trace a typical [request/transaction/process]"

**Slides 7-9 — Step-by-Step**
- One step per slide
- Same diagram from Slide 3, with current step highlighted
- Title: What happens at this step (assertion)

### Section 4: Key Considerations (Slides 10-11)

**Slide 10 — Trade-offs / Limitations**
- What this approach sacrifices
- When it's not the right choice
- Common misconceptions

**Slide 11 — Compared to Alternatives**
- Brief comparison to other approaches
- When to choose this vs. alternatives

### Section 5: Wrap-up (Slides 12-13)

**Slide 12 — Summary**
- Return to core insight
- Three things to remember

**Slide 13 — Resources / Next Steps**
- Where to learn more
- How to get started (if applicable)
- Who to contact for questions

---

## Marp Skeleton

```markdown
---
marp: true
theme: plato
paginate: true
header: '[System Name] Overview'
---

<!-- _class: title -->

# [System Name]

**[One sentence: what it is and what it does]**

---

# [System Name] solves [problem] by [approach]

- **The problem**: [Brief description]
- **The solution**: [How this system addresses it]
- **Why it matters**: [Business/technical value]

---

# Three components handle [the core function]

<!-- Diagram placeholder -->

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│Component│────▶│Component│────▶│Component│
│    A    │     │    B    │     │    C    │
└─────────┘     └─────────┘     └─────────┘
```

---

# Component A [does what]

- **Purpose**: [One sentence]
- **Key behavior**: [How it works]
- **Interfaces with**: [What it connects to]

<!--
Speaker notes: Expand on technical details here
-->

---

# Component B [does what]

- **Purpose**: [One sentence]
- **Key behavior**: [How it works]
- **Interfaces with**: [What it connects to]

---

<!-- _class: transition -->

# Let's trace a [request/transaction] through the system

---

# Step 1: [What happens first]

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│Component│────▶│Component│     │Component│
│  A ★    │     │    B    │     │    C    │
└─────────┘     └─────────┘     └─────────┘
```

[Explanation of this step]

---

# Step 2: [What happens next]

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│Component│     │Component│────▶│Component│
│    A    │     │  B ★    │     │    C    │
└─────────┘     └─────────┘     └─────────┘
```

[Explanation of this step]

---

# Step 3: [What happens finally]

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│Component│     │Component│     │Component│
│    A    │     │    B    │     │  C ★    │
└─────────┘     └─────────┘     └─────────┘
```

[Explanation of this step]

---

# [System] trades [X] for [Y]

**Strengths**:
- [Advantage 1]
- [Advantage 2]

**Limitations**:
- [Limitation 1]
- [Limitation 2]

**Best suited for**: [Use cases]

---

# Summary: Three things to remember

1. **[Key point 1]** — [One sentence elaboration]

2. **[Key point 2]** — [One sentence elaboration]

3. **[Key point 3]** — [One sentence elaboration]

---

# Learn more

- **Documentation**: [Link]
- **Code**: [Repository]
- **Questions**: [Contact/channel]
```

---

## Customization Notes

- For simpler systems, collapse Sections 2 and 3
- For complex systems, expand Section 3 with more walkthrough steps
- Add appendix slides for detailed specs if needed for reference
- Adjust depth based on audience technical level
