# Template: Project Update / Status Report

Use this template for regular status updates, progress reports, or project reviews. The audience needs to quickly understand: Where are we? What's changed? What's next?

---

## Audience Profile

- Stakeholders tracking multiple projects
- Need to know status without reading details
- Looking for: progress, blockers, decisions needed
- Limited time — often reviewing many updates

---

## Structure

### Section 1: The Bottom Line (Slides 1-2)

**Slide 1 — Title + Status**
- Project name
- Overall status indicator (On Track / At Risk / Blocked)
- One-sentence summary

**Slide 2 — Executive Summary**
- Status: [One line]
- Key accomplishment this period: [One line]
- Key risk/blocker: [One line]
- Decision/help needed: [One line, or "None"]

### Section 2: Progress (Slides 3-5)

**Slide 3 — Milestone Status**
- Visual timeline or checklist
- What's done, what's in progress, what's upcoming

**Slide 4 — Key Accomplishments**
- 2-3 specific things completed this period
- Each stated as achievement, not activity

**Slide 5 — Metrics/KPIs (if applicable)**
- Key numbers that show progress
- Trend indicators

### Section 3: Challenges (Slides 6-7)

**Slide 6 — Risks and Issues**
- Current blockers
- Emerging risks
- Status of previously reported issues

**Slide 7 — Decisions Needed**
- What you need from this audience
- By when
- Options if applicable

### Section 4: What's Next (Slides 8-9)

**Slide 8 — Next Period Plan**
- Key activities for next period
- Expected milestones

**Slide 9 — Timeline View**
- Updated project timeline
- Key dates highlighted

---

## Marp Skeleton

```markdown
---
marp: true
theme: plato
paginate: true
header: '[Project Name] Status Update'
footer: '[Date]'
---

<!-- _class: title -->

# [Project Name] 
## Status Update — [Period]

🟢 On Track | 🟡 At Risk | 🔴 Blocked

---

# Executive Summary

| | |
|---|---|
| **Status** | 🟢 On Track — [One sentence summary] |
| **This period** | [Key accomplishment] |
| **Risk/Blocker** | [Main concern, or "None"] |
| **Need from you** | [Decision/help needed, or "None — FYI only"] |

---

# Milestone Progress

```
[Completed] ───●─── [Completed] ───●─── [In Progress] ───○─── [Upcoming]
   Jan 15           Feb 1              Feb 15              Mar 1
     ✓                ✓                  ◐                   ○
```

| Milestone | Target | Status |
|-----------|--------|--------|
| [Milestone 1] | Jan 15 | ✅ Complete |
| [Milestone 2] | Feb 1 | ✅ Complete |
| [Milestone 3] | Feb 15 | 🔄 In Progress (80%) |
| [Milestone 4] | Mar 1 | ○ Not Started |

---

# Key Accomplishments This Period

1. **[Accomplishment 1]**
   [Brief context — why this matters]

2. **[Accomplishment 2]**
   [Brief context — why this matters]

3. **[Accomplishment 3]**
   [Brief context — why this matters]

---

# Metrics

| Metric | Last Period | This Period | Target | Trend |
|--------|-------------|-------------|--------|-------|
| [Metric 1] | [Value] | [Value] | [Value] | ↑ |
| [Metric 2] | [Value] | [Value] | [Value] | → |
| [Metric 3] | [Value] | [Value] | [Value] | ↓ |

---

# Risks and Issues

| Item | Severity | Status | Mitigation |
|------|----------|--------|------------|
| 🔴 [Blocker] | High | Active | [What we're doing] |
| 🟡 [Risk] | Medium | Monitoring | [What we're doing] |
| 🟢 [Resolved] | — | Closed | [How it was resolved] |

---

# Decision Needed

**Question**: [Specific question requiring decision]

**Options**:
- **Option A**: [Description] — [Pros/cons]
- **Option B**: [Description] — [Pros/cons]

**Recommendation**: [Your recommendation]

**Needed by**: [Date]

---

# Next Period Plan

**Focus areas**:
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

**Key dates**:
- [Date]: [Event/milestone]
- [Date]: [Event/milestone]

---

# Updated Timeline

```
        Jan        Feb        Mar        Apr        May
         │          │          │          │          │
Phase 1  ████████████│          │          │          │  ✅ Complete
Phase 2             │██████████│          │          │  🔄 In Progress
Phase 3             │          │██████████│          │  ○ Planned
Phase 4             │          │          │██████████│  ○ Planned
         │          │          │          │          │
                            ▲
                         We are here
```

---

# Appendix: Detailed Metrics

[Additional data for reference]
```

---

## Status Indicators

Use consistent indicators across all updates:

| Indicator | Meaning | When to Use |
|-----------|---------|-------------|
| 🟢 On Track | Proceeding as planned | Default state |
| 🟡 At Risk | May miss targets without intervention | Problems emerging |
| 🔴 Blocked | Cannot proceed | Waiting on external dependency or decision |
| ✅ Complete | Finished | Milestone achieved |
| 🔄 In Progress | Actively being worked | Current focus |
| ○ Not Started | Future work | Upcoming |

---

## Key Principles for Status Updates

**Lead with status.** Don't make people read 10 slides to find out if the project is in trouble.

**Accomplishments, not activities.** Not "worked on testing" but "completed integration testing for all endpoints."

**Be honest about risks.** Surfacing problems early builds trust. Surprises erode it.

**Specific asks.** If you need something, be specific about what, from whom, by when.

**Consistent format.** Use the same structure every time so stakeholders know where to look.

---

## Customization Notes

- For weekly updates, compress to 4-5 slides
- For monthly/quarterly reviews, expand metrics and accomplishments
- Add appendix with detailed data for audiences who want to dig in
- Adapt status indicators to match organizational standards
