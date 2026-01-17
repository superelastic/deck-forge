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
![bg](image.png)           # Full background
![bg left](image.png)      # Left half background
![bg right:40%](image.png) # Right 40% background
![width:500px](image.png)  # Inline with size
```

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
