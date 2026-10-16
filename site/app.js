/* Lesson-Deck-Builder docs — small, dependency-free behaviour:
   canvas switcher, table-of-contents highlight, live-deck tabs, copy buttons, prompt builder. */
(function () {
  const root = document.documentElement;
  const KEY = 'ldb-docs-canvas';

  /* ---------- canvas + board switcher (mirrors a deck's <html data-canvas data-board>) ---------- */
  function applyCanvas(v) {
    if (v === 'paper') { root.setAttribute('data-canvas', 'paper'); root.removeAttribute('data-board'); }
    else { root.setAttribute('data-canvas', 'chalkboard'); root.setAttribute('data-board', v); }
    document.querySelectorAll('[data-set-canvas]').forEach(b =>
      b.setAttribute('aria-pressed', String(b.dataset.setCanvas === v)));
    const out = document.getElementById('canvas-attr');
    if (out) out.textContent = v === 'paper'
      ? '<html data-canvas="paper">'
      : '<html data-canvas="chalkboard" data-board="' + v + '">';
  }
  function currentCanvas() {
    return root.getAttribute('data-canvas') === 'chalkboard' ? (root.getAttribute('data-board') || 'slate-reinked') : 'paper';
  }
  applyCanvas(currentCanvas());
  document.querySelectorAll('[data-set-canvas]').forEach(b => b.addEventListener('click', () => {
    const v = b.dataset.setCanvas;
    applyCanvas(v);
    try { localStorage.setItem(KEY, v); } catch (e) { /* storage blocked: the choice just won't be remembered */ }
  }));

  /* ---------- table of contents: highlight the section in view ---------- */
  const tocLinks = [...document.querySelectorAll('.toc a[href^="#"]')];
  const byId = new Map(tocLinks.map(a => [a.getAttribute('href').slice(1), a]));
  if ('IntersectionObserver' in window && tocLinks.length) {
    const seen = new Set();
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) seen.add(e.target.id); else seen.delete(e.target.id); });
      const first = [...byId.keys()].find(id => seen.has(id));
      if (first) tocLinks.forEach(a => a.classList.toggle('on', a === byId.get(first)));
    }, { rootMargin: '-80px 0px -55% 0px' });
    byId.forEach((_, id) => { const s = document.getElementById(id); if (s) io.observe(s); });
  }

  /* ---------- scale embedded decks: render at 1120×700, shrink to fit; phones get the native size ---------- */
  function fit(vp) {
    const w = vp.clientWidth;
    vp.classList.toggle('native', w < 520);
    if (w >= 520) { const s = w / 1120; vp.style.setProperty('--s', s); vp.style.aspectRatio = '1120 / 700'; }
    else vp.style.aspectRatio = '';
  }
  const vps = [...document.querySelectorAll('.frame .vp')];
  vps.forEach(fit);
  if ('ResizeObserver' in window) { const ro = new ResizeObserver(es => es.forEach(e => fit(e.target))); vps.forEach(v => ro.observe(v)); }
  else window.addEventListener('resize', () => vps.forEach(fit));

  /* ---------- live deck frames with tabs ---------- */
  document.querySelectorAll('[data-frame]').forEach(box => {
    const frame = box.querySelector('iframe');
    const open = box.querySelector('[data-open]');
    const cap = box.querySelector('[data-caption]');
    const tabs = [...box.querySelectorAll('[role="tab"]')];
    function pick(t) {
      tabs.forEach(x => x.setAttribute('aria-selected', String(x === t)));
      if (frame.getAttribute('src') !== t.dataset.src) frame.setAttribute('src', t.dataset.src);
      if (open) open.href = t.dataset.src;
      if (cap) cap.textContent = t.dataset.cap || '';
    }
    tabs.forEach(t => t.addEventListener('click', () => pick(t)));
    // lazy-load: only set the first src when the frame comes near the viewport
    const first = tabs.find(t => t.getAttribute('aria-selected') === 'true') || tabs[0];
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver(es => { if (es.some(e => e.isIntersecting)) { pick(first); io.disconnect(); } }, { rootMargin: '300px' });
      io.observe(box);
    } else pick(first);
  });

  /* ---------- copy buttons ---------- */
  const toast = document.createElement('div');
  toast.className = 'toast'; toast.setAttribute('role', 'status'); document.body.appendChild(toast);
  let tt;
  function say(msg) { toast.textContent = msg; toast.classList.add('on'); clearTimeout(tt); tt = setTimeout(() => toast.classList.remove('on'), 1600); }
  async function copyText(text) {
    try { await navigator.clipboard.writeText(text); say('Copied'); }
    catch (e) {
      const ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); say('Copied'); } catch (err) { say('Select the text and copy it'); }
      ta.remove();
    }
  }
  document.querySelectorAll('.code').forEach(c => {
    const btn = c.querySelector('.copy'); const pre = c.querySelector('pre');
    if (btn && pre) btn.addEventListener('click', () => copyText(pre.innerText.replace(/\n$/, '')));
  });

  /* ---------- prompt builder ---------- */
  const form = document.getElementById('pb');
  if (form) {
    const out = document.getElementById('pb-out');
    const boardRow = document.getElementById('pb-board-row');
    const teachOnly = [...form.querySelectorAll('[data-teach-only]')];
    const val = n => (form.querySelector('[name="' + n + '"]:checked') || {}).value || '';
    const BOARD_NAMES = { 'slate-reinked': 'Slate re-inked', 'midnight-blue': 'Midnight blue', 'olive-gold': 'Olive gold',
      'dusk-indigo': 'Dusk indigo', 'deep-teal': 'Deep teal', 'red-graphite': 'Red graphite' };
    function build() {
      const mode = val('mode');
      const topic = (form.querySelector('#pb-topic').value || '').trim() || '<your topic>';
      const lang = val('lang'), canvas = val('canvas'), board = val('board'), level = val('level'), len = val('len');
      boardRow.classList.toggle('hidden', canvas !== 'chalkboard');
      teachOnly.forEach(el => el.classList.toggle('hidden', mode === 'rulebook'));
      let lines = [];
      if (mode === 'rulebook') {
        lines.push('/lesson-deck-builder');
        lines.push('Follow slides-rulebook.md for the attached lecture, and end the deck with a final quiz following questions-rulebook.md. Read the attached notes before planning.');
        if (canvas === 'ask') lines.push('This is the first deck of a new course: ask me the canvas and board before building.');
        else lines.push('Canvas: ' + (canvas === 'paper' ? 'paper' : 'chalkboard, board ' + BOARD_NAMES[board]) + '.');
        out.textContent = lines.join('\n');
        return;
      }
      const kind = mode === 'present' ? 'a presentation deck' : mode === 'journey' ? 'a learning journey (roadmap + lesson 1)' : 'a teaching deck';
      lines.push('/lesson-deck-builder');
      lines.push('Make ' + kind + ' about ' + topic + '.');
      const bits = [];
      if (lang !== 'ask') bits.push('Language: ' + lang + '.');
      if (canvas === 'paper') bits.push('Canvas: paper.');
      else if (canvas === 'chalkboard') bits.push('Canvas: chalkboard, board ' + BOARD_NAMES[board] + '.');
      if (level !== 'ask') bits.push('Audience: ' + level + '.');
      if (len !== 'ask' && mode !== 'journey') bits.push('Length: about ' + len + ' minutes.');
      if (bits.length) lines.push(bits.join(' '));
      const asked = [];
      if (lang === 'ask') asked.push('the language');
      if (canvas === 'ask') asked.push('the canvas');
      if (asked.length) lines.push('(Claude will ask you ' + asked.join(' and ') + ' first.)');
      out.textContent = lines.join('\n');
    }
    form.addEventListener('input', build); form.addEventListener('change', build);
    build();
    const cp = document.getElementById('pb-copy');
    if (cp) cp.addEventListener('click', () => copyText(out.textContent.replace(/\n\(Claude will ask[^)]*\)$/, '')));
  }
})();
