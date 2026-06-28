---
name: Obsidian & Ether
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c8'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c6c6c7'
  primary: '#ffffff'
  on-primary: '#2f3131'
  primary-container: '#e2e2e2'
  on-primary-container: '#636565'
  inverse-primary: '#5d5f5f'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#ffffff'
  on-tertiary: '#2f3131'
  tertiary-container: '#e2e2e2'
  on-tertiary-container: '#636565'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c7'
  on-primary-fixed: '#1a1c1c'
  on-primary-fixed-variant: '#454747'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  display-lg:
    fontFamily: Instrument Serif
    fontSize: 88px
    fontWeight: '400'
    lineHeight: '1.0'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Instrument Serif
    fontSize: 56px
    fontWeight: '400'
    lineHeight: '1.1'
  headline-md:
    fontFamily: Instrument Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1440px
  gutter: 32px
  margin-desktop: 80px
  margin-mobile: 24px
  section-gap: 160px
---

## Brand & Style

This design system is built for "Asme," a platform dedicated to pioneering ideas and creative vision. The aesthetic is rooted in **Premium Minimalism** with a **Cinematic** edge, focusing on the tension between pure darkness and sharp light. 

The brand personality is authoritative, visionary, and sophisticated. It utilizes a "Liquid Glass" style—a refined evolution of glassmorphism that prioritizes subtle luminosity and deep atmospheric blurs over heavy frosted effects. The goal is to evoke a sense of boundless space and high-end editorial curation.

- **Minimalism:** Extreme restraint in color and decoration.
- **Glassmorphism:** Applied as "Liquid Glass" (deep blurs, translucent layers).
- **Cinematic:** High-impact visuals, generous negative space, and deliberate motion.

## Colors

The palette is strictly monochromatic to ensure the content—pioneering ideas and creative vision—remains the sole focus.

- **Background:** `#000000` (Pure Black). Provides the "infinite" void required for cinematic depth.
- **Foreground/Text:** `#FFFFFF` (Pure White). Maximum contrast for legibility and impact.
- **Surface (Liquid Glass):** `rgba(255, 255, 255, 0.01)`. A near-invisible base that relies on `backdrop-filter: blur(20px)` and `saturate(180%)` to create presence.
- **Accents:** Use varying opacities of White (e.g., 40% for secondary text, 10% for dividers) to maintain the monochrome hierarchy.

## Typography

The typographic system relies on the contrast between the expressive, literary quality of **Instrument Serif** and the systematic, functional clarity of **Inter**.

- **Expressive Heads:** Use Instrument Serif for all primary messaging. Utilize the *italic* variant for emphasis or to break the rhythm in long titles.
- **Functional Text:** Inter is used for body copy and UI elements. 
- **Hierarchy:** Maintain large scale differences between headers and body text to reinforce the premium, editorial feel. 
- **Rendering:** Ensure `antialiased` font smoothing is active to maintain the sharp profile of white text on black.

## Layout & Spacing

The layout philosophy is defined by **Generous Whitespace** and a **Structured Fluid Grid**.

- **Grid:** A 12-column grid with wide gutters (32px) to allow components room to breathe.
- **Alignment:** Hero sections are center-aligned for maximum cinematic impact. Secondary sections utilize asymmetrical layouts (e.g., text spanning columns 2-7) to create visual interest.
- **Sectioning:** Large vertical gaps (160px+) between sections to prevent the UI from feeling cluttered.
- **Responsive:** On mobile, margins reduce to 24px and the grid collapses to a single column, with display type scaling down significantly to ensure fit.

## Elevation & Depth

Depth is not achieved through traditional shadows, but through **Optical Layering** and **Liquid Glass** effects.

- **Base Layer:** Pure Black (`#000000`).
- **Surface Layer:** `backdrop-filter: blur(20px)` combined with a `1px` border using a `Luminosity` or `Overlay` blend mode at 15% opacity.
- **Inset Depth:** For interactive elements, use a subtle `inset` white shadow (`rgba(255, 255, 255, 0.05)`) to create a slight "carved" or "pressed" look within the glass.
- **Z-Axis:** Higher elevation elements should increase their backdrop-blur intensity rather than adding drop shadows.

## Shapes

The design system uses a **Soft** shape language to contrast with the high-contrast color palette.

- **Standard Radius:** 0.25rem (4px) for small UI elements like tags or inputs.
- **Container Radius:** 0.75rem (12px) for larger "Liquid Glass" cards and sections.
- **Media:** Video and image backgrounds should remain sharp (0px) when full-bleed, but follow the `0.75rem` radius when contained in cards.

## Components

### Buttons
Primary buttons are solid White with Black text (`Inter SemiBold`). Secondary buttons are "Liquid Glass" with a 1px white border and white text. Hover states should involve a subtle scale-up (1.02x) and an increase in border opacity.

### Liquid Glass Cards
The signature component. Features a `rgba(255, 255, 255, 0.02)` background, `20px` backdrop blur, and a top-weighted gradient border to simulate a light source from above.

### Input Fields
Minimalist underlines or very subtle glass containers. Focus state expands the underline or increases the glass border opacity to 40%. Labels should use the `label-caps` typography style.

### Navigation
A fixed "Liquid Glass" header. On scroll, the backdrop blur increases. Links use `label-caps` with a simple opacity transition on hover (60% to 100%).

### Cinematic Backgrounds
Video elements should be muted, high-contrast, and slow-moving. Use a black overlay gradient at the bottom to ensure seamless transitions into the next content section.