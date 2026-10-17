/* topic bar — replaces the dots: one rounded block per topic, width = its slide count;
   only the current topic is marked (no progress inside a topic). Click a block to jump to its first slide. */
(function(){
  const bar=document.getElementById('secbar'), nameEl=document.getElementById('secname'); if(!bar) return;
  const secs=[];
  slides.forEach((s,k)=>{ if(s.dataset.sec||!secs.length) secs.push({name:s.dataset.sec||'',from:k,to:k}); else secs[secs.length-1].to=k; });
  secs.forEach(sec=>{
    const b=document.createElement('button'); b.className='sec'; b.style.setProperty('--n',sec.to-sec.from+1);
    const t=document.createElement('span'); t.textContent=sec.name; b.appendChild(t);
    b.setAttribute('aria-label',sec.name); b.addEventListener('click',()=>go(sec.from));
    bar.appendChild(b); sec.el=b;
  });
  function mark(){
    secs.forEach(sec=>{
      const on=idx>=sec.from&&idx<=sec.to;
      sec.el.classList.toggle('now',on); sec.el.classList.toggle('done',idx>sec.to);
      if(on){ sec.el.setAttribute('aria-current','step'); if(nameEl) nameEl.textContent=sec.name; } else sec.el.removeAttribute('aria-current');
    });
  }
  slides.forEach(s=>s.addEventListener('slideenter',mark)); mark();
})();
