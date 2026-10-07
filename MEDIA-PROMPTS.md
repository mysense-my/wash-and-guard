# WASH & GUARD — MEDIA GENERATION PROMPT PACK

Replacement media for every slot on the Wash & Guard landing page.
**19 images + 1 hero video.** This is a single landing page, so only the slots the homepage actually renders are here. Engine: Seedream 5 Pro (Magnific) for images; Kling 2.5 / Veo 3 / Seedance for the video.

Generate at the "target px" size given per slot — larger than the template's own files so crops stay sharp.

---

## GLOBAL STYLE BLOCK — append to EVERY image prompt

```
Shot on a full-frame camera, 35mm or 85mm prime lens, wide aperture, shallow depth of field. Cinematic automotive photography. Very dark near-black background, deep shadows, one strong warm key light plus long vertical white LED strip reflections stretching down the bodywork. Colour grade is charcoal black and gunmetal grey with warm gold-amber highlights — absolutely no blue or cyan cast. Fine natural film grain, realistic surface imperfections, dust in the light beams. Photorealistic editorial photography, not illustration, not a 3D render.
```

## GLOBAL NEGATIVE PROMPT — use on EVERY image

```
text, letters, words, numbers, watermark, logo, brand badge, emblem, number plate characters, signage, poster, blue colour cast, cyan lighting, neon purple, teal and orange grade, oversaturated, cartoon, illustration, 3d render, cgi, plastic waxy skin, extra fingers, deformed hands, six fingers, distorted reflections, warped body panels, tilted horizon, snow, autumn leaves, American suburban street, European cobblestone
```

## Three rules baked into these prompts

1. **No nouns that become text.** Generators render the word "sign", "label" or "brand" as on-image lettering. None of these prompts use them.
2. **Every person gets ethnicity + age + build + an explicit facial expression.** Without stating the expression you get blank mannequin faces.
3. **Every number plate is described as blank.** Otherwise you get gibberish characters that read as fake.

## The Malaysian brief, concretely

- **Cars:** locally-assembled compact hatchbacks, compact crossovers, and mid-size sedans — the everyday Malaysian road mix. Not Lamborghinis.
- **Bikes:** 135–150cc underbone sport bikes and small-capacity sport bikes, plus one large-capacity naked bike for the premium slots.
- **People:** Malay, Chinese-Malaysian and Indian-Malaysian technicians, 20s–40s, in plain black work polos.
- **The bay:** this is Wash & Guard's actual interior — dark grey tiled floor with **gold safety striping painted on it**, black walls, white LED light lines running along the ceiling and walls. Use it as the set for all interior shots.
- **Outside the shutter:** tropical daylight, wet monsoon tarmac, rain trees, low shophouse rooflines — only ever glimpsed, never the subject.

---

# 1 · HERO BACKGROUND VIDEO

The template's hero is a multi-shot edit — roughly six close-ups, hard cuts, hands and forearms only, never a face. This is **one prompt** that produces the whole sequence in a single generation. Four shots instead of six so each one gets enough time inside 8 seconds.

## V1 — `hero-loop.mp4` · 1920×1080 · 8 s · silent · loops

```
An 8-second cinematic sequence of four hard-cut shots, 2 seconds each, no transitions or fades between them. SHOT 1: a pressure washer lance sweeps a thick curtain of white snow foam across the black bonnet of a car, backlit so the foam glows against a black wall. CUT TO SHOT 2: a gloved hand slowly draws a folded microfibre towel across wet black gloss, lifting a clean dry band of mirror finish behind it while water beads catch warm gold light. CUT TO SHOT 3: a gloved hand wipes a cloth across the glossy black and gold fuel tank of a motorcycle, following the curve, a long white light strip reflected in the surface. CUT TO SHOT 4: water sheets off a freshly coated dark grey panel into tight round beads that race away, each catching a pinpoint of gold light. Every shot is an extreme close-up with very shallow depth of field, hands and forearms only, never a face, never a wide view of a whole vehicle. Set in a dark near-black detailing bay lit by one warm gold key light and long white LED strips. Warm gold and black colour grade, absolutely no blue or cyan. Slow constant camera drift within each shot, no shake. Fine film grain, photorealistic footage, no text, no logos.
```

