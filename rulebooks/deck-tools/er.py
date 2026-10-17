"""er.py - ER diagrams for lesson decks (deck-tools 1.5): shapes in SVG, every label an HTML pin (no text in SVG).
A spec: dict(vw, vh, width, nodes=[(id, kind, x, y, label, opts)], edges=[(a, b, style, [labels])], pins=[...]).
kinds: ent, weak, rel, idrel, att, key, pkey, multi, derived, box (plain small rect, e.g. E1), pt (invisible point: a line end)
edge style: '-' single, '=' double (total participation), '.' dashed
edge label: (text, end 'a'|'b', along, side, cls)  along = units from that end's boundary, side = perpendicular offset
"""
import math, html

F = 14.6  # label font size in viewBox units (er-pin)

def tw(s, f=F):
    w = 0
    for ch in s:
        if ch.isupper(): w += .66
        elif ch.islower(): w += .52
        elif ch.isdigit(): w += .56
        elif ch == '_': w += .5
        elif ch == ' ': w += .27
        else: w += .4
    return w * f

def size(kind, label, o):
    if kind == 'pt': return ('rect', 0.01, 0.01)
    ls = label.split('\n'); t = max(tw(l) for l in ls); ex = 8.5 * (len(ls) - 1)
    if kind in ('ent', 'weak', 'box'):
        w = o.get('w', t + 20); h = o.get('h', 26 + 2 * ex)
        if kind == 'weak': w += 8; h += 8
        return ('rect', w / 2, h / 2)
    if kind in ('rel', 'idrel'):
        hh = o.get('hh', 22 + 2 * ex); hw = o.get('hw', (t / 2 + 4) / (1 - (8 + ex) / hh))
        if kind == 'idrel': hw += 7; hh += 5
        return ('dia', hw, hh)
    ry = o.get('ry', 13 + 1.4 * ex); rx = o.get('rx', (t / 2 + 3) / (1 - ((8 + ex) / ry) ** 2) ** .5)
    if kind == 'multi': rx += 3; ry += 3
    return ('ell', rx, ry)

def clip(n, tx, ty):
    shape, a, b = n['shape']; dx, dy = tx - n['x'], ty - n['y']
    if dx == 0 and dy == 0: return n['x'], n['y']
    if shape == 'rect': t = min(a / abs(dx) if dx else 1e9, b / abs(dy) if dy else 1e9)
    elif shape == 'dia': t = 1 / (abs(dx) / a + abs(dy) / b)
    else: t = 1 / math.sqrt((dx / a) ** 2 + (dy / b) ** 2)
    return n['x'] + dx * t, n['y'] + dy * t

def f1(v): return f'{v:.1f}'.rstrip('0').rstrip('.')

def shape_svg(n):
    k = n['kind']; x, y = n['x'], n['y']; _, a, b = n['shape']; out = []
    if k == 'pt': return ''
    if k in ('ent', 'box'):
        out.append(f'<rect class="s fe" x="{f1(x-a)}" y="{f1(y-b)}" width="{f1(2*a)}" height="{f1(2*b)}" rx="2"/>')
    elif k == 'weak':
        out.append(f'<rect class="s fe" x="{f1(x-a)}" y="{f1(y-b)}" width="{f1(2*a)}" height="{f1(2*b)}" rx="2"/>')
        out.append(f'<rect class="s t" x="{f1(x-a+4)}" y="{f1(y-b+4)}" width="{f1(2*a-8)}" height="{f1(2*b-8)}" rx="1"/>')
    elif k in ('rel', 'idrel'):
        out.append(f'<path class="s fe" d="M{f1(x-a)} {f1(y)} L{f1(x)} {f1(y-b)} L{f1(x+a)} {f1(y)} L{f1(x)} {f1(y+b)} Z"/>')
        if k == 'idrel':
            a2, b2 = a - 7, b - 5
            out.append(f'<path class="s t" d="M{f1(x-a2)} {f1(y)} L{f1(x)} {f1(y-b2)} L{f1(x+a2)} {f1(y)} L{f1(x)} {f1(y+b2)} Z"/>')
    else:
        cls = 's t fo' + (' dash' if k == 'derived' else '')
        out.append(f'<ellipse class="{cls}" cx="{f1(x)}" cy="{f1(y)}" rx="{f1(a)}" ry="{f1(b)}"/>')
        if k == 'multi':
            out.append(f'<ellipse class="s t" cx="{f1(x)}" cy="{f1(y)}" rx="{f1(a-3.5)}" ry="{f1(b-3.5)}"/>')
    return ''.join(out)

