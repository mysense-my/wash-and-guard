# Axion template — measured teardown

Everything below was measured from the live site, not guessed. Values marked *measured* came from
`tools/motion.py` driving a headless Chrome with rAF throttling disabled.

## Breakpoints

| Range | Name |
|---|---|
| ≤ 809px | mobile |
| 810 – 1199px | tablet |
| ≥ 1200px | desktop |

Page height at 1440 wide: **11135px**. At 390 wide: **14289px**.

## Section map (desktop, 1440)

| Section | top | height |
|---|---|---|
| Hero | 0 | 900 (100vh) |
| Our craft | 900 | 801 |
| Our services | 1701 | **3754** (sticky stack) |
| Why choose us | 5454 | 948 |
| Before / after | 6402 | 1156 |
| Testimonials | 7558 | 633 |
| Team | 8191 | 886 |
| FAQ | 9076 | 786 |
| CTA + footer | 9862 | 1273 |

## Motion inventory

### 1. Scroll reveal — the one effect used everywhere *(measured)*
Every section header, card and grid cell enters with:
- `opacity: 0 → 1`
- `translateY: 60px → 0`
- duration **~1.25s**, curve is a long-tailed ease-out (Framer spring). Closest CSS fit: `cubic-bezier(0.16, 0.7, 0.3, 1)`.

Measured samples (t ms → translateY px): 0→60, 66→56.9, 132→46.8, 199→35.7, 266→26, 332→18.3,
463→8.4, 530→5.7, 663→2.4, 797→1.0, 1263→0.

Fires when the element's top passes roughly 75% of viewport height. Plays once.

### 2. Services — sticky card stack *(measured)*
Not a carousel and not a marquee. Four cards, each `position: sticky; top: 128px`, height 540px,
spaced 940px apart in flow. **No transform, no scale, no opacity change** — each card simply pins
and the next slides over it. Pure CSS; needs no JavaScript at all.

### 3. Testimonials — auto ticker *(measured)*
Continuous leftward translate at **35.2 px/s**. Track 1544px wide, 8px gap between cards.
Loops seamlessly by duplicating the card set.
**Gotcha:** measuring this in a hidden browser pane gives ~2 px/s because rAF is throttled. Measure in headless Chrome.

### 4. Before / after — clip-path wipe *(measured)*
Top layer carries `clip-path: inset(0 <x>% 0 0)`. Auto-plays a ping-pong between **8% and 92%**,
sweeping across in roughly 1.2s with a short dwell at each end. Draggable handle overrides the
auto-play. Prev/next arrow buttons sit above the image.

### 5. Nav *(measured)*
`position: fixed; top: 0`, 86px tall, **transparent at every scroll position** — no background
fade-in, no hide-on-scroll-down, no shrink. The simplest possible behaviour.

### 6. Hero video
Muted, looping, autoplay, `object-fit: cover`, full-bleed behind the headline.

## Layout language

- Container ~1344px, 48px side margins at desktop.
- Section rhythm: eyebrow → two-line headline → supporting paragraph.
- **Eyebrow**: mono, uppercase, letterspaced, prefixed with a `>` chevron.
- **Headline**: two lines, second line in the accent colour. Regular weight, not bold, tight leading.
- Alternating section grounds: dark → light → dark → light.
- Buttons: pill, label left, arrow glyph in a contrasting square on the right.
- Feature grid: hairline dividers forming a table, not detached cards.
- Team and service cards: photo with text overlaid at the bottom over a gradient.
- Footer: giant outlined wordmark watermark across the base.

## What we change for Wash & Guard

| Template | Ours |
|---|---|
| Blue accent `#0099FF` | Gold `#E8B33A` / `#C9962A` |
| Blue-black ground `#01101c` | Warm near-black `#0E0E10` |
| Britti Sans Trial (licensed trial, cannot ship) | Geist |
| Geist Mono | Geist Mono (kept) |
| 4 service cards | 6 — adds PPF and motorbike detailing |
| US copy, US pricing | Wash & Guard's own copy, RM pricing |