**Negative prompt**

```
text, captions, subtitles, logo, watermark, faces, people talking, full body, wide shot, fades, dissolves, crossfade, shaky camera, zoom burst, blue lighting, cool colour grade, timelapse, cartoon, cgi, 3d render
```

**Notes**

- Works on models that honour shot lists in one generation — Veo 3 and Kling 2.5 both do. If yours flattens it into one continuous shot, move the words `CUT TO` to the front of each shot and put each on its own line.
- Shot 3 is the motorbike. It is the shot that tells a visitor this studio does bikes as well as cars, so don't drop it if you trim.
- The hero headline sits over the middle of frame, so nothing important should live dead centre.
- Trim to a clean loop point if the last frames drift.

---

# 2 · PROCESS — 3 images · 16:9 · target **2048×1152**

The "one standard" row on the homepage. **Re-shot October 2026**: the first set showed a visible face in
every card, which is where these models give themselves away, and the cars were badge-less generic shapes
that read as CGI rather than real vehicles.

Two rules now apply to this row:

1. **No faces.** Hands, forearms and backs only. Detailing photography is about surfaces and tools anyway,
   and every AI tell in the first set lived in a face.
2. **A different car in each card, supplied as a reference photo.** An everyday hatchback in the first, a
   mid-tier sedan or compact SUV in the second, something nicer in the third. The client takes every kind
   of vehicle, and three different cars say so without a line of copy.

Suggested references: **Perodua Myvi or Proton Saga** (card 1), **Honda Civic or Proton X50** (card 2),
anything more expensive, or the motorbike (card 3). Shoot or source the reference three-quarter front,
whole car in frame, flat daylight, sharp, dark or mid-grey paint. Badges tend to come out garbled, so
frame them small or crop them.

Run each of these with your own car photograph attached as the reference image. The reference supplies the vehicle only — it will not carry the room, so the bay is described in full in every prompt. Keep the global style block and negative prompt on.

## P1 — `process-01-prep.webp` — Inspection

```
Using the supplied photograph only as the reference for the car's exact shape, proportions and model, place that same car inside a dark premium detailing bay. Medium shot from a low front three-quarter angle. A technician in a plain black work polo crouches at the front wing with his back and shoulder to the camera, holding a slim handheld inspection light at a shallow angle across the paint so the beam rakes over the panel and throws fine swirl marks into relief. His head is turned away and cropped out of frame — no face visible anywhere. Dark grey tiled floor with gold safety striping, black walls, long white LED strip lights overhead reflecting down the bodywork. Blank number plate with no characters.
```

## P2 — `process-02-treat.webp` — Treatment

```
Tight close-up, no vehicle in full view. Two hands in black nitrile gloves press a dual-action polishing machine with a white foam pad against the rear quarter panel of a glossy dark car, forearms entering from the right edge of frame. The arms are cropped at the elbow — no face, no head, no torso in frame. A thin film of polish spreads under the pad, and the panel behind the pad reads as a deep liquid mirror while the panel ahead of it is still hazy. Dark detailing bay, gold floor striping, long white LED strip lights stretching down the paint in unbroken vertical lines.
```

## P3 — `process-03-deliver.webp` — Handover

```
Close-up of a car key being handed from one person to another over the open driver's door sill of a freshly detailed car. Only two pairs of hands and forearms are in frame — one in a plain black work polo sleeve, one in a casual shirt sleeve. No faces, no heads, no bodies. The key is held cleanly between fingers, fully formed, with a simple unbranded fob. Behind the hands the car's flank is mirror-perfect and reflects long white LED strip lights. Dark grey tiled floor with gold safety striping, black walls, warm gold key light. Blank number plate, no badges.
```

