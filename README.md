# Wash and Guard Auto Detailing

Landing page mockup for Wash and Guard Auto Detailing, Taman Petaling Utama, Petaling Jaya.
Static HTML, CSS and JavaScript. No build step, no dependencies beyond Google Fonts.

```
index.html      the page
styles.css      all styling
script.js       reveals, ticker, before/after slider, accordion, form
assets/         images, video, logo
tools/          headless-Chrome measuring scripts used to build it
```

## Not ready to publish

The page carries `noindex` on purpose. Before it goes live:

- **The four reviews are invented.** The business has not opened and has no customers.
- Service "from" prices are placeholders except the RM 165 bike price. The client's deck prices
  packages, not individual services.
- Opening hours are a placeholder. Phone and email are the client's real details.

`CONTENT.md` tracks every fact as CONFIRMED, PLACEHOLDER or BLOCKER.

## Reference

Layout and interaction mechanics follow a Framer template the client picked; all media and copy are
Wash and Guard's own. `TEARDOWN.md` records the measured spec — type scale, spacing, and the five
motion behaviours, each measured from the live reference rather than estimated.

## Local preview

```bash
python3 -m http.server 8080
```
