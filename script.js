(function () {
  'use strict';
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1. scroll reveal ----------
     Measured on the reference: opacity 0→1 and translateY 60px→0 over ~1.25s,
     firing when the element passes ~75% of the viewport. Plays once. */
  var revealables = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || reduced) {
    revealables.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -25% 0px', threshold: 0.01 });
    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ---------- 2. mobile menu ---------- */
  var burger = document.getElementById('burger');
  var menu = document.getElementById('mobile-menu');
  if (burger && menu) {
    var setMenu = function (open) {
      menu.hidden = !open;
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      document.body.style.overflow = open ? 'hidden' : '';
    };
    burger.addEventListener('click', function () {
      setMenu(burger.getAttribute('aria-expanded') !== 'true');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !menu.hidden) setMenu(false);
    });
  }

  /* ---------- 3. FAQ accordion ---------- */
  document.querySelectorAll('.qa .q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var qa = btn.parentElement;
      var open = qa.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(open));
    });
  });

  /* ---------- 4. reviews ticker ----------
     Measured on the reference: continuous leftward drift at 35.2 px/s. */
  var track = document.getElementById('ticker-track');
  var tickerBox = document.getElementById('ticker');
  if (track && !reduced) {
    var SPEED = 35.2;
    var originals = Array.prototype.slice.call(track.children);
    originals.forEach(function (node) {
      var clone = node.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      track.appendChild(clone);
    });
    var offset = 0, half = 0, last = 0, paused = false, visible = false;

    var measure = function () {
      half = 0;
      var gap = parseFloat(getComputedStyle(track).gap) || 0;
      originals.forEach(function (n) { half += n.getBoundingClientRect().width + gap; });
    };
    measure();
    window.addEventListener('resize', function () { measure(); });

    tickerBox.addEventListener('mouseenter', function () { paused = true; });
    tickerBox.addEventListener('mouseleave', function () { paused = false; });

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { visible = es[0].isIntersecting; },
        { threshold: 0 }).observe(tickerBox);
    } else { visible = true; }

    var tick = function (now) {
      if (!last) last = now;
      var dt = Math.min((now - last) / 1000, 0.05);
      last = now;
      if (visible && !paused && half > 0) {
        offset -= SPEED * dt;
        if (offset <= -half) offset += half;
        track.style.transform = 'translate3d(' + offset.toFixed(2) + 'px,0,0)';
      }
      requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  /* ---------- 5. before / after ----------
     Measured on the reference: clip-path inset right ping-pongs between 8% and 92%,
     sweeping in ~1.2s with a short dwell at each end. Dragging takes over.

     `pos` is the handle's distance from the left edge. The clipped top layer holds
     the BEFORE image and is revealed from the left edge out to the handle, so the
     left of the handle is always the before and the right is always the after —
     which is what the two labels say. The arrows nudge the handle in the direction
     they point rather than jumping to a named state, because "show before" is
     ambiguous once the wipe can run either way. */
  var ba = document.getElementById('ba');
  var baTop = document.getElementById('ba-top');
  var baHandle = document.getElementById('ba-handle');
  if (ba && baTop && baHandle) {
    var MIN = 8, MAX = 92, SWEEP = 1200, DWELL = 700;
    var pos = 50, manual = false, inView = false, t0 = null, dir = 1;

    var paint = function (p) {
      pos = Math.max(0, Math.min(100, p));
      baTop.style.clipPath = 'inset(0 ' + (100 - pos) + '% 0 0)';
      baHandle.style.left = pos + '%';
      baHandle.setAttribute('aria-valuenow', String(Math.round(pos)));
    };
    paint(50);

    var easeInOut = function (t) {
      return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    };

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        inView = es[0].isIntersecting;
        if (!inView) t0 = null;
      }, { threshold: 0.25 }).observe(ba);
    } else { inView = true; }

    var auto = function (now) {
      if (!manual && inView && !reduced) {
        if (t0 === null) { t0 = now; }
        var cycle = SWEEP + DWELL;
        var el = (now - t0) % (cycle * 2);
        var from = dir > 0 ? MIN : MIN;
        if (el < SWEEP) {
          paint(MIN + (MAX - MIN) * easeInOut(el / SWEEP));
        } else if (el < cycle) {
          paint(MAX);
        } else if (el < cycle + SWEEP) {
          paint(MAX - (MAX - MIN) * easeInOut((el - cycle) / SWEEP));
        } else {
          paint(MIN);
        }
      }
      requestAnimationFrame(auto);
    };
    requestAnimationFrame(auto);

    var fromEvent = function (e) {
      var r = ba.getBoundingClientRect();
      var x = (e.touches ? e.touches[0].clientX : e.clientX) - r.left;
      paint((x / r.width) * 100);
    };
    var startDrag = function (e) {
      manual = true;
      fromEvent(e);
      var move = function (ev) { ev.preventDefault(); fromEvent(ev); };
      var end = function () {
        window.removeEventListener('pointermove', move);
        window.removeEventListener('pointerup', end);
      };
      window.addEventListener('pointermove', move, { passive: false });
      window.addEventListener('pointerup', end);
    };
    ba.addEventListener('pointerdown', startDrag);

    baHandle.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
        e.preventDefault();
        manual = true;
        paint(pos + (e.key === 'ArrowRight' ? 4 : -4));
      }
    });

    var glide = function (target) {
      manual = true;
      var start = pos, t = null;
      var step = function (now) {
        if (t === null) t = now;
        var k = Math.min((now - t) / 600, 1);
        paint(start + (target - start) * easeInOut(k));
        if (k < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    var prev = document.getElementById('ba-prev');
    var next = document.getElementById('ba-next');
    if (prev) prev.addEventListener('click', function () { glide(MIN); });
    if (next) next.addEventListener('click', function () { glide(MAX); });
  }
})();

