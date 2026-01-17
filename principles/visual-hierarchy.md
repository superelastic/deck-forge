# Visual Hierarchy in Slides

Visual hierarchy is how you guide the viewer's eye and signal what matters. In slides, you have seconds — not minutes — to communicate importance.

---

## The Hierarchy of Visual Weight

Elements compete for attention. Heavier elements win.

**Weight factors (strongest to weakest)**:
1. Size — Bigger = more important
2. Color contrast — High contrast draws the eye
3. Position — Top-left reads first (in Western languages)
4. Isolation — Surrounded by whitespace = important
5. Typography — Bold, different font = emphasis

---

## Size Communicates Importance

The most important element on your slide should be the largest.

```
┌─────────────────────────────────────────┐
│                                         │
│     MAIN POINT IN LARGE TEXT            │
│                                         │
│  Supporting detail in smaller text      │
│                                         │
│  Additional context, smaller still      │
│                                         │
└─────────────────────────────────────────┘
```

**Common mistake**: Making everything the same size. Six equal bullet points say "none of these is more important than the others." The audience decides what to ignore.

---

## Position Creates Reading Order

People scan slides in predictable patterns:

**F-Pattern** (for text-heavy slides):
```
┌─────────────────────────────────────────┐
│ ████████████████████████████████        │
│ █████████████████████                   │
│ ██████████████                          │
│ ████████████████████████                │
│ ███████████████                         │
└─────────────────────────────────────────┘
```

**Z-Pattern** (for sparse slides):
```
┌─────────────────────────────────────────┐
│ START ─────────────────────────► STOP   │
│       ╲                         ╱       │
│         ╲                     ╱         │
│           ╲                 ╱           │
│             ╲             ╱             │
│ THEN ◄───────────────────── CONTINUE    │
└─────────────────────────────────────────┘
```

**Implications**:
- Put the most important thing top-left or center
- End with call-to-action bottom-right
- Don't bury key information in bottom-left

---

## Whitespace Is Not Empty

Whitespace (negative space) does work:
- Groups related elements
- Separates unrelated elements  
- Creates emphasis through isolation
- Reduces cognitive load

**Crowded slide**:
```
┌─────────────────────────────────────────┐
│Title Text Goes Here And It's Very Long  │
│Point 1: Here is the first point about X │
│Point 2: And another point about Y and Z │
│Point 3: Plus this additional thing here │
│Point 4: Don't forget this important bit │
│[Chart][Chart][Chart][Image][Logo][Date] │
└─────────────────────────────────────────┘
```

**Breathing room**:
```
┌─────────────────────────────────────────┐
│                                         │
│            SINGLE KEY POINT             │
│                                         │
│         Supporting statement            │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

---

## Color for Meaning, Not Decoration

Use color to:
- **Highlight** — Draw attention to key data points
- **Group** — Same color = same category
- **Differentiate** — Different colors = different things
- **Signal** — Red = warning/negative, Green = positive (use carefully)

**Don't use color to**:
- Make slides "prettier"
- Fill space
- Differentiate when position would work

**Consistency rule**: If blue means "current state" on slide 3, blue must mean "current state" on slide 15. Random color creates cognitive overhead.

---

## Typography Hierarchy

Establish clear levels:

| Level | Use | Typical Treatment |
|-------|-----|-------------------|
| H1 | Slide title | Largest, bold or semi-bold |
| H2 | Section headers within slide | Medium, bold |
| Body | Main content | Regular weight, readable size |
| Caption | Annotations, sources | Smaller, lighter weight |

**Font pairing**: Most themes use one font for headings, one for body. Don't add a third without reason.

**Minimum readable size**: 18pt for body text (assuming typical projection). If you need smaller, you have too much content.

---

## Data Visualization Hierarchy

When showing charts or tables:

1. **Title states the insight** — Not "Q3 Revenue" but "Q3 Revenue Exceeded Forecast by 12%"

2. **Highlight the key data** — Circle it, color it, enlarge it
```
Revenue by Quarter
                    ┌─────┐
    ████   ████   ██│$14M│██   ████
    ████   ████   ██│ ▲  │██   ████
    ████   ████   ████████████   ████
    ────   ────   ──────────────   ────
     Q1     Q2        Q3           Q4
                   ↑
              Beat forecast
```

3. **Remove chart junk** — No 3D effects, no unnecessary gridlines, no decorative elements

4. **Direct labeling** — Put labels on the data, not in a legend that requires eye movement

---

## Slide Types and Their Hierarchies

### Title Slide
```
┌─────────────────────────────────────────┐
│                                         │
│                                         │
│         PRESENTATION TITLE              │
│         Subtitle or Date                │
│                                         │
│                            Author Name  │
└─────────────────────────────────────────┘
```

### Assertion Slide
```
┌─────────────────────────────────────────┐
│ ASSERTION TITLE (THE MAIN POINT)        │
│                                         │
│    • Supporting evidence                │
│    • Additional support                 │
│                                         │
│                            Source: XYZ  │
└─────────────────────────────────────────┘
```

### Data Slide
```
┌─────────────────────────────────────────┐
│ INSIGHT STATEMENT AS TITLE              │
│                                         │
│    ┌─────────────────────────────┐      │
│    │                             │      │
│    │      CHART (LARGE)          │      │
│    │      with highlighted data  │      │
│    │                             │      │
│    └─────────────────────────────┘      │
│                            Source: XYZ  │
└─────────────────────────────────────────┘
```

### Transition Slide
```
┌─────────────────────────────────────────┐
│                                         │
│                                         │
│              SECTION NAME               │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

---

## Quick Checklist

Before finalizing any slide:

- [ ] Is the most important element the largest?
- [ ] Is there enough whitespace to breathe?
- [ ] Does color usage have meaning (not decoration)?
- [ ] Can this be read from the back of the room?
- [ ] Is there a clear visual starting point?
- [ ] Have I removed everything non-essential?
