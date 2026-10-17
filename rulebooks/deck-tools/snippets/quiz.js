/* ===== FINAL QUIZ — 9 question kinds, one check per question, score on the last slide ===== */
(function(){
  const qs=[...document.querySelectorAll('.fq')]; if(!qs.length) return;
  const state=qs.map(()=>null);                      // null = not answered · true · false
  const resets=[];
  const num=t=>t.replace(/[\s,]/g,'');
  const shuffle=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;};
  const TICK='<svg viewBox="0 0 30 30"><path class="scrib" pathLength="1" d="M4 6 L26 24 M26 6 L4 24" stroke="var(--red)" stroke-width="2.6" fill="none" stroke-linecap="round"/><path class="tick" pathLength="1" d="M5 16 L12 24 L27 4" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round" filter="url(#wob)"/></svg>';

  qs.forEach((q,i)=>{
    const v=q.querySelector('.verdict'), type=q.dataset.type, chk=q.querySelector('.fq-check');
    const finish=(ok,extra)=>{
      state[i]=ok; q.classList.add('locked');
      v.textContent=(ok?'Yes. ':'Not quite. ')+(extra?extra+' ':'')+q.dataset.why; v.classList.add('show');
      q.querySelectorAll('input,select,.fq-grp button,.fq-check,.fq-clear').forEach(e=>e.disabled=true);
    };
    const unlock=()=>{
      state[i]=null; q.classList.remove('locked'); v.textContent=''; v.classList.remove('show');
      q.querySelectorAll('input,select,.fq-grp button,.fq-check,.fq-clear').forEach(e=>e.disabled=false);
      q.querySelectorAll('.ok,.no,.ans,.picked,.correct,.wrong').forEach(e=>e.classList.remove('ok','no','ans','picked','correct','wrong'));
      q.querySelectorAll('.fix').forEach(e=>e.remove());
    };

    if(type==='mcq'){
      q.querySelectorAll('.opt .box').forEach(b=>b.innerHTML=TICK);
      q.querySelectorAll('.opt').forEach(b=>b.addEventListener('click',()=>{
        if(state[i]!==null) return;
        const ok=b.dataset.ok==='1'; b.classList.add(ok?'correct':'wrong');
        if(!ok) q.querySelector('.opt[data-ok="1"]').classList.add('correct');
        finish(ok);
      }));
      resets[i]=unlock;
    }

    if(type==='gap'){
      /* word bank: drag a word into the gap, or tap it; tap a filled gap to send its word back */
      const drop=q.querySelector('.drop'), bank=q.querySelector('.bank'), chips=[...bank.querySelectorAll('.chip')];
      const order=chips.slice();
      const place=c=>{ if(state[i]!==null) return; const old=drop.querySelector('.chip'); if(old===c) return;
        if(old) bank.appendChild(old); drop.appendChild(c); drop.classList.add('full');
        order.forEach(x=>{ if(x.parentNode===bank) bank.appendChild(x); }); };
      const back=()=>{ if(state[i]!==null) return; const c=drop.querySelector('.chip'); if(!c) return;
        bank.appendChild(c); drop.classList.remove('full'); order.forEach(x=>{ if(x.parentNode===bank) bank.appendChild(x); }); };
      chips.forEach(c=>{
        let sx=0, sy=0, ghost=null, moved=false;
        c.addEventListener('pointerdown',e=>{ if(state[i]!==null||e.button>0) return;
          sx=e.clientX; sy=e.clientY; moved=false; c.setPointerCapture(e.pointerId); });
        c.addEventListener('pointermove',e=>{ if(!c.hasPointerCapture(e.pointerId)) return;
          if(!moved&&Math.hypot(e.clientX-sx,e.clientY-sy)<6) return;
          if(!moved){ moved=true; const r=c.getBoundingClientRect(); ghost=c.cloneNode(true); ghost.classList.add('ghost');
            ghost.style.width=r.width+'px'; document.body.appendChild(ghost); c.classList.add('lifted'); }
          ghost.style.left=(e.clientX-ghost.offsetWidth/2)+'px'; ghost.style.top=(e.clientY-ghost.offsetHeight/2)+'px';
          const over=document.elementFromPoint(e.clientX,e.clientY); drop.classList.toggle('over',!!over&&drop.contains(over)); });
        const end=e=>{ if(!c.hasPointerCapture(e.pointerId)) return; c.releasePointerCapture(e.pointerId);
          if(!moved) return;
          const over=document.elementFromPoint(e.clientX,e.clientY);
          ghost.remove(); ghost=null; c.classList.remove('lifted'); drop.classList.remove('over');
          if(over&&drop.contains(over)) place(c); else if(c.parentNode===drop) back();
          c.dataset.dragged='1'; setTimeout(()=>delete c.dataset.dragged,0); };
        c.addEventListener('pointerup',end); c.addEventListener('pointercancel',end);
        c.addEventListener('click',e=>{ e.stopPropagation(); if(c.dataset.dragged) return;
          if(c.parentNode===drop) back(); else place(c); });
      });
      drop.addEventListener('click',back);
      drop.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); back(); } });
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        const c=drop.querySelector('.chip');
        if(!c){ v.textContent='Drag a word into the gap first.'; v.classList.add('show'); return; }
        const ok=c.textContent.trim()===q.dataset.answer; drop.classList.add(ok?'ok':'no');
        if(!ok) chips.find(x=>x.textContent.trim()===q.dataset.answer).classList.add('ans');
        q.querySelectorAll('.chip').forEach(x=>x.disabled=true);
        finish(ok, ok?'':'Answer: '+q.dataset.answer+'.'); });
      resets[i]=()=>{ unlock(); q.querySelectorAll('.chip').forEach(x=>x.disabled=false);
        const c=drop.querySelector('.chip'); if(c) bank.appendChild(c); drop.classList.remove('full');
        order.forEach(x=>bank.appendChild(x)); };
    }

    if(type==='num'){
      const inp=q.querySelector('input.gap');
      const run=()=>{ if(state[i]!==null||!inp.value.trim()) return;
        const ok=num(inp.value)===q.dataset.answer; inp.classList.add(ok?'ok':'no'); finish(ok); };
      chk.addEventListener('click',run);
      inp.addEventListener('keydown',e=>{ if(e.key==='Enter'){ e.preventDefault(); run(); } });
      resets[i]=()=>{ unlock(); inp.value=''; };
    }

    if(type==='match'){
      const choices=[...q.querySelectorAll('.fq-choices li')].map(li=>({k:li.dataset.key,t:li.textContent}));
      const rows=[...q.querySelectorAll('.fq-row')];
      const fill=()=>{ const order=shuffle(choices.slice());
        rows.forEach(r=>{ const s=r.querySelector('select');
          s.innerHTML='<option value="">Choose…</option>'+order.map(c=>`<option value="${c.k}">${c.t}</option>`).join('');
          s.setAttribute('aria-label','meaning of '+r.querySelector('.fq-term').textContent); }); };
      fill();
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        if(rows.some(r=>!r.querySelector('select').value)){ v.textContent='Choose a meaning for every term first.'; v.classList.add('show'); return; }
        let good=0;
        rows.forEach(r=>{ const ok=r.querySelector('select').value===r.dataset.key; r.classList.add(ok?'ok':'no'); if(ok) good++;
          else{ const f=document.createElement('span'); f.className='fix'; f.textContent='→ '+choices.find(c=>c.k===r.dataset.key).t; r.appendChild(f);} });
        finish(good===rows.length, good===rows.length?'':good+' of '+rows.length+' right.'); });
      resets[i]=()=>{ unlock(); fill(); };
    }

    if(type==='sort'){
      const groups=q.dataset.groups.split('|'), rows=[...q.querySelectorAll('.fq-row')];
      rows.forEach(r=>{ const g=document.createElement('div'); g.className='fq-grp';
        groups.forEach(name=>{ const b=document.createElement('button'); b.type='button'; b.textContent=name; b.dataset.g=name;
          b.addEventListener('click',()=>{ if(state[i]!==null) return; g.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b)); });
          g.appendChild(b); });
        r.appendChild(g); });
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        if(rows.some(r=>!r.querySelector('.fq-grp .on'))){ v.textContent='Put every item in a group first.'; v.classList.add('show'); return; }
        let good=0;
        rows.forEach(r=>{ const ok=r.querySelector('.fq-grp .on').dataset.g===r.dataset.g; r.classList.add(ok?'ok':'no'); if(ok) good++;
          else{ const f=document.createElement('span'); f.className='fix'; f.textContent='→ '+r.dataset.g; r.appendChild(f);} });
        finish(good===rows.length, good===rows.length?'':good+' of '+rows.length+' right.'); });
      resets[i]=()=>{ unlock(); q.querySelectorAll('.fq-grp .on').forEach(b=>b.classList.remove('on')); };
    }

    if(type==='order'){
      const items=[...q.querySelectorAll('.fq-it')], picked=[];
      const paint=()=>items.forEach(it=>{ const p=picked.indexOf(it); it.querySelector('.fq-num').textContent=p<0?'':p+1; it.classList.toggle('picked',p>=0); });
      items.forEach(it=>it.addEventListener('click',()=>{ if(state[i]!==null) return;
        const p=picked.indexOf(it); if(p>=0) picked.splice(p,1); else picked.push(it); paint(); }));
      q.querySelector('.fq-clear').addEventListener('click',()=>{ if(state[i]!==null) return; picked.length=0; paint(); });
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        if(picked.length<items.length){ v.textContent='Tap every step first ('+picked.length+' of '+items.length+').'; v.classList.add('show'); return; }
        let good=0;
        picked.forEach((it,k)=>{ const ok=+it.dataset.n===k+1; it.classList.add(ok?'ok':'no'); if(ok) good++;
          else{ const f=document.createElement('span'); f.className='fix'; f.textContent='should be '+it.dataset.n; it.appendChild(f);} });
        finish(good===items.length, good===items.length?'':good+' of '+items.length+' in place.'); });
      resets[i]=()=>{ unlock(); picked.length=0; paint(); };
    }

    if(type==='spot'){
      q.querySelectorAll('.fq-ch').forEach(c=>c.addEventListener('click',()=>{ if(state[i]!==null) return;
        const ok=c.dataset.ok==='1'; c.classList.add(ok?'ok':'no');
        if(!ok) q.querySelector('.fq-ch[data-ok="1"]').classList.add('ans');
        finish(ok); }));
      resets[i]=unlock;
    }

    if(type==='label'){
      /* label the figure (new kind, deck 2): one drop per numbered slot. Drag a label onto a slot, or tap a slot and then a label
         (a tapped label fills the chosen slot, else the first empty one); tap a filled slot to send its label back. */
      const drops=[...q.querySelectorAll('.drop')], bank=q.querySelector('.bank'), chips=[...bank.querySelectorAll('.chip')];
      const order=chips.slice(); let sel=null;
      const tidy=()=>order.forEach(x=>{ if(x.parentNode===bank) bank.appendChild(x); });
      const mark=d=>{ sel=d; drops.forEach(x=>x.classList.toggle('sel',x===d)); };
      const back=d=>{ if(state[i]!==null) return; const c=d.querySelector('.chip'); if(!c) return;
        bank.appendChild(c); d.classList.remove('full'); tidy(); };
      const put=(c,d)=>{ if(state[i]!==null) return; const old=d.querySelector('.chip'); if(old===c) return;
        const from=c.parentNode.classList.contains('drop')?c.parentNode:null;
        if(old) bank.appendChild(old);
        d.appendChild(c); d.classList.add('full'); if(from) from.classList.remove('full'); tidy();
        mark(drops.find(x=>!x.querySelector('.chip'))||null); };
      const target=()=>(sel&&!sel.querySelector('.chip'))?sel:(drops.find(x=>!x.querySelector('.chip'))||sel);
      chips.forEach(c=>{
        let sx=0, sy=0, ghost=null, moved=false, hot=null;
        c.addEventListener('pointerdown',e=>{ if(state[i]!==null||e.button>0) return;
          sx=e.clientX; sy=e.clientY; moved=false; c.setPointerCapture(e.pointerId); });
        c.addEventListener('pointermove',e=>{ if(!c.hasPointerCapture(e.pointerId)) return;
          if(!moved&&Math.hypot(e.clientX-sx,e.clientY-sy)<6) return;
          if(!moved){ moved=true; const r=c.getBoundingClientRect(); ghost=c.cloneNode(true); ghost.classList.add('ghost');
            ghost.style.width=r.width+'px'; document.body.appendChild(ghost); c.classList.add('lifted'); }
          ghost.style.left=(e.clientX-ghost.offsetWidth/2)+'px'; ghost.style.top=(e.clientY-ghost.offsetHeight/2)+'px';
          const over=document.elementFromPoint(e.clientX,e.clientY); hot=over&&drops.find(d=>d.contains(over))||null;
          drops.forEach(d=>d.classList.toggle('over',d===hot)); });
        const end=e=>{ if(!c.hasPointerCapture(e.pointerId)) return; c.releasePointerCapture(e.pointerId);
          if(!moved) return;
          const over=document.elementFromPoint(e.clientX,e.clientY), d=over&&drops.find(x=>x.contains(over));
          ghost.remove(); ghost=null; c.classList.remove('lifted'); drops.forEach(x=>x.classList.remove('over'));
          if(d) put(c,d); else if(c.parentNode.classList.contains('drop')) back(c.parentNode);
          c.dataset.dragged='1'; setTimeout(()=>delete c.dataset.dragged,0); };
        c.addEventListener('pointerup',end); c.addEventListener('pointercancel',end);
        c.addEventListener('click',e=>{ e.stopPropagation(); if(c.dataset.dragged||state[i]!==null) return;
          if(c.parentNode.classList.contains('drop')){ const d=c.parentNode; back(d); mark(d); }
          else{ const t=target(); if(t) put(c,t); } });
      });
      drops.forEach(d=>{
        const tap=()=>{ if(state[i]!==null) return; if(d.querySelector('.chip')) back(d); mark(d); };
        d.addEventListener('click',tap);
        d.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); tap(); } });
      });
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        const open=drops.filter(d=>!d.querySelector('.chip')).length;
        if(open){ v.textContent='Put a label on every number first ('+(drops.length-open)+' of '+drops.length+').'; v.classList.add('show'); return; }
        let good=0;
        drops.forEach(d=>{ const ok=d.querySelector('.chip').textContent.trim()===d.dataset.answer; d.classList.add(ok?'ok':'no'); if(ok) good++;
          else{ const f=document.createElement('span'); f.className='fix'; f.textContent='→ '+d.dataset.answer; d.parentNode.appendChild(f);} });
        mark(null); chips.forEach(x=>x.disabled=true);
        finish(good===drops.length, good===drops.length?'':good+' of '+drops.length+' right.'); });
      resets[i]=()=>{ unlock(); chips.forEach(x=>x.disabled=false);
        drops.forEach(d=>{ const c=d.querySelector('.chip'); if(c) bank.appendChild(c); d.classList.remove('full','over'); });
        order.forEach(x=>bank.appendChild(x)); mark(null); };
    }
  });

  /* score slide */
  const sc=document.getElementById('fq-score'); if(!sc) return;
  const of=document.getElementById('fq-of'); if(of) of.textContent=qs.length;
  const tot=document.getElementById('fq-total'), msg=document.getElementById('fq-msg'),
        grid=document.getElementById('fq-grid'), rev=document.getElementById('fq-review');
  const topicStart=name=>slides.findIndex(s=>s.dataset.sec===name);
  function score(){
    const right=state.filter(x=>x===true).length, open=state.filter(x=>x===null).length;
    tot.textContent=right;
    msg.textContent= open===qs.length ? 'Answer the questions, then come back here.'
      : open ? `${open} question${open>1?'s':''} still open. The score counts answered questions only.`
      : right>=Math.ceil(.85*qs.length) ? 'Excellent. You own this chapter.'
      : right>=Math.ceil(.6*qs.length) ? 'Good work. Revisit the topics below, then try again.'
      : 'A second pass will help. Start with the topics below.';
    const kinds=[...new Set(qs.map(q=>q.dataset.kind||'Questions'))];      // grid: one cell per kind, in order of appearance
    grid.innerHTML=kinds.map((k,n)=>{
      const m=qs.map((q,j)=>[q,j]).filter(([q])=>(q.dataset.kind||'Questions')===k)
        .map(([,j])=>state[j]===true?'<span class="m-ok">✓</span>':state[j]===false?'<span class="m-no">✗</span>':'<span class="m-skip">·</span>').join(' ');
      return `<div class="fq-cell"><b>${n+1} · ${k}</b><span class="marks">${m}</span></div>`; }).join('');
    const miss=[...new Set(qs.filter((q,j)=>state[j]===false).map(q=>q.dataset.topic))];
    rev.innerHTML=miss.length?'<span class="soft">Revisit:</span> ':'';
    miss.forEach(t=>{ const b=document.createElement('button'); b.className='k-btn'; b.textContent=t;
      b.addEventListener('click',()=>{ const k=topicStart(t); if(k>=0) go(k); }); rev.appendChild(b); });
  }
  sc.addEventListener('slideenter',score); score();
  document.getElementById('fq-retry').addEventListener('click',()=>{
    resets.forEach(r=>r&&r()); score(); go(slides.indexOf(qs[0].closest('.slide'))); });
})();