/* ---------- 6. roll-up hover ----------
   Wraps each control's label so it can roll out of the top while a copy rolls in
   from below. Done here rather than in the markup so the HTML stays readable and
   the page still reads correctly with JavaScript off. */
(function () {
  var targets = document.querySelectorAll('.btn, .nav-links a, .foot-col a, .mobile-menu a');
  Array.prototype.forEach.call(targets, function (el) {
    Array.prototype.forEach.call(el.childNodes, function (node) {
      if (node.nodeType !== 3) return;
      var text = node.textContent.replace(/\s+/g, ' ').trim();
      if (!text) return;
      var roll = document.createElement('span');
      roll.className = 'roll';
      var a = document.createElement('span');
      a.className = 'roll-a';
      a.textContent = text;
      var b = document.createElement('span');
      b.className = 'roll-b';
      b.textContent = text;
      b.setAttribute('aria-hidden', 'true');
      roll.appendChild(a);
      roll.appendChild(b);
      el.replaceChild(roll, node);
    });
  });
})();

/* ---------- 7. booking form -> WhatsApp ----------
   No backend on a static page, so the form composes a WhatsApp message instead.
   WA_NUMBER is the studio's real WhatsApp line. */
(function () {
  var WA_NUMBER = '601126161356';
  var form = document.getElementById('booking-form');
  if (!form) return;
  var note = document.getElementById('form-note');
  var noteDefault = note ? note.textContent : '';

  var invalid = function (el, bad) {
    if (bad) { el.setAttribute('aria-invalid', 'true'); }
    else { el.removeAttribute('aria-invalid'); }
  };

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name = form.elements.name.value.trim();
    var phone = form.elements.phone.value.trim();
    invalid(form.elements.name, !name);
    invalid(form.elements.phone, !phone);
    if (!name || !phone) {
      if (note) {
        note.textContent = 'Please add your name and a number we can reach you on.';
        note.style.color = '#B4442E';
      }
      (!name ? form.elements.name : form.elements.phone).focus();
      return;
    }
    if (note) { note.textContent = noteDefault; note.style.color = ''; }

    var lines = [
      'Hi Wash and Guard, I would like to book a slot.',
      '',
      'Name: ' + name,
      'Contact: ' + phone,
      'Vehicle: ' + form.elements.type.value + ' — ' + (form.elements.model.value.trim() || 'to confirm'),
      'Service: ' + form.elements.service.value
    ];
    var notes = form.elements.notes.value.trim();
    if (notes) { lines.push('Notes: ' + notes); }

    window.open('https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
  });
})();

/* ---------- 8. scrolled nav ----------
   The reference swaps to a solid header variant once the page moves. Same idea
   here, in ink so the gold wordmark and white links stay legible. */
(function () {
  var nav = document.getElementById('nav');
  if (!nav) return;
  var ticking = false;
  var apply = function () {
    nav.classList.toggle('scrolled', window.scrollY > 40);
    ticking = false;
  };
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(apply); }
  }, { passive: true });
  apply();
})();