**Check before accepting:** no face or head anywhere in frame, five fingers per hand, the car reads as a
real model with proper panel gaps and a real grille, blank plate, and the three cards show three
different vehicles.

---

# 3 · SERVICE CARDS — 6 images · 16:9 · target **2400×1350**

One per service card. These also become the hero image of each service detail page, so keep them clean and readable at large size.

## S1 — `service-wash.webp` — Wash & Undercarriage

```
A silver compact Malaysian hatchback covered in thick white snow foam, mid-wash, inside a dark detailing bay. A technician's arm in a black sleeve and black glove guides a pressure washer lance, sending a fine mist across the roofline. Water runs down the gold safety striping painted on the dark grey tiled floor and the floor reflects the white LED ceiling strips. Blank number plate, no badges. Three-quarter front view, wide framing, backlit so the foam glows against the black wall.
```

## S2 — `service-polish.webp` — Machine Polish

```
Tight three-quarter close-up of a black sedan's front wing being machine polished. A gloved hand holds a dual-action polisher with a white foam pad against the panel; half the wing is corrected to a deep liquid-mirror gloss and half still shows a dull hazy finish, with the difference clearly visible along a hard line. Dark detailing bay behind, gold floor striping, long white LED strip reflections running down the door. Blank number plate, no badges.
```

## S3 — `service-ceramic.webp` — Ceramic Coating

```
Macro close-up of a gloved hand holding a small coating applicator block wrapped in a suede cloth, drawing a wet ceramic coating across the corner of a black bonnet. The coated section flashes with rainbow high-gloss sheen where the light hits it. Beside the panel sits a plain amber glass dropper bottle with no lettering on it. Dark detailing bay, warm gold key light, long white LED reflections stretching across the paint. Extremely shallow depth of field.
```

## S4 — `service-tint.webp` — Window Tint

```
A Malay technician in his late twenties, plain black work polo shirt, black gloves, concentrating intently as he squeegees a dark tint film onto the inside of a car's rear windscreen. His hands press the film flat and a thin bead of water runs to the edge. Shot from outside the glass looking in, so the film's clean dark tone contrasts with the bright white LED strip lights reflecting off the glass. Dark detailing bay, gold floor striping visible through the window. Blank number plate, no badges.
```

## S5 — `service-ppf.webp` — Paint Protection Film

```
Close-up of two gloved hands laying a large clear protective film sheet over the bonnet of a dark grey compact crossover, the film lifting slightly in a soft curve and catching the light along its edge. A squeegee rests against the panel. The bonnet beneath is flawless and reflects long white LED strip lights. Dark detailing bay, gold safety striping on the floor, black walls. Blank number plate, no badges. Shot from a low front three-quarter angle.
```

## S6 — `service-motorbike.webp` — Motorbike Detailing

```
A 150cc Malaysian sport underbone motorcycle with glossy black and gold fairings, on a paddock stand inside a dark detailing bay, being hand-polished by a young Chinese-Malaysian technician in a plain black work polo shirt, kneeling beside it with a focused expression and a microfibre cloth in his gloved hand. The fairing is mirror-glossy and reflects long white LED strip lights. Dark grey tiled floor with gold safety striping, black walls. Blank number plate, no badges, no decals with lettering. Low three-quarter front view.
```

---

# 4 · BEFORE / AFTER SLIDER — 1 generation + 1 edit · 16:9 · 2048×1152

**Do not generate these as two prompts.** Two independent generations give two different cars, which
is what went wrong the first time — no wording fixes it, because the model has no memory of the first
image. Generate the *after* once, then **edit that exact file** to make the *before*. The edit keeps
the car, the angle, the lens and the lighting because it starts from those pixels.

## Step 1 — generate `ba-after.webp`

This is the base image. Get this one right before going anywhere near step 2.

