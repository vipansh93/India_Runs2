---
name: Cinematic Noir
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
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
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
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
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
    fontSize: 72px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Instrument Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Instrument Serif
    fontSize: 36px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Instrument Serif
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1440px
  gutter: 2rem
  margin-mobile: 1rem
  section-gap: 8rem
  stack-sm: 0.5rem
  stack-md: 1.5rem
---

## Brand & Style

The design system is engineered for a premium, cinematic experience that prioritizes high-fidelity content over interface chrome. It targets an audience that values immersion, storytelling, and high-end aesthetics, common in streaming, luxury lifestyle, or premium portfolio platforms.

The style is a fusion of **Minimalism** and **Glassmorphism**. By utilizing a deep navy foundation paired with high-contrast white accents, the UI recedes to the background, allowing video and imagery to take center stage. The "Noir" aesthetic is achieved through extreme tonal ranges, subtle translucent overlays, and razor-sharp typography.

## Colors

The palette is strictly functional, designed to maintain visual focus on media. The **Background** (HSL 201 100% 13%) provides a cooler, more "cinematic" alternative to pure black, creating depth in shadows. 

The **Primary** color is pure white, reserved for high-priority calls to action and essential navigation. **Secondary** and **Muted** surfaces utilize deep grays to create subtle separation without breaking the dark-room atmosphere. Interactive elements in their resting state should lean into the **Border** and **Input** tones to ensure the interface feels integrated rather than overlaid.

## Typography

This design system utilizes a high-contrast typographic pairing. **Instrument Serif** is used for display and headline levels; its elegant, editorial strokes evoke luxury and traditional film title sequences.

**Inter** handles all functional and body text. It is chosen for its exceptional legibility at small sizes and its neutral, modern character which balances the expressive nature of the serif. For labels and metadata, Inter is often used in medium weights with increased letter spacing and uppercase styling to mimic technical film slates or HUD elements.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for desktop to maintain a cinematic 16:9 or 21:9 visual balance, switching to a fluid model for mobile devices. 

- **Desktop:** 12-column grid with a maximum width of 1440px. 
- **Gaps:** Generous vertical spacing (section-gap) is encouraged to give content "room to breathe," mimicking the pacing of a film.
- **Safe Areas:** Maintain a minimum 2rem margin on all edges to ensure interface elements do not crowd the viewport edges.
- **Mobile:** Elements reflow to a single column with a 16px gutter. Headlines scale down to prevent excessive line-breaking.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and background manipulation rather than traditional shadows. 

1.  **Base Layer:** The deep navy background or full-screen video.
2.  **Glass Layer:** Navigation bars, cards, and modals use a semi-transparent background (e.g., `rgba(0,0,0,0.4)`) with a significant `backdrop-filter: blur(20px)`.
3.  **Luminous Borders:** Instead of shadows, use a 1px solid border at 18% opacity to define the edges of floating elements.
4.  **Vignetting:** Apply a subtle inner radial gradient to the viewport to draw the eye toward the center of the screen.

## Shapes

The shape language is sharp and precise. A **Soft (0.25rem)** border radius is the standard for most interactive elements like buttons and inputs, providing just enough refinement to feel modern without losing the "editorial" edge. Larger containers like cards or video players may use `rounded-lg` (0.5rem) to slightly soften the overall composition.

## Components

### Buttons
- **Primary:** Solid white background with near-black text. No border. Sharp 0.25rem corners.
- **Secondary:** Glass effect (blur + dark tint) with a 1px border. White text.
- **Ghost:** No background or border. High-contrast white text that underlines on hover.

### Inputs & Forms
- **Fields:** Subtle dark background with the 1px `border-input`. Text is `muted-foreground` until focused. On focus, the border becomes pure white.
- **Checkboxes:** Square with a 1px border. When checked, the fill is white with a black checkmark.

### Cards & Glass Elements
- Use a `backdrop-blur-xl` combined with a subtle top-down linear gradient (transparent to `rgba(255,255,255,0.05)`). This creates a "sheen" effect similar to a lens or high-end display.

### Media Overlays
- Text appearing over video should use a subtle `text-shadow` or a dark gradient scrim at the bottom of the media container to ensure legibility of the white `Instrument Serif` headlines.