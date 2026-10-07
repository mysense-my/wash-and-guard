"""Derive ba-before from ba-after.

Two separate generations never produce the same car, so the 'before' is made from
the 'after' itself: the car is segmented out, aged, and composited back over the
untouched bay. Same car, same angle, same lights, guaranteed.

usage: python3 tools/make_before.py [strength]   # strength defaults to 1.0
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import gaussian_filter, zoom

SRC, OUT = 'assets/ba-after.webp', 'assets/ba-before.webp'
K = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
rng = np.random.default_rng(7)

base = Image.open(SRC).convert('RGB')
W, H = base.size
a = np.asarray(base).astype(np.float32) / 255.0
lum = a.mean(axis=2)

# ---- 1. car mask -------------------------------------------------------------
from rembg import remove, new_session
cut = remove(base, session=new_session('isnet-general-use'), post_process_mask=True)
mask = gaussian_filter(np.asarray(cut.split()[-1]).astype(np.float32) / 255.0, 2.0)
m = mask[..., None]
print('car covers %.1f%% of frame' % (mask.mean() * 100))

# Which way dirt moves the paint depends on the car: on a dark car dust reads
# lighter than the panel, on a silver or white one it reads darker. Use the 70th
# percentile of the car's own pixels, not the mean — the mask takes in tyres,
# glass and grille, whose darkness drags a mean below the threshold even on a
# silver car.
car_lum = float(np.percentile(lum[mask > 0.6], 70)) if (mask > 0.6).any() else 0.3
light_car = car_lum > 0.45
print('car luminance %.2f -> %s car' % (car_lum, 'light' if light_car else 'dark'))

if light_car:
    DUST = np.array([0.36, 0.315, 0.25], dtype=np.float32)
    STRENGTH, EXPOSURE, LIFT, SOFT, SPOTS = 0.62, 0.84, 0.004, 0.58, 0.34
else:
    DUST = np.array([0.62, 0.575, 0.50], dtype=np.float32)
    STRENGTH, EXPOSURE, LIFT, SOFT, SPOTS = 0.30, 0.965, 0.017, 0.20, 0.13
STRENGTH *= K

# ---- 2. where the dirt sits --------------------------------------------------
def octave(scale):
    small = rng.random((max(2, H // scale), max(2, W // scale)))
    return zoom(small, (H / small.shape[0], W / small.shape[1]), order=3)

def streaks():
    small = rng.random((max(2, H // 7), max(2, W // 90)))
    out = zoom(small, (H / small.shape[0], W / small.shape[1]), order=3)
    return gaussian_filter(out, (7, 0.9))

# Real grime is patchy and runs downward. A smooth field reads as a filter laid
# over the photo, so this mixes fine texture with vertical run-off streaks and
# then pushes the contrast up so it breaks into patches rather than a wash.
dust = (0.28 * octave(110) + 0.26 * octave(40) + 0.28 * octave(11)
        + 0.18 * streaks())
dust = (dust - dust.min()) / (np.ptp(dust) + 1e-6)
dust = np.clip((dust - 0.30) / 0.46, 0, 1)
dust = gaussian_filter(dust, 0.9)

ys = np.linspace(0, 1, H)[:, None]
settled = np.clip((1.15 - ys * 0.7) ** 2.1, 0, 1.4)          # dust on upward faces
spray = np.clip((ys - 0.42) / 0.58, 0, 1) ** 1.3 * 1.55      # road spray low down
weight = np.clip(settled * 0.72 + spray, 0, 1.6)

# Glass, lamp lenses and chrome do not hold dirt the way paint does, and they are
# the brightest things in the frame. Find them as local highlights — pixels well
# above their own neighbourhood — and keep the dust off them. Weighting dust by
# raw luminance instead puts the heaviest grime straight onto the headlamps,
# which is what gives the whole thing away as a filter.
local = gaussian_filter(lum, 14)
spec = np.clip((lum - local - 0.045) / 0.16, 0, 1)
weight = weight * (1.0 - 0.92 * spec)
dust_amt = np.clip(dust * weight, 0, 1)[..., None]

# ---- 3. kill the gloss -------------------------------------------------------
soft = np.asarray(base.filter(ImageFilter.GaussianBlur(3.0))).astype(np.float32) / 255.0
work = a * (1 - SOFT) + soft * SOFT
work = np.where(work > 0.62, 0.62 + (work - 0.62) * (0.22 if light_car else 0.58), work)
work = work * EXPOSURE + LIFT
grey = work.mean(axis=2, keepdims=True)
work = grey + (work - grey) * (0.70 if light_car else 0.80)

# ---- 4. lay the dirt on ------------------------------------------------------
work = work * (1 - dust_amt * STRENGTH) + DUST * (dust_amt * STRENGTH)
work += (rng.random((H, W, 1)).astype(np.float32) - 0.5) * 0.034 * dust_amt

# ---- 5. dried water spots ----------------------------------------------------
spots = np.zeros((H, W), dtype=np.float32)
yy, xx = np.mgrid[0:H, 0:W]
for _ in range(260):
    cx, cy = rng.integers(0, W), rng.integers(int(H * 0.20), int(H * 0.70))
    r = rng.uniform(2, 11)
    spots += np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * r * r)))
spots = np.clip(spots, 0, 1) * SPOTS
tone = np.array([0.56, 0.53, 0.47]) if light_car else np.array([0.72, 0.70, 0.66])
work = work * (1 - spots[..., None]) + tone * spots[..., None]

# ---- 6. composite over the untouched bay -------------------------------------
# let the original specular highlights read back through, so lamps and glass
# keep their shine while the paint around them goes flat
keep = (np.clip((spec - 0.55) / 0.45, 0, 1) * 0.55)[..., None] * m
work = np.clip(work, 0, 1) * (1 - keep) + a * keep
out = a * (1 - m) + np.clip(work, 0, 1) * m
halo = np.clip(gaussian_filter(mask, 26) - mask, 0, 1)[..., None]
out = out * (1 - halo * 0.05) + DUST * (halo * 0.05)

Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8)).save(
    OUT, 'WEBP', quality=84, method=6)
print('wrote', OUT)