```
A dark grey mid-size sedan parked at a three-quarter front angle inside a dark detailing bay. The whole car is in frame, centred, with even space on the left and right and clear headroom above the roof. Camera at headlight height, level, 50mm lens, no perspective distortion, no tilt. The car is freshly detailed: liquid-mirror gloss paint, long white LED strip lights reflecting in sharp unbroken vertical lines down the flank, clean glossy black tyres, spotless glass, a warm gold highlight running along the shoulder line. Dark grey tiled floor with gold safety striping, black walls, long white LED strips overhead. Blank number plate with no characters, no badges.
```

Check before accepting: whole car in frame, level camera, even space either side, nothing cropped,
blank plate. If the framing is off, regenerate now — every fault here is inherited by step 2.

## Step 2 — edit that image into `ba-before.webp`

Feed the approved after image back in as the **source image**, not as a style reference.

- Magnific: **Reimagine**, creativity **low**, resemblance/structure **high**
- Any Flux Kontext or Nano-Banana style editor: an edit, not a fresh generation
- Strength / denoise: **0.25–0.35**. Higher and it redraws the car

```
Same photograph, same car, same angle, same lighting, same framing. Change only the condition of the surfaces: the paint is covered in a dull film of dried road grime and dust, there is rain spotting and water marks across the glass, brake dust on the wheels, and the finish is flat and matte with no reflections in it. Do not move the camera. Do not change the car, the bay, the lights, the floor or the composition in any way.
```

**Accept only if:** the car is in exactly the same position, the wheels have not rotated, the
background lights have not moved, and the image is the same size. Hold the two side by side and flick
between them — anything that jumps is a fail. Re-run with lower strength.

## If your tool cannot do image-to-image

Fall back to seed-locking: run the step 1 prompt, note the seed, then run it again with the **same
seed** and the condition words swapped to the step 2 wording. This gets close but rarely exact —
check it the same way, and expect a few attempts.

## Why it matters

The slider wipes between these two along a moving vertical line. A mismatch in car, angle or light
position reads as two unrelated photographs the instant the handle moves, which is worse than having
no slider at all.

---

# 5 · REVIEW CARDS — 4 images · 3:2 · target **2400×1600**

Each sits above a customer quote. Mix the vehicle types so the page reads as a real local customer base.

## R1 — `review-01.webp` — coating customer, car exterior

```
A glossy black compact crossover parked outside at dusk on wet tarmac, photographed from a low rear three-quarter angle. Water beads sit tight and round across the paintwork. Warm street light and a tropical evening sky behind, blurred rain trees and a low shophouse roofline far in the background. The bodywork is mirror-perfect with sharp reflections. Blank number plate, no badges. Moody, cinematic, warm gold highlights against a near-black car.
```

## R2 — `review-02.webp` — interior customer

```
Interior of a freshly detailed compact Malaysian car, shot from the rear seat looking forward across the centre console to the windscreen. Black fabric and grey plastic surfaces are spotless with a clean matte finish and no artificial shine, the dashboard is dust-free, the glass is streak-free. Soft daylight comes through the windscreen; tropical greenery is visible outside, heavily blurred. No lettering on any dial or screen. Clean, calm, premium.
```

## R3 — `review-03.webp` — big bike customer

```
A large-capacity naked motorcycle with a glossy black tank, parked on a paddock stand inside a dark detailing bay. Shot from a low front three-quarter angle. The tank and fairings are mirror-glossy and reflect long white LED strip lights in clean vertical lines; the engine cases and forks are spotless. Dark grey tiled floor with gold safety striping, black walls. Blank number plate, no badges, no decals with lettering.
```

## R4 — `review-04.webp` — family car customer

```
A silver seven-seater MPV parked inside a dark detailing bay, photographed from a front three-quarter angle. Freshly washed and polished, the paint is clean and bright with long white LED strip reflections along the flank, the wheels are spotless, the glass is clear. Dark grey tiled floor with gold safety striping, black walls. Blank number plate, no badges. Well-lit, clean and honest rather than dramatic.
```

