(() => {
  const leaf = (t) => [...document.querySelectorAll('*')].filter(e =>
      e.children.length === 0 && (e.textContent||'').trim() === t)[0]
    || [...document.querySelectorAll('*')].filter(e =>
      (e.textContent||'').trim() === t).pop();
  const pick = (el, key) => {
    if (!el) return key + ': NOT FOUND';
    const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    return {size: cs.fontSize, weight: cs.fontWeight, lh: cs.lineHeight, ls: cs.letterSpacing,
      ff: cs.fontFamily.split(',')[0].replace(/"/g,''), color: cs.color, tt: cs.textTransform,
      w: Math.round(r.width), h: Math.round(r.height)};
  };
  const o = {};
  o.eyebrow   = pick(leaf('OUR CRAFT'));
  o.note      = pick(leaf('Every vehicle follows the same structured process to ensure precise, professional, and consistent results — with no shortcuts and no guesswork.'));
  o.cardTitle = pick(leaf('Preparing'));
  o.cardBody  = pick(leaf('We assess the vehicle, identify its specific needs, and carefully prepare it before any work begins.'));
  o.svcTitle  = pick(leaf('Premium wash'));
  o.price     = pick(leaf('89$'));
  o.statNum   = pick(leaf('500+'));
  o.statLabel = pick(leaf('CARS DETAILED'));
  o.navLink   = pick(leaf('GALLERY'));
  o.btnLabel  = pick(leaf('SEE OUR SERVICES'));
  o.faqQ      = pick(leaf('What products do you use ?'));
  o.cellTitle = pick(leaf('100% satisfaction'));
  o.cellBody  = pick(leaf("If it's not right, we redo it. No questions asked."));
  // hero lede paragraph
  o.heroLede  = pick([...document.querySelectorAll('p')].find(p => (p.textContent||'').startsWith('Ceramic coatings')));
  // buttons
  const b = [...document.querySelectorAll('a')].find(a => (a.textContent||'').trim() === 'SEE OUR SERVICES');
  if (b) { const cs = getComputedStyle(b), r = b.getBoundingClientRect();
    o.btnBox = {h: Math.round(r.height), w: Math.round(r.width), pad: cs.padding, radius: cs.borderRadius, bg: cs.backgroundColor}; }
  // hero: where does content sit
  const hero = document.querySelector('[data-framer-name="HERO SECTION"]');
  if (hero) { const cs = getComputedStyle(hero.querySelector('[data-framer-name="Container"]') || hero);
    o.heroPad = {pad: cs.padding, h: Math.round(hero.getBoundingClientRect().height)}; }
  return o;
})()
