---
name: Apple Human Interface Guidelines (HIG) Design
description: "Apple Human Interface Guidelines (HIG) design and development standards for iOS, macOS, and visionOS. / TR: iOS, macOS ve visionOS için Apple Human Interface Guidelines (İnsan Arayüzü Yönergeleri) tabanlı uygulama tasarımı ve geliştirme becerisi."
---

# Apple Human Interface Guidelines (HIG) Skill

## Introduction
This skill provides comprehensive guidelines and actionable instructions for building applications that strictly adhere to Apple's Human Interface Guidelines (HIG). The focus is on clarity, deference, and depth, ensuring native-feeling experiences across iOS, macOS, and visionOS.

## Core Apple Design Principles

1. **Clarity**: Text is legible at every size, icons are precise and lucid, adornments are subtle and appropriate, and a sharpened focus on functionality motivates the design. Negative space, color, fonts, graphics, and interface elements subtly highlight important content and convey interactivity.
2. **Deference**: Fluid motion and a crisp, beautiful interface help people understand and interact with content without competing with it. Content typically fills the entire screen, while translucency and blurring often hint at more.
3. **Depth**: Distinct visual layers and realistic motion convey hierarchy, impart vitality, and facilitate understanding. Touch and discoverability heighten delight and enable access to functionality and additional content without losing context.

## Platform Conventions

### iOS Conventions
- **Tab Bars**: Used for top-level navigation. Must contain between 2 and 5 items. Avoid hiding tab bars when navigating deep into a hierarchy unless absolutely necessary.
- **Navigation Bars**: Provide drill-down navigation. Use large titles for root views, reverting to standard titles upon scrolling.
- **Modals & Sheets**: Use sheets for non-blocking contextual tasks. Use full-screen modals for immersive content or complex tasks.
- **Safe Areas**: Always respect safe areas to prevent content from being clipped by the notch, Dynamic Island, or home indicator.

### macOS Conventions
- **Window Anatomy**: Utilize toolbars, sidebars, and content areas effectively. Sidebars are typically translucent (`NSVisualEffectView`).
- **Menus**: Rely heavily on the global menu bar for application commands. Do not duplicate all menu bar actions in the window UI.
- **Pointer Interactions**: Design for hover states and precise clicking, contrasting with iOS's larger touch targets.

### visionOS Conventions (Spatial Computing)
- **Windows, Volumes, and Spaces**: Use windows for 2D interfaces, volumes for 3D content, and spaces for fully immersive experiences.
- **Depth and Glass Materials**: Use Apple's provided glass materials to ensure UI remains legible against diverse physical backgrounds.
- **Eye Tracking and Gestures**: Ensure UI elements are large enough for eye-tracking precision (minimum 60pt spacing center-to-center). Rely on indirect pinch gestures.

## Typography and SF Symbols

### Dynamic Type
Applications must support Dynamic Type to allow users to adjust text size at the system level.

```swift
// Do: Use semantic text styles
Text("Headline")
    .font(.headline)
    .foregroundStyle(.primary)

// Do not: Hardcode font sizes unless strictly necessary
Text("Headline")
    .font(.system(size: 17, weight: .semibold))
```

### SF Symbols
Always use SF Symbols for iconography instead of custom assets where possible, to inherit weight, scale, and hierarchical rendering.

```swift
Image(systemName: "person.crop.circle.fill")
    .symbolRenderingMode(.hierarchical)
    .foregroundStyle(.tint)
    .imageScale(.large)
```

## Dark Mode Best Practices
- **Semantic Colors**: Use semantic system colors (e.g., `Color.primary`, `Color.secondary`, `Color.systemBackground`) which automatically adapt to Dark Mode.
- **Elevations**: In Dark Mode, use base and elevated colors to distinguish between overlapping views (e.g., modals over backgrounds).
- **Vibrancy**: Utilize vibrant materials for text and symbols on top of blurred backgrounds to ensure legibility.

## Accessibility (A11y)

### VoiceOver
Ensure all interactive elements have appropriate accessibility labels, values, and traits.

```swift
Button(action: toggleMute) {
    Image(systemName: isMuted ? "speaker.slash" : "speaker")
}
.accessibilityLabel(isMuted ? "Unmute" : "Mute")
.accessibilityHint("Toggles the audio playback volume.")
```

### Contrast & Motion
- Support the "Increase Contrast" system setting.
- Respect the "Reduce Motion" system setting by substituting complex animations with simple cross-fades.

## SwiftUI Implementation Best Practices

1. **State Management**: Use `@State` for local view state, `@Binding` for two-way communication, and `@Observable` / `@Environment` for global data.
2. **View Decomposition**: Break complex views into smaller, reusable components to improve performance and readability.
3. **Modifiers Order**: Remember that modifier order matters in SwiftUI. Padding before background differs from background before padding.

## Standard Component Usage

| Component | Use Case | Avoid |
| :--- | :--- | :--- |
| **Alerts** | Critical actions, destructive confirmations. | Using for non-critical information. |
| **Action Sheets** | Multiple mutually exclusive choices. | Using when there are more than 5 choices. |
| **Context Menus** | Quick actions on an item (long press). | Essential actions that have no other access path. |
| **Toasts/HUDs** | Non-intrusive success/status feedback. | Blocking the UI for long periods. |

## App Store Review Readiness Checklist
- [ ] Safe areas are respected on all device models (iPhone SE to Pro Max, iPad).
- [ ] Dynamic Type is fully supported; text does not clip or truncate awkwardly at largest sizes.
- [ ] Dark Mode is fully supported with appropriate contrast ratios.
- [ ] VoiceOver navigates logical sequences and all buttons have descriptive labels.
- [ ] Touch targets are at least 44x44 points.
- [ ] No private APIs are used.
- [ ] Proper permissions (Camera, Photo Library, Location) include descriptive usage strings in `Info.plist`.
- [ ] Launch screen transitions smoothly into the initial view.

## Conclusion
By adhering to these guidelines, developers ensure their applications provide a familiar, intuitive, and accessible experience that users expect from the Apple ecosystem.
