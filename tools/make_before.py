"""Derive ba-before from ba-after.

Two separate generations never produce the same car, so the 'before' is made from
the 'after' image itself: the car is segmented out, aged, and composited back over
the untouched bay. Same car, same angle, same lights, guaranteed.
"""
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import gaussian_filter, zoom

SRC = 'assets/ba-after.webp'
OUT = 'assets/ba-before.webp'
rng = np.random.default_rng(7)

base = Image.open(SRC).convert('RGB')
W, H = base.size
a = np.asarray(base).astype(np.float32) / 255.0

# ---- 1. car mask -------------------------------------------------------------
from rembg import remove, new_session
session = new_session('isnet-general-use')
cut = remove(base, session=session, post_process_mask=True)
mask = np.asarray(cut.split()[-1]).astype(np.float32) / 255.0
mask = gaussian_filter(mask, 2.0)
print('car covers %.1f%% of frame' % (mask.mean() * 100))
m = mask[..., None]

# ---- 2. dust ----------------------------------------------------------------
def octave(shape, scale):
    small = rng.random((max(2, shape[0] // scale), max(2, shape[1] // scale)))
    return zoom(small, (shape[0] / small.shape[0], shape[1] / small.shape[1]), order=3)

dust = (0.38 * octave((H, W), 110) + 0.34 * octave((H, W), 40) +
        0.28 * octave((H, W), 13))
dust = (dust - dust.min()) / (np.ptp(dust) + 1e-6)
dust = gaussian_filter(dust, 1.2)

# Dust settles on upward-facing surfaces: weight toward the top of the car and
# toward areas that were already catching light (bonnet, roof, boot lid).
lum = a.mean(axis=2)
ys = np.linspace(1.15, 0.45, H)[:, None]
settle = np.clip((ys ** 2.1) * (0.25 + 1.05 * np.clip(lum * 1.7, 0, 1)), 0, 1.2)
dust_amt = np.clip(dust * settle, 0, 1)[..., None]

DUST_RGB = np.array([0.62, 0.575, 0.50], dtype=np.float32)   # warm grey-brown

# ---- 3. kill the gloss ------------------------------------------------------
soft = np.asarray(base.filter(ImageFilter.GaussianBlur(3.0))).astype(np.float32) / 255.0
work = a * 0.80 + soft * 0.20                       # soften hard specular edges
work = np.where(work > 0.62, 0.62 + (work - 0.62) * 0.58, work)   # compress highlights
work = work * 0.965 + 0.017                         # lift blacks, flatten range

grey = work.mean(axis=2, keepdims=True)
work = grey + (work - grey) * 0.80                  # desaturate

# ---- 4. lay the dust on -----------------------------------------------------
work = work * (1 - dust_amt * 0.30) + DUST_RGB * (dust_amt * 0.30)
work += (rng.random((H, W, 1)).astype(np.float32) - 0.5) * 0.030 * dust_amt   # grit

# ---- 5. dried water spots ---------------------------------------------------
spots = np.zeros((H, W), dtype=np.float32)
yy, xx = np.mgrid[0:H, 0:W]
for _ in range(95):
    cx, cy = rng.integers(0, W), rng.integers(int(H * 0.22), int(H * 0.72))
    r = rng.uniform(2.5, 7)
    spots += np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * r * r)))
spots = np.clip(spots, 0, 1) * 0.13
work = work * (1 - spots[..., None]) + np.array([0.72, 0.70, 0.66]) * spots[..., None]

# ---- 6. composite over the untouched bay ------------------------------------
out = a * (1 - m) + np.clip(work, 0, 1) * m

# a faint haze of overspray on the floor right around the car, so it doesn't
# look like a clean car was pasted onto a dirty one
halo = np.clip(gaussian_filter(mask, 26) - mask, 0, 1)[..., None]
out = out * (1 - halo * 0.07) + DUST_RGB * (halo * 0.07)

Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8)).save(
    OUT, 'WEBP', quality=84, method=6)
print('wrote', OUT)
