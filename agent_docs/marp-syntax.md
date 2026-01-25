# Marp Syntax Reference

## Frontmatter

```yaml
---
marp: true
theme: plato
paginate: true
header: 'Project Name'
footer: 'Confidential'
---
```

## Slide Separation

```markdown
---
```

## Slide Classes

```markdown
<!-- _class: title -->      # Title slide styling
<!-- _class: transition -->  # Section transition slide
<!-- _class: lead -->        # Lead/emphasis slide
<!-- _class: small -->       # Smaller text for dense content
<!-- _class: large -->       # Larger text for emphasis
```

## Images

```markdown
![bg](image.png)                    # Full background
![bg left](image.png)               # Left half background
![bg right:40%](image.png)          # Right 40% background
![bg right:50% contain](image.png)  # Right half, scaled to fit (recommended for diagrams)
![width:500px](image.png)           # Inline with size
```

## Split Layouts with Images (Recommended for Diagrams)

Use `![bg right:50% contain]` for two-column text+diagram layouts:

```markdown
## Slide title

![bg right:50% contain](img/diagram.svg)

Text content appears on the left.

- Bullet points
- More details
```

**Options:**
- `right:50%` / `left:50%` — which side, how wide
- `contain` — scale image to fit without cropping
- `cover` — scale image to fill (may crop)

## Multi-column Layout

```markdown
<div class="columns">
<div>

Left content

</div>
<div>

Right content

</div>
</div>
```

## Speaker Notes

```markdown
<!--
These are speaker notes.
Only visible in presenter view.
-->
```

## Available Themes

| Theme | Best For | Aesthetic |
|-------|----------|-----------|
| `plato` | Technical presentations, engineering | Clean, minimal, light |
| `heidegger` | Academic, philosophical | Elegant, serif fonts |
| `turing` | Software, computing topics | Technical, monospace accents |

Themes are in `themes/` directory. Each theme CSS can be customized.