---

# 6 · TEAM PORTRAITS — 3 images · 16:9 · target **2400×1355**

All three must match exactly: same backdrop, same light, same crop, same wardrobe. Generate T1, then reference it for T2 and T3.

## T1 — `team-01.webp` — Founder & lead detailer

```
Studio portrait of a Malay man in his late thirties, medium build, short black hair, neatly trimmed beard, warm confident closed-mouth smile, looking straight into the camera with his arms folded. He wears a plain black work polo shirt with no lettering or emblem on it. Lit by a single warm gold key light from the left with strong falloff, against a completely plain dark charcoal backdrop. Centred, waist-up, wide framing with dark empty space either side. Sharp, editorial, premium.
```

## T2 — `team-02.webp` — Coating & film specialist

```
Studio portrait of a Chinese-Malaysian man in his late twenties, slim build, short black hair, clean shaven, calm neutral expression with a slight smile, looking straight into the camera with his arms folded. He wears a plain black work polo shirt with no lettering or emblem on it. Identical lighting to a matching portrait: a single warm gold key light from the left with strong falloff, plain dark charcoal backdrop. Centred, waist-up, wide framing with dark empty space either side.
```

## T3 — `team-03.webp` — Motorbike specialist

```
Studio portrait of an Indian-Malaysian man in his early thirties, athletic build, short black hair, light stubble, relaxed friendly expression, looking straight into the camera with his arms folded. He wears a plain black work polo shirt with no lettering or emblem on it. Identical lighting to a matching portrait: a single warm gold key light from the left with strong falloff, plain dark charcoal backdrop. Centred, waist-up, wide framing with dark empty space either side.
```

---

# 7 · SECTION BACKGROUND — 1 image · 16:9 · target **2400×1350**

Sits behind both the FAQ and the closing call to action. Headlines sit on top, so it must be **empty, dark and low-contrast**.

## BG1 — `bg-faq-cta.webp` — behind the FAQ / closing call-to-action

```
An empty premium detailing bay photographed straight down its length, symmetrical one-point perspective. Long white LED strip lights run along both side walls and the ceiling, converging toward the far end. The dark grey tiled floor is wet and glossy and mirrors the light strips; a gold safety stripe is painted along each side of the floor. Black walls, no vehicles, no people, no equipment on the walls. Very dark, moody, deep shadows, cinematic, empty and quiet.
```

---

# 9 · NOT AI-GENERATED — handle separately

| Asset | What it is | How it gets made |
|---|---|---|
| `logo.svg` | Wash & Guard wordmark | Trace from the client's supplied logo — needs a flat single-colour horizontal lockup for the header and footer. **Ask the client for the vector file.** |
| `grain.png` ×2 | 267×267 tiling noise texture the template overlays on dark sections | I generate this in code, no AI needed |
| `og-image.jpg` | 5000×2625 social share card | Screenshot of the finished homepage, captured at the end of the build |

---

# 10 · GENERATION CHECKLIST

- [ ] V1 — hero video
- [ ] P1 P2 P3 — process
- [ ] S1–S6 — service cards
- [ ] BA — after image, then the edit that makes the before **(one generation + one edit, never two generations)**
- [ ] R1–R4 — reviews
- [ ] T1 T2 T3 — team **(same backdrop and light across all three)**
- [ ] BG1 — section background **(must stay empty and dark — text sits on it)**

**Before you accept any image, check:** no gibberish text anywhere, no number plate characters, no badge shapes that read as a real manufacturer, hands have five fingers, reflections aren't warped, and the grade is gold-on-black with no blue in it.

Drop the finished files into `assets/` in the project folder using the filenames above, and the build will pick them up directly.


---

# APPENDIX A — cut from the landing page build

The template ships a gallery page, a contact page and six service detail pages. A one-page build renders none of them, so these slots are not in the checklist above. They are kept here in case a section gets added later.

