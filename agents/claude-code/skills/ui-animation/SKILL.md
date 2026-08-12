---
name: ui-animation
description: "UI animation standards: web/mobile motion terminology, opportunity detection, optimization, and code review. / TR: Uçtan uca kullanıcı arayüzü (UI) animasyon yeteneği: web ve mobil animasyonlar için terminoloji, optimizasyon ve kod incelemesi."
---

# UI Animation — Complete Guide

This skill covers the full lifecycle of UI animations: from identifying where animations add value, through implementation with best practices, to reviewing and optimizing existing animations.

---

## 1. Animation Vocabulary & Taxonomy

### Motion Primitives
| Primitive | CSS / JS Property | Use Case |
|---|---|---|
| **Fade** | `opacity` | Entrance/exit, overlays, skeleton → content |
| **Slide** | `translateX / translateY` | Page transitions, drawers, toasts |
| **Scale** | `scale / transform: scale()` | Modals, cards, hover emphasis |
| **Rotate** | `rotate / transform: rotate()` | Loading spinners, icon state change |
| **Morph** | `clip-path`, `d` (SVG path) | Shape transitions, creative reveals |
| **Color Shift** | `background-color`, `color`, `fill` | State feedback (success/error), theming |
| **Blur** | `filter: blur()` | Depth of field, focus transitions |
| **Stagger** | Sequential delay per child | List/grid entrance, cascade effects |

### Easing Reference
| Name | CSS Value | Personality |
|---|---|---|
| Ease Out Cubic | `cubic-bezier(0.33, 1, 0.68, 1)` | Snappy, responsive (recommended default) |
| Ease In Out Quart | `cubic-bezier(0.76, 0, 0.24, 1)` | Elegant, polished transitions |
| Spring | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Playful, bouncy, delightful |
| Linear | `linear` | Only for infinite loops (spinners, marquees) |

### Duration Guidelines
- **Micro-interactions** (hover, press): `100–200ms`
- **Small transitions** (toggle, tab switch): `200–300ms`
- **Medium transitions** (modal open, slide-in): `300–500ms`
- **Large/page transitions**: `400–700ms`
- **Never exceed `1000ms`** for functional animations

---

## 2. Finding Animation Opportunities

When reviewing a UI, systematically scan for these high-impact animation opportunities:

### High Priority (Always Animate)
1. **Page/Route Transitions** — Fade + subtle slide between pages
2. **Modal & Dialog** — Scale from 0.95 → 1.0 + backdrop fade
3. **Loading States** — Skeleton shimmer, spinner, progress bar
4. **Toast / Notification** — Slide in from edge + auto-dismiss fade
5. **Navigation State** — Active tab indicator slide, hamburger → X morph

### Medium Priority (Strong UX Lift)
6. **List/Grid Item Entrance** — Staggered fade-up on scroll-into-view
7. **Accordion / Collapse** — Smooth height + opacity transition
8. **Hover & Focus States** — Scale, shadow lift, color shift on interactive elements
9. **Form Validation** — Shake on error, checkmark on success
10. **Data Visualization** — Chart bars/lines animate from zero on load

### Low Priority (Polish & Delight)
11. **Scroll-Linked Parallax** — Background layers at different scroll speeds
12. **Cursor Effects** — Custom cursor, magnetic buttons
13. **Easter Eggs** — Confetti on achievement, playful 404 pages
14. **Micro-copy Transitions** — Button label swap ("Save" → "Saved ✓")

### Anti-Patterns to Avoid
- ❌ Animating layout-triggering properties (`width`, `height`, `top`, `left`) — use `transform` instead
- ❌ Animation on every scroll event without `IntersectionObserver` or throttling
- ❌ Motion that blocks user input or slows task completion
- ❌ Inconsistent easing across the same app
- ❌ Ignoring `prefers-reduced-motion` accessibility setting

---

## 3. Implementation Patterns

### CSS Transitions (Simple State Changes)
```css
.card {
  transition: transform 300ms cubic-bezier(0.33, 1, 0.68, 1),
              box-shadow 300ms cubic-bezier(0.33, 1, 0.68, 1);
}
.card:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
}
```

### CSS Keyframes (Multi-Step Animations)
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-in {
  animation: fadeInUp 400ms cubic-bezier(0.33, 1, 0.68, 1) both;
}
```

### Staggered List Entrance
```css
.list-item {
  animation: fadeInUp 400ms cubic-bezier(0.33, 1, 0.68, 1) both;
}
.list-item:nth-child(1) { animation-delay: 0ms; }
.list-item:nth-child(2) { animation-delay: 60ms; }
.list-item:nth-child(3) { animation-delay: 120ms; }
/* Or use: animation-delay: calc(var(--i) * 60ms); with CSS custom property */
```

### Accessibility — Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### JavaScript — Intersection Observer for Scroll Animations
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate-in');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
```

### React / Framer Motion Pattern
```jsx
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  exit={{ opacity: 0, y: -10 }}
  transition={{ duration: 0.35, ease: [0.33, 1, 0.68, 1] }}
>
  {children}
</motion.div>
```

### SwiftUI Pattern
```swift
withAnimation(.spring(response: 0.4, dampingFraction: 0.75)) {
    isExpanded.toggle()
}
```

---

## 4. Reviewing & Optimizing Animations

### Performance Checklist
- [ ] Only `transform` and `opacity` are animated (GPU-composited, no layout/paint)
- [ ] No forced synchronous layout (read then write in the same frame)
- [ ] `will-change` used sparingly and only on elements about to animate
- [ ] Animations are removed/paused when off-screen
- [ ] `requestAnimationFrame` used for JS-driven animations (not `setInterval`)

### Quality Checklist
- [ ] Consistent easing curve across the entire application
- [ ] Duration feels natural — not too fast (jarring) or too slow (sluggish)
- [ ] Entrance and exit animations are paired (don't just fade in without fade out)
- [ ] Stagger delays are uniform (40–80ms between items)
- [ ] `prefers-reduced-motion` is respected with graceful fallback

### Common Issues & Fixes
| Issue | Symptom | Fix |
|---|---|---|
| Jank / dropped frames | Stuttering on mid-range devices | Move to `transform`/`opacity` only |
| Flash of unstyled content | Elements visible before animation starts | Use `animation-fill-mode: both` |
| Competing animations | Multiple animations fight for same property | Use `animation-composition` or sequence |
| Overshooting spring | Element bounces too aggressively | Increase `dampingFraction` or reduce overshoot |
| Scroll-linked jank | Parallax causes frame drops | Use CSS `scroll-timeline` or throttle with rAF |

---

## 5. Animation Libraries Reference

| Library | Platform | Best For |
|---|---|---|
| **Framer Motion** | React | Declarative layout animations, gestures |
| **GSAP** | Vanilla JS | Complex timelines, scroll-triggered sequences |
| **Lottie** | Web / iOS / Android | After Effects → code, icon & illustration animations |
| **CSS (native)** | All | Simple transitions, keyframes, scroll-driven |
| **SwiftUI .animation** | iOS / macOS | Native spring physics, matched geometry |
| **Rive** | Cross-platform | Interactive, state-machine driven animations |
