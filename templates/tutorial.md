# Template: Tutorial / How-To

Use this template when teaching a skill, process, or procedure. The audience needs to learn how to do something and should be able to follow along or reference later.

---

## Audience Profile

- Learning a new skill or process
- May follow along in real-time or reference later
- Need clear steps they can replicate
- Benefit from seeing common mistakes

---

## Structure

### Section 1: Context (Slides 1-3)

**Slide 1 — Title**
- Clear statement of what they'll learn
- Expected outcome

**Slide 2 — Why This Matters**
- When you'd use this skill
- Problem it solves
- What's possible after learning this

**Slide 3 — Prerequisites & Setup**
- What they need before starting
- Environment/tools required
- What to have ready

### Section 2: The Process (Slides 4-N)

**One slide per step** — Each step should be:
- Numbered
- Self-contained (can be referenced individually)
- Include visual if helpful
- Note common pitfalls

### Section 3: Putting It Together (Slides N+1 to N+3)

**Complete Example Slide**
- Show the full process applied to a real scenario

**Common Mistakes Slide**
- What often goes wrong
- How to fix or avoid

**Variations/Advanced Slide**
- Alternative approaches
- Where to go next

### Section 4: Reference (Final slides)

**Summary / Cheat Sheet**
- Quick reference of all steps
- Key commands or syntax

**Resources**
- Where to learn more
- Practice exercises

---

## Marp Skeleton

```markdown
---
marp: true
theme: plato
paginate: true
header: 'Tutorial: [Skill Name]'
---

<!-- _class: title -->

# How to [Do Thing]

**By the end, you'll be able to [specific outcome]**

---

# Why learn this?

**Use case**: [When you'd need this]

**Problem solved**: [What pain point this addresses]

**Outcome**: [What becomes possible]

---

# Before you start

**Prerequisites**:
- [Prerequisite 1]
- [Prerequisite 2]

**You'll need**:
- [Tool/resource 1]
- [Tool/resource 2]

**Time required**: ~[X] minutes

---

<!-- _class: transition -->

# The Process

---

# Step 1: [Action verb] [object]

[Brief explanation of what this step accomplishes]

```
[Code, command, or example]
```

**What you should see**: [Expected result]

⚠️ **Watch out**: [Common mistake at this step]

---

# Step 2: [Action verb] [object]

[Brief explanation of what this step accomplishes]

```
[Code, command, or example]
```

**What you should see**: [Expected result]

---

# Step 3: [Action verb] [object]

[Brief explanation of what this step accomplishes]

```
[Code, command, or example]
```

**What you should see**: [Expected result]

💡 **Tip**: [Helpful hint]

---

# Step 4: [Action verb] [object]

[Brief explanation of what this step accomplishes]

```
[Code, command, or example]
```

**What you should see**: [Expected result]

---

# Step 5: [Action verb] [object]

[Brief explanation of what this step accomplishes]

```
[Code, command, or example]
```

**Done!** You should now have [outcome].

---

<!-- _class: transition -->

# Putting it together

---

# Complete Example: [Scenario]

**Starting point**: [Initial state]

```
[Full sequence of commands/steps]
```

**Result**: [Final state]

---

# Common Mistakes

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| [Mistake 1] | [Cause] | [Solution] |
| [Mistake 2] | [Cause] | [Solution] |
| [Mistake 3] | [Cause] | [Solution] |

---

# Variations & Next Steps

**Alternative approach**: [Different way to achieve same result]

**Advanced usage**: [More sophisticated application]

**Related skills**: [What to learn next]

---

# Quick Reference

| Step | Action | Command/Syntax |
|------|--------|----------------|
| 1 | [Action] | `[command]` |
| 2 | [Action] | `[command]` |
| 3 | [Action] | `[command]` |
| 4 | [Action] | `[command]` |
| 5 | [Action] | `[command]` |

---

# Resources

**Documentation**: [Link]

**Practice exercises**: [Link or description]

**Help**: [Where to get help]

**Related tutorials**: [What to learn next]
```

---

## Key Principles for Tutorials

**One step per slide.** Don't combine steps. People reference individual steps when stuck.

**Show expected results.** After each step, tell them what they should see. This confirms they're on track.

**Anticipate failures.** Call out common mistakes where they typically occur, not in a separate "troubleshooting" section at the end.

**Concrete examples.** Abstract explanations don't teach. Specific examples do.

**Scannable format.** When someone returns to reference step 3, they shouldn't have to read steps 1 and 2 again.

---

## Customization Notes

- For longer processes, group steps into phases with transition slides
- For code-heavy tutorials, ensure code blocks are readable (not too small)
- Add screenshots or diagrams where visual confirmation helps
- Consider splitting into multiple decks for complex topics
