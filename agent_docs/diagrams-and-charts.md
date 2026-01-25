# Diagrams and Charts

Visual representations should clarify, not impress. Choose the right tool for each visualization type to balance simplicity with fidelity.

## Tool Selection

| Visualization Type | Tool | Rationale |
|--------------------|------|-----------|
| Flowcharts | Mermaid | Native Marp support, no build step, simple syntax |
| Block diagrams | Mermaid | Boxes and arrows with automatic layout |
| Sequence diagrams | Mermaid | Clear actor/message notation |
| State machines | Mermaid | Built-in state diagram support |
| X-Y data plots | Matplotlib → SVG | Data-faithful, vector output, agent-friendly |
| Pie/bar charts | Matplotlib → SVG | Precise control over data representation |
| Complex architecture | Hand-drawn SVG | When auto-layout fails or custom positioning needed |

**The test**: Is there a simpler tool that would work? Use the lightest tool that accurately represents the content.

## When to Visualize

Use these heuristics during deck creation to identify text that benefits from visual representation.

### Text Patterns That Signal Visualization

| Text Pattern | Visualization | Example Trigger |
|--------------|---------------|-----------------|
| Sequential steps (3+) | Flowchart | "First... then... finally..." |
| Decision with branches | Flowchart with diamond | "If X, do Y; otherwise Z" |
| Actor interactions | Sequence diagram | "User sends request to server..." |
| State transitions | State diagram | "Moves from idle to active when..." |
| Quantity comparisons | Bar chart | "A has 40%, B has 25%, C has 35%" |
| Trend over time | Line chart | "Revenue grew from 10M to 50M over 5 years" |
| Part-of-whole | Pie chart | "Budget breakdown: 60% salaries, 25% operations..." |
| Hierarchical structure | Mind map / tree | "Main topic with three subtopics..." |

### When NOT to Visualize

- **Simple lists** — bullets suffice when items are independent
- **Single comparisons** — words are clearer: "A is twice B"
- **Abstract concepts** — without clear structure, visuals mislead
- **When source has adequate visual** — transpose existing diagrams rather than regenerating

**The workflow**: During structure proposal, identify candidate passages. Propose: "Slide 4 could use a flowchart for the approval process." Get approval, then generate.

## Mermaid Diagrams

Mermaid renders natively in Marp. Wrap diagrams in a fenced code block with `mermaid` language.

### Flowcharts

```markdown
```mermaid
flowchart LR
    A[Input] --> B{Decision}
    B -->|Yes| C[Process]
    B -->|No| D[Skip]
    C --> E[Output]
    D --> E
`` `
```

Direction options: `LR` (left-right), `TB` (top-bottom), `RL`, `BT`

Node shapes:
- `[text]` — rectangle
- `(text)` — rounded rectangle
- `{text}` — diamond (decision)
- `((text))` — circle
- `[(text)]` — cylinder (database)

### Sequence Diagrams

```markdown
```mermaid
sequenceDiagram
    participant U as User
    participant S as Server
    participant D as Database

    U->>S: Request data
    S->>D: Query
    D-->>S: Results
    S-->>U: Response
`` `
```

Arrow types:
- `->>` solid with arrowhead
- `-->>` dotted with arrowhead
- `--)` solid with open arrow (async)

### State Diagrams

```markdown
```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing: start
    Processing --> Complete: finish
    Processing --> Error: fail
    Error --> Idle: reset
    Complete --> [*]
`` `
```

### Block Diagrams

```markdown
```mermaid
block-beta
    columns 3
    A["Service A"]:1
    B["Service B"]:1
    C["Service C"]:1
    D["Shared Database"]:3
`` `
```

### Styling Mermaid

Add classes to highlight elements:

```markdown
```mermaid
flowchart LR
    A[Start] --> B[Current Step]
    B --> C[Next]

    style B fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
`` `
```

## Matplotlib Charts (Pre-rendered SVG)

For data plots, generate SVG files using Python and include them as images. This keeps the pipeline simple—only data visualizations need pre-rendering.

### Workflow

1. Create a Python script in the deck's `img/` folder
2. Generate SVG output
3. Reference the SVG in your slide

### Example: Line Chart

```python
# img/generate_charts.py
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
values = [10, 25, 40, 35, 50]

# Create figure
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(months, values, marker='o', linewidth=2, color='#1976d2')
ax.fill_between(months, values, alpha=0.1, color='#1976d2')

# Styling for slides
ax.set_ylabel('Growth (%)', fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(labelsize=11)

# Highlight key point
ax.annotate('Peak', xy=('May', 50), xytext=('Apr', 55),
            arrowprops=dict(arrowstyle='->', color='#d32f2f'),
            fontsize=11, color='#d32f2f')

plt.tight_layout()
plt.savefig('growth_chart.svg', format='svg', transparent=True)
plt.close()
```

### Example: Bar Chart

```python
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
colors = ['#90a4ae', '#90a4ae', '#1976d2', '#90a4ae']  # Highlight C

fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(categories, values, color=colors)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylabel('Count')

# Add value labels
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            str(val), ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('comparison.svg', format='svg', transparent=True)
plt.close()
```

### Slide-Optimized Styling

Charts for slides need different treatment than charts for papers:

| Aspect | Paper/Report | Slide |
|--------|--------------|-------|
| Font size | 8-10pt | 11-14pt |
| Line weight | 1px | 2-3px |
| Gridlines | Often useful | Usually remove |
| Legend | Detailed | Minimal or inline labels |
| Data density | High | Low (highlight 1-2 points) |
| Axis labels | Complete | Essential only |

**The test**: Would someone in the back row understand this chart in 3 seconds?

### Including in Slides

```markdown
---

## Our growth accelerated in Q2

![width:700px](img/growth_chart.svg)

Revenue increased 40% after the platform launch.

---
```

### Running Chart Generation

Add chart generation to your deck workflow:

```bash
cd my-presentation/img
python generate_charts.py
cd ..
./scripts/build.sh preview deck.md
```

## When to Use Each Approach

### Use Mermaid when:
- Showing process flow or relationships
- Diagram structure matters more than exact positioning
- You want easy iteration without regenerating files
- The diagram is part of the explanation, not the data

### Use Matplotlib when:
- Representing actual numerical data
- Precision matters (axes, scales, proportions)
- You need to highlight specific data points
- The chart IS the evidence for your claim

### Use hand-drawn SVG when:
- Auto-layout produces poor results
- You need pixel-perfect positioning
- The diagram is highly custom (not a standard type)
- Mermaid doesn't support the diagram type

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Chart with 10+ data series | Unreadable, defeats purpose | Show 2-3 key series, others in appendix |
| Mermaid for data plots | No axis control, misleading proportions | Use Matplotlib |
| Matplotlib for simple flowchart | Overkill, harder to maintain | Use Mermaid |
| Tiny labels on charts | Unreadable from distance | Increase font size, simplify |
| Rainbow color schemes | Distracting, no meaning | Use 1-2 colors with semantic meaning |
| 3D charts | Distort perception of values | Use 2D—always |

## Mermaid in Marp: Technical Notes

Mermaid support requires the Marp CLI with the `--html` flag enabled. The standard build script handles this.

If diagrams don't render:
1. Check that `marp: true` is in frontmatter
2. Verify code fence uses exactly `mermaid` (lowercase)
3. Test the diagram at [mermaid.live](https://mermaid.live) first
4. Check for syntax errors (missing quotes, brackets)

Large diagrams may need slide class adjustment:
```markdown
<!-- _class: small -->
```