def line_svg(p, q, style):
    (x1, y1), (x2, y2) = p, q
    hot = ' hot' if style.endswith('h') else ''; style = style.rstrip('h')
    if style == '=':
        dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1; ox, oy = -dy / L * 2.2, dx / L * 2.2
        return (f'<path class="s t{hot}" d="M{f1(x1+ox)} {f1(y1+oy)} L{f1(x2+ox)} {f1(y2+oy)}"/>'
                f'<path class="s t{hot}" d="M{f1(x1-ox)} {f1(y1-oy)} L{f1(x2-ox)} {f1(y2-oy)}"/>')
    cls = 's t' + (' dash' if style == '.' else '') + hot
    return f'<path class="{cls}" d="M{f1(x1)} {f1(y1)} L{f1(x2)} {f1(y2)}"/>'

def pin(text, x, y, cls='mid', extra=''):
    return f'<span class="lf-pin er {cls}{extra}" style="--x:{f1(x)};--y:{f1(y)}">{text}</span>'

def name_html(label, kind):
    code = kind in ('ent', 'weak', 'rel', 'idrel', 'att', 'key', 'pkey', 'multi', 'derived')
    return '<br>'.join((f'<code class="rn">{html.escape(l)}</code>' if code else html.escape(l)) for l in label.split('\n'))

def build(spec):
    nodes = {}
    for nd in spec['nodes']:
        nid, kind, x, y, label = nd[:5]; o = nd[5] if len(nd) > 5 else {}
        nodes[nid] = dict(id=nid, kind=kind, x=x, y=y, label=label, o=o, shape=size(kind, label, o))
    lines, pins = [], []
    for e in spec.get('edges', []):
        a, b, style = e[:3]; labs = e[3] if len(e) > 3 else []; eo = e[4] if len(e) > 4 else {}
        A, B = nodes[a], nodes[b]
        ta = (A['x'] + eo['pa'][0], A['y'] + eo['pa'][1]) if 'pa' in eo else None
        tb = (B['x'] + eo['pb'][0], B['y'] + eo['pb'][1]) if 'pb' in eo else None
        pa = ta or clip(A, *(tb or (B['x'], B['y'])))
        pb = tb or clip(B, *(ta or (A['x'], A['y'])))
        if eo.get('hot'): style = style + 'h'
        lines.append(line_svg(pa, pb, style))
        dx, dy = pb[0] - pa[0], pb[1] - pa[1]; L = math.hypot(dx, dy) or 1; ux, uy = dx / L, dy / L
        for lab in labs:
            text, end, along, side = lab[:4]; cls = lab[4] if len(lab) > 4 else 'mid'
            if end == 'a': bx, by, sx, sy = pa[0], pa[1], ux, uy
            else: bx, by, sx, sy = pb[0], pb[1], -ux, -uy
            px, py = bx + sx * along + (-uy) * side, by + sy * along + ux * side
            pins.append(pin(text, px, py, cls))
    shapes = []
    for n in nodes.values():
        shapes.append(shape_svg(n))
        o = n['o']
        if o.get('nolabel'): continue
        extra = ''
        if n['kind'] == 'key': extra = ' k'
        if n['kind'] == 'pkey': extra = ' pk'
        if n['kind'] in ('ent', 'weak', 'rel', 'idrel', 'box'): extra += ' up'
        lx, ly = n['x'] + o.get('lx', 0), n['y'] + o.get('ly', 0)
        pins.append(pin(name_html(n['label'], n['kind']), lx, ly, 'mid', extra + (' ' + o['cls'] if o.get('cls') else '')))
    for p in spec.get('pins', []):
        text, x, y = p[:3]; cls = p[3] if len(p) > 3 else 'mid'
        pins.append(pin(text, x, y, cls))
    vw, vh = spec['vw'], spec['vh']
    width = spec.get('width', vw)
    cls = spec.get('cls', '')
    extra_svg = spec.get('svg', '')
    return (f'<div class="lf erfig {cls}" style="--vw:{vw};--vh:{vh};width:min({width}px,100%)">'
            f'<svg viewBox="0 0 {vw} {vh}" aria-hidden="true"><g filter="url(#wob)">{"".join(lines)}{extra_svg}{"".join(shapes)}</g></svg>'
            f'<div class="lf-layer">{"".join(pins)}</div></div>')
