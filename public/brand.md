# SEER — Brand Spec for PowerPoint (Seer Protocol)

This is the SEER design system ("Seer Protocol") translated out of web-CSS into PowerPoint terms:
RGB values, point sizes, Office-safe font fallbacks, slide dimensions, and component recipes.

**How to use with Claude:** paste this whole file into a chat and say something like
*"Build me a [N]-slide PowerPoint using this SEER brand spec — topic: …"*. Everything Claude
needs (colours, fonts, layouts, component recipes, do/don't rules) is below. It maps 1:1 to the
live design system at **seer.coach/designsystem-final**.

---

## 0. The one-paragraph summary

Dark, flat, esports-software. Studio-black slides, off-white text, **Seer green** as the single
hero accent, with a small supporting cast (gold, red, blue, purple) used **only** for meaning.
Big condensed UPPERCASE headlines (Oswald), clean body (Inter), monospace for labels/stats
(JetBrains Mono). No gradients, no glow-less flat-grey corporate look, no drop shadows except
soft coloured glows. Generous dark space. Think "post-match victory screen", not "SaaS pitch deck".

---

## 1. Slide setup

- **Aspect ratio:** 16:9 → **13.333 in × 7.5 in** (33.87 cm × 19.05 cm)
- **Slide background:** solid **Studio Black — RGB 18, 20, 22** (hex `#121416`). Never white.
- **Default margins / safe area:** 0.6 in (1.5 cm) all sides; content rarely touches edges.
- **Vibe:** lots of negative dark space; one focal element per slide; left-aligned by default.

---

## 2. Colour palette (PowerPoint RGB)

Set these as your Theme Colors. **Seer Green is the only "loud" colour** — everything else is
semantic (used to mean something), never decorative.

| Role | Name | HEX | RGB | Use for |
|---|---|---|---|---|
| Background | Studio Black | `#121416` | **18, 20, 22** | Slide background |
| Surface | Slate | `#1B1E21` | **27, 30, 33** | Cards, boxes, panels |
| Recessed | Field | `#0D0F11` | **13, 15, 17** | Inset fields, table cells, input wells |
| Text | Zinc (ink) | `#F4F4F5` | **244, 244, 245** | Headlines & body text |
| Muted text | Muted | `#8C8C95` | **140, 140, 149** | Sub-text, captions, footnotes |
| Hairline | Line | `#3A3B3D`* | **58, 59, 61** | 1 pt card/table borders |
| **Primary accent** | **Seer Green** | `#28D397` | **40, 211, 151** | The hero accent: key words, primary buttons, highlights, positive |
| On-primary | Deep Green | `#04261A` | **4, 38, 26** | Text **on top of** a green fill (e.g. button label) |
| Secondary | Hextech Gold | `#C8AA6E` | **200, 170, 110** | "Recommendation" / advice / secondary highlight |
| Alert | Team Red | `#FF4454` | **255, 68, 84** | Warnings, danger, losses, the "X" |
| Alert (text) | Soft Red | `#FF6B78` | **255, 107, 120** | Red text at small sizes (more legible than Team Red) |
| Info | Team Blue | `#3B82F6` | **59, 130, 246** | "Your team" / blue side / neutral data |
| Special | Analysis Purple | `#D8B4FE` | **216, 180, 254** | "Analysis" / insight callouts |

\* The web uses a 12%-opacity white hairline; on Studio Black that resolves to ~RGB 58,59,61 — use that flat value in PowerPoint since PPT borders don't blend nicely.

**Accent discipline (important):** on any given slide, green does the talking. Gold/red/blue/purple
appear only when the content *means* recommendation / warning / team / analysis. A slide with five
accent colours is wrong; a slide with green + one semantic colour is right.

---

## 3. Typography

Four fonts, each with a job. All are free Google Fonts — **install them on the machine that
opens the deck**, or use the Office-safe fallback so it never renders in Times New Roman.

| Job | Font | Weight | Office fallback (Win / Mac) | Used for |
|---|---|---|---|---|
| **Display** | **Oswald** | SemiBold 600 | Bebas Neue → **Arial Narrow Bold** / Oswald | All headlines & big stat numbers |
| **Body** | **Inter** | Regular 400 / Medium 500 / SemiBold 600 | **Segoe UI** / Helvetica Neue | Paragraphs, bullets, button labels, card titles |
| **Data/labels** | **JetBrains Mono** | Regular 400 / Medium 500 | **Consolas** / Menlo | Eyebrows, chips, stat captions, tickers, numbers-as-data |
| **Wordmark** | **Orbitron** | Bold 700 | **Bahnschrift** / Arial Bold | The "S E E R" wordmark only |

### Display rules (Oswald)
- **ALL CAPS**, weight 600, letter-spacing **+0.03 em** (in PPT: Character Spacing → Expanded ~1–1.5 pt).
- Line spacing tight: ~1.05–1.1×.
- Accent treatment: colour **one phrase** Seer Green within an otherwise Zinc headline.
  e.g. **IT SEES THE GAME `BEFORE YOU DO.`** (the green part is the payoff).

### Labels / eyebrows (JetBrains Mono)
- ALL CAPS, **letter-spacing very wide** (PPT Expanded ~2–3 pt), small (9–11 pt).
- Colour: **Seer Green** for active labels, **Muted** for passive captions.
- Optional: prefix with a short green dash "— SECTION NAME" or wrap "[ LABEL ]".

### Type scale (points, for a 13.33×7.5 deck)

| Element | Font | Size (pt) | Case | Colour |
|---|---|---|---|---|
| Hero / cover title | Oswald 600 | 44–54 | UPPER | Zinc + green accent |
| Slide title (H2) | Oswald 600 | 30–34 | UPPER | Zinc + green accent |
| Card / stat number | Oswald 600 | 24–30 | UPPER | Green (good) / Red (bad) |
| Sub-head | Oswald 600 | 18–20 | UPPER | Zinc |
| Lead paragraph | Inter 400 | 15–16 | Sentence | Muted |
| Body / bullets | Inter 400 | 12–14 | Sentence | Muted (key words Zinc) |
| Card title | Inter 600 | 14–15 | Sentence | Zinc |
| Eyebrow / label | JetBrains Mono 500 | 10–11 | UPPER, wide | Green |
| Caption / footnote | JetBrains Mono 400 | 8–9 | UPPER, wide | Muted |

---

## 4. Component recipes (build these with PowerPoint shapes)

All cards are **flat** — solid Slate fill, 1 pt hairline border, soft rounded corners. **No drop
shadows, no gradients.** The only "depth" is a faint coloured glow (see Glow recipe).

### Card / panel
- Shape: Rounded Rectangle, corner radius ~0.12 in (8–12 px feel).
- Fill: **Slate (27,30,33)**. Border: **1 pt, Line (58,59,61)**.
- Padding: ~0.25 in inside. Title in Inter 600 Zinc, body in Inter 400 Muted.

### Highlighted card (the signature look)
- Same card, plus a **left-edge glow pill**: a thin rounded rectangle (~4 px wide × 60% card
  height), filled Seer Green, with a soft green glow, sitting on the card's left edge.
- Use Red instead of Green when the card represents a problem/miss.

### Stat block
- Slate card. Big number in **Oswald 600, 24–30 pt** — **Green** if it's good, **Red** if it's bad.
- Under it, a JetBrains Mono caption in Muted (e.g. `KDA · JETT`).
- Optional: a row of small **segmented dash meters** under the number (3–5 short rounded
  rectangles; lit ones = Green with glow, unlit = dark grey ~RGB 35,37,40).

### Chip / tag (the "typed message" labels)
- Small pill, JetBrains Mono ~9–10 pt UPPER, tinted background = accent at ~14% opacity,
  text = the accent at full strength. The three canonical chips:
  - `RECOMMENDATION` → Gold text on faint gold fill
  - `ANALYSIS` → Purple text on faint purple fill
  - `WARNING` → Red text on faint red fill

### Primary button
- Rounded Rectangle, fill **Seer Green (40,211,151)**, label **Inter 500, Deep Green (4,38,26)**
  text, sentence case. Add a soft green glow. (No 3-D, no bevel, no gradient.)

### Ghost button
- Transparent/near-black fill, **1 pt Line border**, Zinc label. (Hover-equivalent in a deck:
  just the green-bordered variant for emphasis.)

### Glow recipe (use sparingly)
- PowerPoint → Shape Effects → **Glow** → custom colour = the accent, Size ~8–12 pt,
  Transparency ~55–60%. Apply to: primary buttons, the logo mark, key stat numbers, edge pills.
  Never glow body text.

### Divider / hairline
- 1 pt line, Line colour (58,59,61). Or a 2 px Seer-Green segment as a section marker.

---

## 5. Logo

- **Mark:** the eye-and-star — two bone-white claws around a glowing green 4-point star.
  Vector file: `public/logos/seer-mark.svg` (PowerPoint imports SVG: Insert → Pictures → this file).
  - On dark slides: claws = **Zinc (244,244,245)**, star = **Seer Green (40,211,151)** with a green glow.
  - Monochrome contexts: whole mark in Zinc, or whole mark in Seer Green.
- **Wordmark:** "S E E R" in **Orbitron Bold**, heavily letter-spaced (PPT Expanded ~6–8 pt).
  Lock-up = mark + wordmark with a gap roughly equal to the mark's width.
- **Favicon-style tile:** mark centered on a Studio-Black rounded square (`public/logos/seer-mark-icon.svg`).
- **Don't:** recolour the star anything but green; add the old purple/pink/orange gradient; stretch; outline.

---

## 6. Slide archetypes (ready-to-use layouts)

1. **Cover** — Studio Black. Logo mark (with glow) centered or top-left; big Oswald UPPER title
   with one green phrase; JetBrains-Mono green eyebrow above it; thin green dash divider.
2. **Section divider** — huge Oswald UPPER word, mostly green, on near-empty black; small mono
   label top-left like `— 02 / THE PROBLEM`.
3. **Stat trio** — three Slate stat cards in a row, each a big Oswald number (green/red) + mono caption.
4. **Bulleted content** — left: Oswald UPPER title + green eyebrow; right: Inter bullets in Muted
   with key terms in Zinc; optional chips for emphasis.
5. **Comparison / "your team vs enemy"** — two columns, left tinted Team Blue, right Team Red,
   rows as small Field-filled tiles.
6. **Quote / callout** — single Slate card, left-edge green glow pill, Inter italic, green attribution.
7. **Closing / CTA** — centered Oswald UPPER line, green primary button shape, mono reassurance caption.

---

## 7. Quick do / don't

**Do:** dark slides; one green hero accent; UPPERCASE Oswald headlines; flat cards with hairlines;
mono labels; lots of black space; semantic colour only.

**Don't:** white/light backgrounds; rainbow accent slides; gradients; drop shadows / bevels / 3-D;
Times New Roman or Calibri headlines; centre everything; cram the slide.

---

*Source of truth: this maps to `seer.coach/designsystem-final` (the "Seer Protocol" direction).
Other palette directions A–G exist at `seer.coach/designsystem-{a..g}` but Protocol is the brand.*
