"""Paint a number plate flat.

Generators keep rendering a model wordmark where the plate should be, which is an
obvious artefact and inconsistent with every other vehicle on the site. This fills
the plate interior column by column using the median of that column's own dark
pixels, so the plate keeps its real lighting falloff and texture.

usage: python3 tools/blank_plate.py <src> <dst> x0 x1 y0 y1
"""
import sys
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

src, dst = sys.argv[1], sys.argv[2]
x0, x1, y0, y1 = (int(v) for v in sys.argv[3:7])
rng = np.random.default_rng(3)

im = Image.open(src).convert('RGB')
a = np.asarray(im).astype(np.float32)
plate = a[y0:y1, x0:x1].copy()
h, w, _ = plate.shape
lum = plate.mean(axis=2)
thresh = np.percentile(lum, 45)

fill = np.zeros_like(plate)
for x in range(w):
    col = plate[:, x]
    dark = col[lum[:, x] <= thresh]
    if len(dark) < 4:
        dark = col[np.argsort(lum[:, x])[:max(4, h // 3)]]
    fill[:, x] = np.median(dark, axis=0)

# keep the plate's vertical shading rather than a flat slab
shade = np.linspace(1.06, 0.93, h)[:, None, None]
fill = fill * shade
fill = gaussian_filter(fill, (1.6, 1.2, 0))
fill += (rng.random((h, w, 1)).astype(np.float32) - 0.5) * 3.0

# feather the edges so it sits inside the existing frame
m = np.ones((h, w), dtype=np.float32)
f = 3
m[:f, :] = np.linspace(0, 1, f)[:, None]
m[-f:, :] = np.linspace(1, 0, f)[:, None]
m[:, :f] *= np.linspace(0, 1, f)[None, :]
m[:, -f:] *= np.linspace(1, 0, f)[None, :]
m = gaussian_filter(m, 1.0)[..., None]

a[y0:y1, x0:x1] = plate * (1 - m) + np.clip(fill, 0, 255) * m
Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(dst)
print('wrote', dst)
