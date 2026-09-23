(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const mx = el => { const m = getComputedStyle(el).transform.match(/matrix\(([^)]+)\)/); return m ? parseFloat(m[1].split(',')[4]) : 0; };
  const my = el => { const m = getComputedStyle(el).transform.match(/matrix\(([^)]+)\)/); return m ? parseFloat(m[1].split(',')[5]) : 0; };
  const out = {};

  // --- NAV ---
  const nav = [...document.querySelectorAll('*')].find(el => {
    const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    return cs.position === 'fixed' && r.height > 40 && r.width > 300 && r.top < 50;
  });
  out.nav = {};
  for (const y of [0, 400, 1200, 3000, 1000]) {
    scrollTo(0, y); await sleep(700);
    const r = nav.getBoundingClientRect(), cs = getComputedStyle(nav);
    out.nav['y'+y] = {top: Math.round(r.top), h: Math.round(r.height), op: cs.opacity, bg: cs.backgroundColor, ty: Math.round(my(nav))};
  }

  // --- TICKER (testimonials) ---
  const t = [...document.querySelectorAll('[data-framer-name="TESTIMONIALS"]')][0];
  t.scrollIntoView({block:'center'}); await sleep(2500);
  const track = [...t.querySelectorAll('*')].find(el => el.children.length === 4 && getComputedStyle(el).transform.startsWith('matrix'));
  const p = [];
  for (let i=0;i<6;i++){ p.push(+mx(track).toFixed(2)); await sleep(700); }
  out.ticker = {samples: p, trackW: Math.round(track.getBoundingClientRect().width),
                cardW: Math.round(track.children[0].getBoundingClientRect().width),
                gap: getComputedStyle(track).gap, pxPerSec: +(((p[5]-p[0])/3.5)).toFixed(1)};

  // --- BEFORE/AFTER ---
  const ba = [...document.querySelectorAll('[data-framer-name="BEFORE AFTER SECTION"]')][0];
  ba.scrollIntoView({block:'center'}); await sleep(2000);
  const clipEl = [...ba.querySelectorAll('*')].find(el => getComputedStyle(el).clipPath !== 'none');
  const c = [];
  for (let i=0;i<6;i++){ c.push(getComputedStyle(clipEl).clipPath); await sleep(700); }
  out.beforeAfter = {clips: c, w: Math.round(clipEl.getBoundingClientRect().width), h: Math.round(clipEl.getBoundingClientRect().height)};

  // --- REVEAL: watch the team section animate in ---
  scrollTo(0, 0); await sleep(1200);
  const team = [...document.querySelectorAll('[data-framer-name="TEAM SECTION"]')][0];
  const target = team.querySelector('h2, [data-framer-name="Header"]') || team.children[0];
  const before = {op: getComputedStyle(target).opacity, ty: +my(target).toFixed(1)};
  const tTop = team.getBoundingClientRect().top + scrollY;
  scrollTo(0, tTop - innerHeight * 0.75);
  const frames = [];
  const t0 = performance.now();
  while (performance.now() - t0 < 1600) {
    frames.push({t: Math.round(performance.now()-t0), op: +getComputedStyle(target).opacity, ty: +my(target).toFixed(1)});
    await new Promise(r => requestAnimationFrame(r));
  }
  out.reveal = {before, frames: frames.filter((f,i) => i % 4 === 0).slice(0, 26)};

  return out;
})()