## A1 — contact-page background

## BG2 — `bg-contact-hero.webp` — contact page hero

```
An empty premium detailing bay at a slight angle, the shutter door at the far end half open with warm tropical daylight spilling across the wet dark grey tiled floor. Long white LED strip lights run along the black walls. A gold safety stripe is painted along the floor edge. No vehicles, no people. Very dark foreground, bright glow at the far end, deep atmospheric haze in the light. Cinematic and empty.
```

## A2 — gallery grid, nine images

# 8 · GALLERY — 9 images

Mixed orientation grid. **5 landscape · 7:4 · target 2800×1600** and **4 portrait · 4:7 · target 1600×2800.**

### Landscape · 7:4 · 2800×1600

## G1 — `gallery-01.webp`

```
A glossy black sedan inside a dark detailing bay, shot tight along the flank from a low angle so the long white LED strip lights stretch down the door in unbroken vertical reflections. Water beads cling across the paint. Dark grey tiled floor with gold safety striping. Blank number plate, no badges. Half the frame is deep shadow.
```

## G2 — `gallery-02.webp`

```
Macro close-up of water beading tight and round on a freshly coated dark grey bonnet, each bead catching a pinpoint of warm gold light. The panel curves away into darkness. Extremely shallow depth of field, only a narrow strip in sharp focus. Nothing else in frame.
```

## G3 — `gallery-03.webp`

```
A 150cc Malaysian sport underbone motorcycle with black and gold bodywork on a paddock stand inside a dark detailing bay, shot from a low rear three-quarter angle. The tail fairing and exhaust are spotless and reflect long white LED strip lights. Dark grey tiled floor with gold safety striping, black walls. Blank number plate, no badges, no decals with lettering.
```

## G4 — `gallery-04.webp`

```
The underside of a compact crossover raised on a scissor lift inside a dark detailing bay, photographed from low and behind as a pressure washer sends a fine mist across the clean undercarriage. Water spray glows in the beam of the white LED strip lights. Dark grey tiled floor with gold safety striping. Blank number plate, no badges. Dramatic backlight, heavy atmosphere.
```

## G5 — `gallery-05.webp`

```
A silver compact Malaysian hatchback under thick white snow foam inside a dark detailing bay, shot wide from a front three-quarter angle. Foam slides slowly down the bonnet and doors. The foam is lit bright white against black walls; the wet dark grey tiled floor with gold safety striping mirrors the whole car. Blank number plate, no badges.
```

### Portrait · 4:7 · 1600×2800

## G6 — `gallery-06.webp`

```
Vertical close-up of a gloved hand polishing the corner of a black car's headlight cluster with a small foam pad, the lens crystal clear and throwing a sharp warm gold highlight. Dark detailing bay behind, completely out of focus, with a single white LED strip glowing. Very shallow depth of field, the frame tall and tight.
```

## G7 — `gallery-07.webp`

```
Vertical shot of a Malay technician in his twenties, plain black work polo shirt, black gloves, leaning into the driver's footwell of a car with a focused expression, running a soft detailing brush along the base of the centre console. Clean black interior surfaces, a small work light throwing warm light across the cabin. Dark bay visible through the open door behind him. No lettering on any surface.
```

## G8 — `gallery-08.webp`

```
Vertical close-up of a freshly cleaned alloy wheel and glossy black tyre on a dark grey car, shot from a low front angle inside a dark detailing bay. The wheel face is spotless, the brake caliper visible behind the spokes, water beads on the arch above. Gold safety striping on the wet tiled floor beneath. No badges, no lettering on the tyre wall.
```

## G9 — `gallery-09.webp`

```
Vertical shot looking down the length of a black car's flank inside a dark detailing bay, the body curving away, long white LED strip lights running down the paint in unbroken vertical lines. A gloved hand enters at the bottom of the frame wiping the surface with a folded microfibre cloth. Mostly deep shadow with one bright band of reflection.
```

---
