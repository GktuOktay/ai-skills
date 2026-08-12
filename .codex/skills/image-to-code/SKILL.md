---
name: Image to Code Conversion
description: "Converts screenshots, mockups, or Figma design files into pixel-perfect, responsive code. / TR: Ekran görüntüleri, mockup'lar veya tasarım dosyalarını (Figma vb.) analiz ederek piksel mükemmelliğinde, duyarlı (responsive) ve temiz koda dönüştürme."
---

# Image to Code Conversion Skill

## Overview
This skill defines the systematic process for analyzing static images (screenshots, design mockups) and translating them into high-quality, production-ready frontend code (HTML/CSS, React, SwiftUI, etc.). The goal is pixel-perfect accuracy, responsive behavior, and semantic structure.

## Phase 1: Visual Analysis Workflow

Before writing any code, systematically break down the image.

### 1. Structural Layout
- **Identify the Grid/Layout Model**: Is it a column-based layout, a grid of cards, or a single column? (Flexbox vs. CSS Grid).
- **Macro Regions**: Divide the design into header, sidebar, main content area, and footer.
- **Alignment & Spacing**: Mentally measure the gaps. Are they consistent? (e.g., 16px, 24px, 32px gaps).

### 2. Component Identification
Break down regions into reusable components:
- Buttons (primary, secondary, icon-only)
- Cards
- Input fields and forms
- Badges/Tags
- Navigation items

### 3. Style Extraction (Educated Guessing)
- **Colors**: Identify the primary brand color, background colors, text colors (primary, secondary, muted), and border colors.
- **Typography**: Estimate font families (serif, sans-serif, monospace), weights (regular, medium, bold), and sizing hierarchy (H1 down to captions).
- **Radii & Shadows**: Note corner rounding (e.g., 4px subtle, 999px pill, 16px card) and the direction/softness of drop shadows.

## Phase 2: Reconstruction Strategy

### 1. The Semantic Skeleton (HTML/JSX)
Always start by writing semantic HTML without styles.
- Use `<header>`, `<main>`, `<section>`, `<article>`, `<nav>`, `<aside>`.
- Ensure accessibility: use `<button>` for actions, `<a>` for links, and add `aria-labels` for icon-only buttons.

```html
<!-- Example of a good structural skeleton -->
<article class="card">
  <div class="card-image-wrapper">
    <img src="..." alt="..." />
  </div>
  <div class="card-content">
    <span class="badge">Technology</span>
    <h3 class="title">Understanding AI</h3>
    <p class="description">A deep dive into...</p>
    <div class="card-footer">
      <div class="author">...</div>
      <button>Read More</button>
    </div>
  </div>
</article>
```

### 2. Layout Implementation (CSS)
Apply CSS starting from the outside in.
- **Container limits**: Set `max-width` and `margin: 0 auto` for page constraints.
- **Flexbox/Grid**: Implement the macro layout.
- **Spacing**: Apply `gap`, `padding`, and `margin`.

### 3. Detail Styling
- Apply typography rules (font-size, line-height, color, weight).
- Apply visual treatments (border-radius, box-shadow, background-color).
- Refine alignment (e.g., `align-items: center` for icon + text).

## Phase 3: Responsive Adaptation

Static images usually show one viewport (desktop or mobile). You must intelligently infer the other viewports.

- **Mobile First or Desktop First**: Choose based on the source image, but ensure constraints are fluid.
- **Stacking**: Side-by-side elements on desktop should stack vertically on mobile (e.g., `flex-direction: column`).
- **Typography Scaling**: Reduce heading sizes on mobile.
- **Touch Targets**: Ensure interactive elements are at least 44x44px for touch interfaces.

## Framework-Specific Patterns

### Tailwind CSS
Use utility classes to rapidly match the design system.
```html
<div class="flex flex-col md:flex-row gap-6 p-6 bg-white rounded-2xl shadow-lg">...</div>
```

### React / Component Architectures
Extract repeated elements into components with props.
```jsx
// Convert a list of identical UI elements into a map
{items.map(item => (
  <Card key={item.id} title={item.title} image={item.image} />
))}
```

### SwiftUI
Leverage `VStack`, `HStack`, and `ZStack` directly correlating to flex directions.
```swift
VStack(alignment: .leading, spacing: 16) {
    Image("thumbnail").resizable().scaledToFit()
    Text("Title").font(.title2).bold()
}
.padding()
.background(Color.white)
.cornerRadius(12)
```

## Common Pitfalls to Avoid

1. **Hardcoding Heights**: Never hardcode `height: 500px` on a container containing text. Let the content dictate the height (use `min-height` if necessary).
2. **Ignoring Line Height**: Text looks wrong if `line-height` is not adjusted. Headings need tight line-height (1.1 - 1.2), body text needs loose line-height (1.5 - 1.6).
3. **Absolute Positioning Abuse**: Avoid `position: absolute` for layout purposes; use Flexbox/Grid instead.
4. **Missing States**: Don't forget to code `:hover`, `:focus`, and `:active` states for interactive elements, even if they aren't in the static image.

## Step-by-Step Execution Checklist
- [ ] Analyze image for layout grid and components.
- [ ] Extract inferred color palette and typography scale.
- [ ] Write raw, unstyled semantic HTML/JSX.
- [ ] Apply CSS Flexbox/Grid for structural layout.
- [ ] Apply padding, margins, and gaps.
- [ ] Apply typography, colors, borders, and shadows.
- [ ] Add responsive media queries.
- [ ] Add interactive states (hover/focus).
- [ ] Review against original image for optical alignment.
