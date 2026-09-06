---
name: imagegen-frontend
description: "Frontend projeleri için yapay zeka görsel oluşturma rehberi: web hero görselleri, mobil varlıklar, ikonlar ve pazarlama görselleri."
---

# Image Generation for Frontend — Web & Mobile

A unified guide for generating, integrating, and optimizing AI-created images across web and mobile frontend projects. Covers prompt engineering, asset pipeline, and platform-specific best practices.

---

## 1. Prompt Engineering for Frontend Assets

### Prompt Structure Formula
```
[Subject] + [Style] + [Composition] + [Lighting] + [Color Palette] + [Technical Specs]
```

### Style Presets by Use Case

#### Hero / Landing Page Backgrounds
```
Prompt pattern:
"Abstract [theme] background, smooth gradient, soft bokeh lights,
[brand color] and [accent color] palette, 16:9 aspect ratio,
high resolution, minimal, modern, clean negative space"

Example:
"Abstract geometric mesh background, smooth gradient transitions,
soft purple and indigo tones with subtle pink accents,
16:9 aspect ratio, 4K resolution, dark theme, minimal and premium feel"
```

#### App UI Illustrations (Onboarding, Empty States, Features)
```
Prompt pattern:
"Flat illustration of [scene/concept], [art style] style,
[2-3 colors] color scheme, clean vector look, white/transparent background,
centered composition, suitable for mobile app UI"

Example:
"Flat illustration of a person organizing tasks on a digital board,
minimal geometric style, blue and coral color scheme,
clean vector look, white background, centered, friendly and modern"
```

#### Product Mockups & Screenshots
```
Prompt pattern:
"[Device type] mockup displaying [UI description],
[environment/setting], professional product photography style,
soft studio lighting, shallow depth of field, [angle]"

Example:
"iPhone 15 Pro mockup displaying a fitness tracking dashboard,
on a minimal white desk with soft shadows,
professional product photography, 45-degree angle, studio lighting"
```

#### Icons & Small Assets
```
Prompt pattern:
"Single [object] icon, [style] style, [color] on [background],
simple, centered, 1:1 aspect ratio, suitable for app icon / UI icon"

Example:
"Single rocket icon, line art with gradient fill, purple to blue,
on transparent background, simple, centered, 1:1, modern SaaS style"
```

#### Blog / Content Images
```
Prompt pattern:
"Editorial illustration for article about [topic],
[art style], [mood], [color palette], 3:2 aspect ratio,
professional quality, suitable for tech blog header"
```

---

## 2. Asset Specifications by Platform

### Web Assets
| Asset Type | Recommended Size | Format | Notes |
|---|---|---|---|
| Hero background | 1920×1080 (2x: 3840×2160) | WebP, AVIF (fallback JPG) | Compress to < 200KB |
| Card thumbnail | 600×400 | WebP | Lazy load |
| Blog header | 1200×630 | WebP, JPG | Also used for OG meta image |
| Favicon | 32×32, 180×180, 512×512 | PNG, SVG | Multi-size for all platforms |
| Logo | SVG (vector) | SVG | Never rasterize logos |
| Background pattern | 400×400 (tileable) | PNG, SVG | Use `background-repeat` |

### iOS / macOS Assets
| Asset Type | Sizes | Format | Notes |
|---|---|---|---|
| App Icon | 1024×1024 (source) | PNG | Xcode generates all sizes |
| Onboarding illustration | 750×750 @2x, 1125×1125 @3x | PNG, PDF (vector) | Asset Catalog |
| Tab bar icon | 25×25 @1x → 75×75 @3x | PDF (vector preferred) | Template rendering mode |
| Launch screen image | Device-specific | PNG | Use storyboard constraints |

### Android Assets
| Asset Type | Sizes | Format | Notes |
|---|---|---|---|
| Adaptive Icon | 108×108dp (432×432px @4x) | PNG, XML vector | Foreground + background layers |
| Feature graphic | 1024×500 | PNG, JPG | Play Store listing |
| Notification icon | 24×24dp | XML vector | White silhouette only |
| Splash screen | Centered 200×200dp | XML vector, PNG | Use SplashScreen API |

---

## 3. Integration Patterns

### Web — Responsive Image Delivery
```html
<picture>
  <source srcset="hero.avif" type="image/avif">
  <source srcset="hero.webp" type="image/webp">
  <img
    src="hero.jpg"
    alt="Descriptive alt text for accessibility"
    width="1920"
    height="1080"
    loading="lazy"
    decoding="async"
  />
</picture>
```

### Web — CSS Background with Generated Image
```css
.hero {
  background-image:
    linear-gradient(135deg, rgba(0,0,0,0.4), rgba(0,0,0,0.1)),
    url('/images/hero-bg.webp');
  background-size: cover;
  background-position: center;
  min-height: 80vh;
}
```

### React / Next.js — Optimized Image Component
```jsx
import Image from 'next/image';

<Image
  src="/illustrations/onboarding-1.webp"
  alt="Welcome illustration"
  width={600}
  height={400}
  priority={isAboveFold}
  placeholder="blur"
  blurDataURL={blurPlaceholder}
/>
```

### SwiftUI — Asset Catalog Image
```swift
Image("onboarding-welcome")
    .resizable()
    .aspectRatio(contentMode: .fit)
    .frame(maxWidth: 300)
    .accessibilityLabel("Welcome illustration")
```

---

## 4. Optimization Pipeline

### Compression Targets
| Format | Quality | Target Size | Tool |
|---|---|---|---|
| AVIF | q=50-65 | < 100KB (hero) | `sharp`, `squoosh` |
| WebP | q=75-80 | < 150KB (hero) | `cwebp`, `sharp` |
| JPG (fallback) | q=80-85 | < 250KB (hero) | `mozjpeg`, `sharp` |
| PNG (icons/illustrations) | lossless | < 50KB | `pngquant`, `oxipng` |
| SVG | minified | < 10KB | `svgo` |

### Automated Build Pipeline
```bash
# Convert and optimize all images in a directory
npx sharp-cli --input ./src/images/*.png --output ./public/images/ --format webp --quality 80
npx sharp-cli --input ./src/images/*.png --output ./public/images/ --format avif --quality 60
```

### Performance Checklist
- [ ] All images have explicit `width` and `height` to prevent CLS (Cumulative Layout Shift)
- [ ] Above-fold images use `loading="eager"` or `priority`; below-fold use `loading="lazy"`
- [ ] `alt` text is descriptive and meaningful (not "image1.png")
- [ ] Modern formats (WebP/AVIF) served with `<picture>` fallback
- [ ] Image CDN or responsive `srcset` for multiple resolutions
- [ ] SVG used for icons, logos, and simple illustrations (not raster)

---

## 5. Design Consistency Rules

### Maintaining Visual Cohesion with AI-Generated Images
1. **Lock your color palette** — Include exact brand hex/HSL values in every prompt
2. **Lock your style** — Use the same style keywords consistently (e.g., always "flat geometric" or always "3D isometric")
3. **Lock your lighting** — Keep lighting direction and mood consistent across all assets
4. **Post-process uniformly** — Apply the same color grading/filter to all generated images
5. **Create a prompt template** — Document your working prompts and reuse them

### Anti-Patterns
- ❌ Mixing illustration styles (flat + 3D + realistic in the same app)
- ❌ Using AI-generated faces for user avatars (uncanny valley risk)
- ❌ Generating text within images (AI text rendering is unreliable)
- ❌ Using uncompressed AI output directly (always optimize)
- ❌ Ignoring aspect ratio — always specify in the prompt
