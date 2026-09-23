(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const nav = [...document.querySelectorAll('*')].find(el => {
    const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    return cs.position === 'fixed' && r.height > 40 && r.width > 300 && r.top < 50;
  });
  const out = {};
  const snap = () => {
    const rows = [];
    const walk = (el, d) => {
      const cs = getComputedStyle(el), r = el.getBoundingClientRect();
      if (r.height > 20 && r.width > 200) {
        rows.push({d, name: el.getAttribute('data-framer-name'), tag: el.tagName,
          bg: cs.backgroundColor, bd: cs.backdropFilter, op: cs.opacity,
          border: cs.borderBottomWidth + ' ' + cs.borderBottomColor,
          h: Math.round(r.height), top: Math.round(r.top), tf: cs.transform.slice(0,44)});
      }
      if (d < 4) [...el.children].forEach(c => walk(c, d + 1));
    };
    walk(nav, 0);
    return rows;
  };
  for (const y of [0, 200, 600, 1500, 4000]) {
    scrollTo(0, y); await sleep(900);
    out['y' + y] = snap();
  }
  return out;
})()
