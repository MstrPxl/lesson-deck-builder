/* B4 · phone layer — wide boxes scroll sideways without turning the page; a build that lands
   below the fold scrolls into view (phones only) */
document.querySelectorAll('pre,.code,.tbl-wrap').forEach(e=>{ if(e.scrollWidth>e.clientWidth+2||matchMedia('(max-width:880px)').matches) e.setAttribute('data-capture',''); });
slides.forEach(s=>s.addEventListener('build',()=>{
  if(!s.classList.contains('active')||!matchMedia('(max-width:880px)').matches) return;
  const now=[...s.querySelectorAll('[data-build].now')].filter(e=>e.getBoundingClientRect().height>0).pop(); if(!now) return;
  const r=now.getBoundingClientRect(), nav=document.querySelector('.nav'), lim=nav?nav.getBoundingClientRect().top-8:innerHeight;
  if(r.bottom>lim||r.top<0) s.scrollBy({top:r.bottom>lim?Math.min(r.bottom-lim,r.top-60):r.top-60,behavior:'smooth'});
}));
