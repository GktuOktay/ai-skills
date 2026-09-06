---
name: Brandkit Management
description: "Marka tutarlılığını sağlamak için marka kimliği, logo kullanımı, tipografi, renk paletleri ve görsel kuralların yönetimi."
alwaysApply: false
---

# Brandkit Management Guidelines

This skill provides comprehensive instructions for applying brand identity assets to frontend components, ensuring consistency across all visual touchpoints.

## 1. Brand Consistency & Tone of Voice

Consistency builds trust. Every UI component and copy snippet should align with the core brand values.
- **Tone:** Professional, accessible, and forward-thinking.
- **Application:** Use consistent terminology. Do not mix playful and strictly formal tones unless specified by the campaign.

## 2. Logo Usage Rules

The logo is the primary visual identifier. Maintain its integrity at all times.

- **Clear Space:** Always maintain a minimum clear space around the logo equal to the height of the logo icon.
- **Minimum Size:** For digital use, the logo should never be smaller than `24px` in height.
- **Backgrounds:** Use the primary full-color logo on light backgrounds. Use the white monochrome logo on dark or busy backgrounds.
- **Don'ts:** Do not stretch, distort, add drop shadows, or change the colors of the logo.

## 3. Typography Hierarchy

Consistent typography establishes a visual rhythm and guides the user's attention.

| Level | Font Family | Size (Desktop/Mobile) | Weight | Line Height |
| :--- | :--- | :--- | :--- | :--- |
| **H1 (Display)** | Primary Sans | 48px / 36px | Bold (700) | 1.2 |
| **H2 (Section)** | Primary Sans | 32px / 28px | SemiBold (600) | 1.3 |
| **H3 (Subsection)** | Primary Sans | 24px / 20px | Medium (500) | 1.4 |
| **Body (Main)** | Secondary Serif | 16px / 16px | Regular (400) | 1.5 |
| **Small/Caption** | Primary Sans | 14px / 14px | Regular (400) | 1.5 |

## 4. Color Palettes

Colors evoke emotions and highlight actions. Stick to the predefined palette.

### Primary Colors
- **Brand Primary:** `#0055FF` (Actionable items, primary buttons, links)
- **Brand Dark:** `#1A1A1A` (Primary text, dark mode backgrounds)
- **Brand Light:** `#F8F9FA` (Backgrounds, cards, secondary panels)

### Secondary/Semantic Colors
- **Success:** `#00C853` (Validations, success states)
- **Warning:** `#FFAB00` (Alerts, non-destructive warnings)
- **Error:** `#D50000` (Destructive actions, error messages)
- **Neutral/Gray:** `#757575` (Secondary text, borders, disabled states)

## 5. Visual Motifs & UI Application

When applying these guidelines to code (e.g., Tailwind CSS, Styled Components):

- **Border Radius:** Use `4px` for small elements (inputs, tags) and `8px` for larger containers (cards, modals) to maintain a modern, sharp look.
- **Shadows:** Use soft, diffused shadows to elevate interactive elements.
  - *Rest:* `box-shadow: 0 2px 4px rgba(0,0,0,0.05)`
  - *Hover:* `box-shadow: 0 4px 12px rgba(0,0,0,0.1)`
- **Motifs:** Incorporate subtle geometric background patterns at `5%` opacity for branded sections.

### Code Implementation Checklist
- [ ] Are CSS variables or design tokens used instead of hardcoded hex values?
- [ ] Is typography responsive across mobile, tablet, and desktop breakpoints?
- [ ] Do button states (hover, active, disabled) reflect the brand palette?
- [ ] Is contrast ratio AAA or AA compliant for accessibility?
