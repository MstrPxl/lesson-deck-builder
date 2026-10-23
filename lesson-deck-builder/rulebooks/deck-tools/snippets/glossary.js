/* deck glossary (rulebook T5b) — the first use of each glossary term on every other slide
   becomes an anchored gloss (components §24). The definitions live once, on the glossary slide. */
(function(){
  const dl=document.getElementById('glossary'); if(!dl) return;
  const esc=s=>s.replace(/[.*+?^${}()|[\]\\\/]/g,'\\$&');
  const terms=[...dl.querySelectorAll('dt')].map(dt=>{
    const name=dt.textContent.trim(), dd=dt.nextElementSibling;
    const forms=[name,...(dt.dataset.forms||'').split(',').map(x=>x.trim()).filter(Boolean)];
    const caps=/^[A-Z0-9\/]+$/.test(name);                       // acronyms match case-sensitively
    return {name, def:dd?dd.textContent.trim():'', re:new RegExp('(?<![\\w/])('+forms.map(esc).join('|')+')(?![\\w/])', caps?'':'i')};
  });
  const SKIP='dfn,h1,h2,h3,.lf,button,.gl-w,.formal,.fbox .k,.lk-t,.er,.mb-mem,textarea,svg,template,code,pre,kbd,.tag,.badge,.hint,.verdict';
  let n=0;
  document.querySelectorAll('section.slide').forEach(sl=>{
    if(sl.contains(dl)||sl.querySelector('.fq')) return;   // no glossary cards inside a quiz (questions-rulebook.md §6): they could give answers away
    const defined=new Set([...sl.querySelectorAll('dfn')].map(d=>d.textContent.trim().toLowerCase()));
    terms.forEach(t=>{
      if(defined.has(t.name.toLowerCase())) return;               // the defining slide keeps its visible definition
      const w=document.createTreeWalker(sl,NodeFilter.SHOW_TEXT,{acceptNode:x=>x.parentElement.closest(SKIP)?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT});
      for(let node=w.nextNode();node;node=w.nextNode()){
        const m=t.re.exec(node.nodeValue); if(!m) continue;
        const r=document.createRange(); r.setStart(node,m.index); r.setEnd(node,m.index+m[0].length);
        const id='--gx'+(++n), g=document.createElement('span'); g.className='gl-w';
        g.innerHTML=`<span class="gl-t" tabindex="0" style="anchor-name:${id}"></span><span class="gl-card" role="tooltip" style="position-anchor:${id}"><b></b></span>`;
        g.firstChild.textContent=m[0]; g.querySelector('b').textContent=t.name; g.lastChild.append(t.def);
        r.deleteContents(); r.insertNode(g); break;
      }
    });
  });
})();
