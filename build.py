#!/usr/bin/env python3
"""
Générateur du profil GitHub Exoliance.

Modifie uniquement le bloc CONFIG ci-dessous, puis lance :
    python3 build.py
Le script régénère README.md et tous les visuels dans assets/ (versions sombre + claire).
Aucune dépendance externe : Python 3.8+ suffit.
"""
from pathlib import Path
from xml.sax.saxutils import escape

# ═══════════════════════════════════════════════════════════════════════
#  CONFIG — tout ce qui est personnalisable est ici
# ═══════════════════════════════════════════════════════════════════════
CONFIG = {
    "username": "Elilou14",
    "repo": "elilou14",                   # nom exact du repo de profil               # ton identifiant GitHub (le repo doit s'appeler pareil)
    "brand": "EXOLIANCE",
    "tagline": "Automatisations & outils sur mesure",
    "location": "Île-de-France",
    "audiences": ["clubs sportifs", "établissements", "associations", "PME & équipes terrain"],
    "email": "",                          # ← ton email pro (vide = bouton masqué)
    "website": "",                        # ← URL de ton site (vide = bouton masqué)
    "linkedin": "",                       # ← URL LinkedIn (ou "" pour masquer le bouton)
    "stack": ["Python", "Node.js", "n8n", "Make", "Zapier", "Google Apps Script",
              "Airtable", "Notion API", "Supabase", "Webhooks", "REST API",
              "Stripe", "Google Workspace", "Brevo"],
    # Réalisations facultatives : ("Nom", "Ce que ça fait", "lien ou ''")
    "projects": [],
    "snake": True,                        # animation du graphe de contributions (via GitHub Actions)
}

PALETTES = {
    "dark": dict(bg="#0A0E14", bg2="#111821", border="#222C38", grid="#16202B",
                 text="#E8EEF5", muted="#7C8896", accent="#B8FF3C", accent_ink="#0A0E14",
                 accent2="#3CE3FF", glow_op="0.22"),
    "light": dict(bg="#FFFFFF", bg2="#F4F7FA", border="#D5DDE5", grid="#EEF2F6",
                  text="#141A21", muted="#5A6674", accent="#3E8C00", accent_ink="#FFFFFF",
                  accent2="#0083B8", glow_op="0.14"),
}

SANS = "Inter, 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'SF Mono', ui-monospace, Menlo, Consolas, 'DejaVu Sans Mono', 'Liberation Mono', monospace"

OUT = Path(__file__).parent
ASSETS = OUT / "assets"


def e(s):
    return escape(str(s), {'"': "&quot;"})


def base_style(p, extra=""):
    return f"""<style>
  .sans{{font-family:{SANS};}}
  .mono{{font-family:{MONO};}}
  .t{{fill:{p['text']};}} .m{{fill:{p['muted']};}} .a{{fill:{p['accent']};}} .a2{{fill:{p['accent2']};}}
  {extra}
  @media (prefers-reduced-motion: reduce){{ *{{animation:none!important;}} }}
</style>"""


def svg_open(w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{e(title)}"><title>{e(title)}</title>')


def card(p, w, h, rid):
    return f"""<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="20" fill="{p['bg']}" stroke="{p['border']}"/>
<defs>
  <pattern id="grid{rid}" width="28" height="28" patternUnits="userSpaceOnUse">
    <path d="M28 0H0V28" fill="none" stroke="{p['grid']}" stroke-width="1"/>
  </pattern>
  <radialGradient id="gmask{rid}" cx="50%" cy="50%" r="65%">
    <stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/>
  </radialGradient>
  <mask id="fade{rid}"><rect width="{w}" height="{h}" fill="url(#gmask{rid})"/></mask>
  <clipPath id="cardclip{rid}"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="20"/></clipPath>
</defs>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="20" fill="url(#grid{rid})" mask="url(#fade{rid})"/>"""


# ─────────────────────────────────────────────────────────────── HERO ──
def hero(p):
    W, H = 1000, 460
    c = CONFIG
    words = c["audiences"]
    n = len(words)
    cycle = 3 * n
    out = [svg_open(W, H, f"{c['brand']} — {c['tagline']}")]
    pct = 100 / n
    out.append(base_style(p, f"""
  .word{{opacity:0; animation:rot {cycle}s infinite both; transform-box:fill-box;}}
  @keyframes rot{{
    0%{{opacity:0; transform:translateY(14px);}}
    {pct*0.12:.2f}%{{opacity:1; transform:translateY(0);}}
    {pct*0.85:.2f}%{{opacity:1; transform:translateY(0);}}
    {pct*0.98:.2f}%{{opacity:0; transform:translateY(-14px);}}
    100%{{opacity:0; transform:translateY(-14px);}}
  }}
  .log{{opacity:0; animation:log 8s infinite both;}}
  @keyframes log{{ 0%{{opacity:0;}} 4%{{opacity:1;}} 80%{{opacity:1;}} 90%{{opacity:0;}} 100%{{opacity:0;}} }}
  .blink{{animation:blink 1s steps(1) infinite;}}
  @keyframes blink{{ 50%{{opacity:0;}} }}
"""))
    out.append(card(p, W, H, "h"))
    out.append(f"""<defs>
  <radialGradient id="glow"><stop offset="0" stop-color="{p['accent']}" stop-opacity="{p['glow_op']}"/><stop offset="1" stop-color="{p['accent']}" stop-opacity="0"/></radialGradient>
  <radialGradient id="glow2"><stop offset="0" stop-color="{p['accent2']}" stop-opacity="{p['glow_op']}"/><stop offset="1" stop-color="{p['accent2']}" stop-opacity="0"/></radialGradient>
  <linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="-400" y1="0" x2="0" y2="0">
    <stop offset="0" stop-color="{p['text']}"/>
    <stop offset="0.45" stop-color="{p['text']}"/>
    <stop offset="0.5" stop-color="{p['accent']}"/>
    <stop offset="0.55" stop-color="{p['text']}"/>
    <stop offset="1" stop-color="{p['text']}"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1400 0;1400 0" keyTimes="0;0.55;1" dur="7s" begin="1.4s" repeatCount="indefinite"/>
  </linearGradient>
  <clipPath id="reveal"><rect x="40" y="110" width="0" height="120">
    <animate attributeName="width" values="0;620" keyTimes="0;1" dur="1.1s" begin="0.25s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
  </rect></clipPath>
  <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p['accent']}" stop-opacity="0"/><stop offset="1" stop-color="{p['accent']}" stop-opacity="0.07"/></linearGradient>
  <clipPath id="wordwin"><rect x="56" y="318" width="520" height="40"/></clipPath>
</defs>
<g clip-path="url(#cardcliph)">
  <circle cx="250" cy="200" r="300" fill="url(#glow)">
    <animate attributeName="cx" values="220;360;220" dur="16s" repeatCount="indefinite"/>
  </circle>
  <circle cx="800" cy="260" r="240" fill="url(#glow2)">
    <animate attributeName="cy" values="300;180;300" dur="12s" repeatCount="indefinite"/>
  </circle>
  <rect x="0" y="0" width="{W}" height="90" fill="url(#scan)">
    <animate attributeName="y" values="-100;{H+10}" dur="8s" repeatCount="indefinite"/>
  </rect>
</g>""")

    # Statut
    out.append(f"""<g transform="translate(56 50)">
  <rect width="334" height="30" rx="15" fill="{p['bg2']}" stroke="{p['border']}"/>
  <circle cx="18" cy="15" r="4" fill="{p['accent']}"/>
  <circle cx="18" cy="15" r="4" fill="none" stroke="{p['accent']}" stroke-width="2">
    <animate attributeName="r" values="4;12" dur="1.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.9;0" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <text x="34" y="19.5" class="mono t" font-size="11.5" letter-spacing="1.4">DISPONIBLE POUR DE NOUVEAUX PROJETS</text>
</g>
<text x="58" y="124" class="mono m" font-size="13" letter-spacing="0.5">// studio d'automatisation — {e(c['location'])}</text>""")

    # Titre
    out.append(f"""<g clip-path="url(#reveal)">
  <text x="52" y="210" class="sans" font-size="88" font-weight="800" fill="url(#shine)"
        textLength="540" lengthAdjust="spacingAndGlyphs">{e(c['brand'])}</text>
</g>
<rect x="58" y="230" width="0" height="5" rx="2.5" fill="{p['accent']}">
  <animate attributeName="width" values="0;72" dur="0.6s" begin="1.1s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.2 0.8 0.2 1"/>
</rect>
<text x="58" y="280" class="sans t" font-size="27" font-weight="650">{e(c['tagline'])}</text>
<text x="58" y="314" class="mono m" font-size="14">conçus pour les</text>
<g clip-path="url(#wordwin)">""")
    for i, w in enumerate(words):
        out.append(f'<text x="58" y="348" class="sans a word" font-size="27" font-weight="750" '
                   f'style="animation-delay:{3*i}s">{e(w)}</text>')
    out.append("</g>")

    # Ligne de log
    logs = ["inscription reçue", "facture générée", "planning à jour", "SMS envoyé"]
    out.append(f'<text x="58" y="410" class="mono m" font-size="12.5">run#2048 ›</text>')
    x = 146
    for i, l in enumerate(logs):
        out.append(f'<text x="{x}" y="410" class="mono log" font-size="12.5" style="animation-delay:{0.6*i}s">'
                   f'<tspan class="a">✓</tspan> <tspan class="t">{e(l)}</tspan></text>')
        x += int((len(l) + 4) * 7.6)
    out.append(f'<rect x="{x}" y="399" width="8" height="14" fill="{p["accent"]}" class="blink"/>')

    # Diagramme de workflow
    hub = (790, 232)
    R = 40
    ins = [("Formulaire", 150), ("Paiement", 232), ("Email", 314)]
    outs = [("CRM", 150), ("Planning", 232), ("Facture", 314)]
    ix, iw = 584, 110
    ox, ow = 878, 94
    dur = 2.6
    g = ['<g>']
    paths = []
    for k, (lab, y) in enumerate(ins):
        x1, x2 = ix + iw, hub[0] - R
        m = (x2 - x1) * 0.65
        d = f"M{x1} {y} C {x1+m:.0f} {y}, {x2-m:.0f} {hub[1]}, {x2} {hub[1]}"
        paths.append(("in", d, k * 0.85))
    for k, (lab, y) in enumerate(outs):
        x1, x2 = hub[0] + R, ox
        m = (x2 - x1) * 0.65
        d = f"M{x1} {hub[1]} C {x1+m:.0f} {hub[1]}, {x2-m:.0f} {y}, {x2} {y}"
        paths.append(("out", d, dur + k * 0.85))
    for kind, d, _ in paths:
        g.append(f'<path d="{d}" fill="none" stroke="{p["border"]}" stroke-width="2"/>')
        g.append(f'<path d="{d}" fill="none" stroke="{p["accent2"] if kind=="in" else p["accent"]}" '
                 f'stroke-width="2" stroke-dasharray="3 9" opacity="0.7">'
                 f'<animate attributeName="stroke-dashoffset" values="24;0" dur="0.9s" repeatCount="indefinite"/></path>')
    for kind, d, begin in paths:
        col = p["accent2"] if kind == "in" else p["accent"]
        g.append(f'<circle r="4.5" fill="{col}" opacity="0"><animateMotion dur="1.3s" begin="{begin:.2f}s" '
                 f'repeatCount="indefinite" path="{d}" calcMode="spline" keyTimes="0;1" keySplines="0.4 0 0.2 1"/>'
                 f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.85;1" dur="1.3s" begin="{begin:.2f}s" repeatCount="indefinite"/></circle>')

    def node(x, y, w, lab, flash_begin=None, col=None):
        s = [f'<g transform="translate({x} {y-19})">',
             f'<rect width="{w}" height="38" rx="10" fill="{p["bg2"]}" stroke="{p["border"]}" stroke-width="1.5">']
        if flash_begin is not None:
            s.append(f'<animate attributeName="stroke" values="{p["border"]};{col};{p["border"]}" '
                     f'keyTimes="0;0.15;1" dur="1.3s" begin="{flash_begin:.2f}s" repeatCount="indefinite"/>')
        s.append('</rect>')
        s.append(f'<circle cx="14" cy="19" r="3.5" fill="{col or p["muted"]}"/>')
        s.append(f'<text x="26" y="23.5" class="mono t" font-size="12.5">{e(lab)}</text></g>')
        return "".join(s)

    for k, (lab, y) in enumerate(ins):
        g.append(node(ix, y, iw, lab, k * 0.85, p["accent2"]))
    for k, (lab, y) in enumerate(outs):
        g.append(node(ox, y, ow, lab, dur + k * 0.85 + 1.15, p["accent"]))

    cx, cy = hub
    g.append(f"""<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{p['accent']}" stroke-width="1.5" opacity="0">
  <animate attributeName="r" values="{R};{R+36}" dur="2.6s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0.6;0" dur="2.6s" repeatCount="indefinite"/>
</circle>
<circle cx="{cx}" cy="{cy}" r="{R+12}" fill="none" stroke="{p['accent']}" stroke-width="1.5" stroke-dasharray="2 10" opacity="0.8">
  <animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy};360 {cx} {cy}" dur="14s" repeatCount="indefinite"/>
</circle>
<circle cx="{cx}" cy="{cy}" r="{R}" fill="{p['bg2']}" stroke="{p['accent']}" stroke-width="2"/>
<g transform="translate({cx} {cy})">
  <g>
    <animateTransform attributeName="transform" type="rotate" values="0;-360" dur="9s" repeatCount="indefinite"/>
    <path d="M0 -19 L4.5 -8 L16.5 -9.5 L9.5 0 L16.5 9.5 L4.5 8 L0 19 L-4.5 8 L-16.5 9.5 L-9.5 0 L-16.5 -9.5 L-4.5 -8Z"
          fill="none" stroke="{p['accent']}" stroke-width="2" stroke-linejoin="round"/>
    <circle r="6" fill="{p['accent']}"/>
  </g>
</g>
<text x="{cx}" y="{cy+78}" text-anchor="middle" class="mono m" font-size="11.5" letter-spacing="1">exoliance.engine</text>
<text x="{ix}" y="106" class="mono m" font-size="11" letter-spacing="1.5">ENTRÉES</text>
<text x="{ox}" y="106" class="mono m" font-size="11" letter-spacing="1.5">SORTIES</text>""")
    g.append("</g>")
    out += g
    out.append("</svg>")
    return "\n".join(out)


# ─────────────────────────────────────────────────────────── TERMINAL ──
def terminal(p):
    W = 1000
    fs, lh, cw = 15, 27, 9.03
    x0, y0 = 40, 88
    lines = [
        ("cmd", [("whoami", "t")]),
        ("out", [("→ ", "a"), ("Exoliance", "t"), (" — studio d'automatisation & d'outils sur mesure", "m")]),
        ("gap", None),
        ("cmd", [("exoliance services ", "t"), ("--list", "a2")]),
        ("out", [("  ▸ ", "a"), ("Automatisation de process".ljust(30), "t"), ("inscriptions, relances, facturation", "m")]),
        ("out", [("  ▸ ", "a"), ("Outils internes sur mesure".ljust(30), "t"), ("dashboards, back-offices, portails", "m")]),
        ("out", [("  ▸ ", "a"), ("Intégrations & API".ljust(30), "t"), ("CRM, paiement, agenda, emails", "m")]),
        ("gap", None),
        ("cmd", [("exoliance pour ", "t"), ("--qui", "a2")]),
        ("out", [("  " + " · ".join(CONFIG["audiences"]), "m")]),
        ("gap", None),
        ("cmd", [("exoliance contact", "t")]),
        ("out", [("  ✓ ", "a"), ("Un process qui vous fait perdre du temps ? Parlons-en ↓", "t")]),
        ("cmd", []),
    ]
    rows = sum(1 for k, _ in lines if k != "gap") + sum(0.5 for k, _ in lines if k == "gap")
    H = int(y0 + rows * lh + 24)

    # Timeline
    t = 0.6
    events = []  # (start, end, kind, row_y, nchars)
    cursor = []  # (time, x, y)
    y = y0
    for kind, segs in lines:
        if kind == "gap":
            y += lh * 0.5
            continue
        if kind == "cmd":
            n = sum(len(s) for s, _ in segs)
            px = x0 + 2 * cw
            cursor.append((t, px, y))
            t += 0.25
            start = t
            per = 0.038
            for k in range(1, n + 1):
                cursor.append((start + k * per, px + k * cw, y))
            t = start + n * per
            events.append((start, t, "cmd", y, n, per))
            t += 0.25
        else:
            t += 0.12
            events.append((t, t, "out", y, 0, 0))
            t += 0.08
        y += lh
    hold = 4.0
    D = round(t + hold, 2)

    def kt(v):
        return f"{min(max(v / D, 0), 1):.4f}"

    out = [svg_open(W, H, "Terminal : présentation d'Exoliance")]
    out.append(base_style(p, ".cur{animation:blink 1s steps(1) infinite;} @keyframes blink{50%{opacity:0;}}"))
    out.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" fill="{p["bg"]}" stroke="{p["border"]}"/>')
    out.append(f'<path d="M1 44 V17 a16 16 0 0 1 16 -16 H{W-17} a16 16 0 0 1 16 16 V44 Z" fill="{p["bg2"]}"/>')
    out.append(f'<line x1="1" y1="44" x2="{W-1}" y2="44" stroke="{p["border"]}"/>')
    for i, col in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
        out.append(f'<circle cx="{26+i*20}" cy="22.5" r="6" fill="{col}"/>')
    out.append(f'<text x="{W/2}" y="27" text-anchor="middle" class="mono m" font-size="12.5">exoliance@studio: ~ — zsh</text>')

    out.append("<defs>")
    ei = 0
    for (start, end, kind, ry, n, per) in events:
        if kind == "cmd":
            vals = ["0"]
            kts = ["0"]
            vals.append("0"); kts.append(kt(start))
            for k in range(1, n + 1):
                vals.append(f"{(2 + k) * cw + 2:.1f}")
                kts.append(kt(start + k * per))
            vals.append("0"); kts.append(kt(D - 0.25))
        else:
            vals = ["0", "0", str(W), "0"]
            kts = ["0", kt(start), kt(start + 0.01), kt(D - 0.25)]
        # garantir keyTimes strictement croissants
        clean_v, clean_k, last = [], [], -1
        for v, k in zip(vals, kts):
            if float(k) <= last:
                continue
            clean_v.append(v); clean_k.append(k); last = float(k)
        out.append(f'<clipPath id="l{ei}"><rect x="{x0-4}" y="{ry-19}" height="{lh}" width="0">'
                   f'<animate attributeName="width" dur="{D}s" repeatCount="indefinite" calcMode="discrete" '
                   f'values="{";".join(clean_v)}" keyTimes="{";".join(clean_k)}"/></rect></clipPath>')
        ei += 1
    out.append("</defs>")

    y = y0
    ei = 0
    for kind, segs in lines:
        if kind == "gap":
            y += lh * 0.5
            continue
        if kind == "cmd":
            spans = "".join(f'<tspan class="{c}">{e(s)}</tspan>' for s, c in segs)
            out.append(f'<text x="{x0}" y="{y}" class="mono" font-size="{fs}" xml:space="preserve" '
                       f'clip-path="url(#l{ei})"><tspan class="a" font-weight="700">❯ </tspan>{spans}</text>')
        else:
            spans = "".join(f'<tspan class="{c}">{e(s)}</tspan>' for s, c in segs)
            out.append(f'<text x="{x0}" y="{y}" class="mono" font-size="{fs}" xml:space="preserve" '
                       f'clip-path="url(#l{ei})">{spans}</text>')
        ei += 1
        y += lh

    # curseur qui suit la frappe
    cursor.append((D - 0.25, x0 + 2 * cw, y0))
    xs, ys, ks, last = [], [], [], -1
    for (tt, cx, cy) in cursor:
        k = float(kt(tt))
        if k <= last:
            continue
        xs.append(f"{cx + 1:.1f}"); ys.append(f"{cy - 14}"); ks.append(f"{k:.4f}"); last = k
    if ks[0] != "0.0000":
        xs.insert(0, f"{x0 + 2*cw + 1:.1f}"); ys.insert(0, f"{y0-14}"); ks.insert(0, "0")
    out.append(f'<rect class="cur" x="{xs[0]}" y="{ys[0]}" width="9" height="18" fill="{p["accent"]}">'
               f'<animate attributeName="x" dur="{D}s" repeatCount="indefinite" calcMode="discrete" values="{";".join(xs)}" keyTimes="{";".join(ks)}"/>'
               f'<animate attributeName="y" dur="{D}s" repeatCount="indefinite" calcMode="discrete" values="{";".join(ys)}" keyTimes="{";".join(ks)}"/>'
               f'</rect>')
    out.append("</svg>")
    return "\n".join(out)


# ─────────────────────────────────────────────────────────── MÉTHODE ──
def process(p):
    W, H = 1000, 280
    steps = [
        ("01", "Audit", ["On repère vos tâches", "répétitives et chronophages"]),
        ("02", "Prototype", ["Une première version", "concrète, testée avec vous"]),
        ("03", "Déploiement", ["Branché sur vos outils", "existants, sans tout changer"]),
        ("04", "Suivi", ["Ajustements, formation", "et maintenance"]),
    ]
    xs = [125, 375, 625, 875]
    cy = 132
    D = 10
    out = [svg_open(W, H, "Méthode : audit, prototype, déploiement, suivi")]
    out.append(base_style(p))
    out.append(card(p, W, H, "p"))
    out.append(f'<text x="44" y="52" class="mono m" font-size="12.5" letter-spacing="1">// MÉTHODE</text>')
    out.append(f'<text x="44" y="82" class="sans t" font-size="24" font-weight="750">Comment on travaille</text>')
    out.append(f'<line x1="{xs[0]}" y1="{cy}" x2="{xs[-1]}" y2="{cy}" stroke="{p["border"]}" stroke-width="3" stroke-linecap="round"/>')
    seg = 0.8 / (len(xs) - 1)
    vals = [str(xs[0])]
    kts = ["0"]
    for i in range(1, len(xs)):
        vals += [str(xs[i - 1]), str(xs[i])]
        kts += [f"{0.05 + seg*(i-1) + 0.06:.3f}", f"{0.05 + seg*i:.3f}"]
    vals += [str(xs[-1]), str(xs[0])]
    kts += ["0.96", "1"]
    out.append(f'<line x1="{xs[0]}" y1="{cy}" x2="{xs[0]}" y2="{cy}" stroke="{p["accent"]}" stroke-width="3" stroke-linecap="round">'
               f'<animate attributeName="x2" dur="{D}s" repeatCount="indefinite" values="{";".join(vals)}" keyTimes="{";".join(kts)}"/></line>')
    out.append(f'<circle r="5" fill="{p["accent"]}" cy="{cy}" cx="{xs[0]}">'
               f'<animate attributeName="cx" dur="{D}s" repeatCount="indefinite" values="{";".join(vals)}" keyTimes="{";".join(kts)}"/></circle>')
    for i, (num, title, desc) in enumerate(steps):
        x = xs[i]
        on = 0.05 + seg * i if i else 0.03
        k_on = f"{on:.3f}"
        out.append(f'<circle cx="{x}" cy="{cy}" r="22" fill="{p["bg2"]}" stroke="{p["border"]}" stroke-width="2">'
                   f'<animate attributeName="stroke" dur="{D}s" repeatCount="indefinite" calcMode="discrete" '
                   f'values="{p["border"]};{p["accent"]};{p["border"]}" keyTimes="0;{k_on};0.96"/></circle>')
        out.append(f'<circle cx="{x}" cy="{cy}" r="22" fill="none" stroke="{p["accent"]}" stroke-width="2" opacity="0">'
                   f'<animate attributeName="r" dur="{D}s" repeatCount="indefinite" values="22;22;40;40" keyTimes="0;{k_on};{on+0.08:.3f};1"/>'
                   f'<animate attributeName="opacity" dur="{D}s" repeatCount="indefinite" values="0;0.8;0;0" keyTimes="0;{k_on};{on+0.08:.3f};1"/></circle>')
        out.append(f'<text x="{x}" y="{cy+5}" text-anchor="middle" class="mono" font-size="13" font-weight="700" fill="{p["muted"]}">'
                   f'<animate attributeName="fill" dur="{D}s" repeatCount="indefinite" calcMode="discrete" '
                   f'values="{p["muted"]};{p["accent"]};{p["muted"]}" keyTimes="0;{k_on};0.96"/>{num}</text>')
        out.append(f'<text x="{x}" y="{cy+58}" text-anchor="middle" class="sans t" font-size="17" font-weight="700">{e(title)}</text>')
        for j, dl in enumerate(desc):
            out.append(f'<text x="{x}" y="{cy+84+j*19}" text-anchor="middle" class="sans m" font-size="13.5">{e(dl)}</text>')
    out.append("</svg>")
    return "\n".join(out)


# ──────────────────────────────────────────────────────────── STACK ──
def stack(p):
    W, H = 1000, 96
    cw = 7.8
    chips, x = [], 0
    for s in CONFIG["stack"]:
        w = int(len(s) * cw + 40)
        chips.append((x, w, s))
        x += w + 12
    setw = x
    out = [svg_open(W, H, "Outils maîtrisés : " + ", ".join(CONFIG["stack"]))]
    out.append(base_style(p))
    out.append(f"""<defs>
  <linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="#000"/><stop offset="0.08" stop-color="#fff"/><stop offset="0.92" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
  <mask id="edgem"><rect width="{W}" height="{H}" fill="url(#edge)"/></mask>
</defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="{p['bg']}" stroke="{p['border']}"/>
<text x="28" y="30" class="mono m" font-size="11.5" letter-spacing="1.5">// STACK &amp; OUTILS</text>
<g mask="url(#edgem)"><g>
  <animateTransform attributeName="transform" type="translate" values="0 0;-{setw} 0" dur="{max(18, setw/45):.1f}s" repeatCount="indefinite"/>""")
    for rep in range(3):
        for (cx, w, s) in chips:
            X = cx + rep * setw + 20
            out.append(f'<g transform="translate({X} 44)"><rect width="{w}" height="32" rx="16" fill="{p["bg2"]}" stroke="{p["border"]}"/>'
                       f'<circle cx="16" cy="16" r="3.5" fill="{p["accent"]}"/>'
                       f'<text x="28" y="20.5" class="mono t" font-size="13">{e(s)}</text></g>')
    out.append("</g></g></svg>")
    return "\n".join(out)


# ─────────────────────────────────────────────────────────── BOUTONS ──
def button(p, label, primary, icon):
    W, H = 210, 52
    fill = p["accent"] if primary else p["bg2"]
    ink = p["accent_ink"] if primary else p["text"]
    stroke = p["accent"] if primary else p["border"]
    return f"""{svg_open(W, H, label)}
{base_style(p)}
<defs>
  <linearGradient id="sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="{0.45 if primary else 0.12}"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <clipPath id="bc"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14"/></clipPath>
</defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>
<g clip-path="url(#bc)"><rect x="-80" y="0" width="70" height="{H}" fill="url(#sh)" transform="skewX(-20)">
  <animate attributeName="x" values="-90;-90;{W+40}" keyTimes="0;0.6;1" dur="4s" repeatCount="indefinite"/>
</rect></g>
<text x="{W/2}" y="31.5" text-anchor="middle" class="sans" font-size="15" font-weight="700" fill="{ink}">{icon}  {e(label)}</text>
</svg>"""


# ─────────────────────────────────────────────────────────── FOOTER ──
def footer(p):
    W, H = 1000, 170
    out = [svg_open(W, H, "Automatisons votre prochain process")]
    out.append(base_style(p))
    wave = lambda amp, yb: (f"M0 {yb} " + " ".join(
        f"Q {125 + 250*i} {yb - amp if i % 2 == 0 else yb + amp} {250 + 250*i} {yb}" for i in range(8))
        + f" V{H} H0 Z")
    out.append(f"""<defs><clipPath id="fc"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="20"/></clipPath></defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="20" fill="{p['bg']}" stroke="{p['border']}"/>
<g clip-path="url(#fc)">
  <path d="{wave(14, 128)}" fill="{p['accent2']}" opacity="0.12"><animateTransform attributeName="transform" type="translate" values="0 0;-500 0" dur="9s" repeatCount="indefinite"/></path>
  <path d="{wave(10, 140)}" fill="{p['accent']}" opacity="0.18"><animateTransform attributeName="transform" type="translate" values="-500 0;0 0" dur="6s" repeatCount="indefinite"/></path>
</g>
<text x="{W/2}" y="64" text-anchor="middle" class="sans t" font-size="25" font-weight="750">Votre prochain process automatisé commence ici.</text>
<text x="{W/2}" y="96" text-anchor="middle" class="mono m" font-size="13.5">moins de saisie · moins d'oublis · plus de temps pour l'essentiel</text>
</svg>""")
    return "\n".join(out)


# ─────────────────────────────────────────────────────────── README ──
def pic(name, alt, width=None, link=None):
    u = "./assets"
    w = f' width="{width}"' if width else ' width="100%"'
    img = (f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="{u}/{name}-dark.svg">\n'
           f'  <source media="(prefers-color-scheme: light)" srcset="{u}/{name}-light.svg">\n'
           f'  <img alt="{e(alt)}" src="{u}/{name}-dark.svg"{w}>\n</picture>')
    return f'<a href="{link}">{img}</a>' if link else img


def readme():
    c = CONFIG
    u = c["username"]
    parts = ['<!-- Généré par build.py — modifie CONFIG puis relance `python3 build.py` -->',
             '<div align="center">', "", pic("hero", f"{c['brand']} — {c['tagline']}"), "", ""]
    btns = []
    if c["email"]:
        btns.append(f'<a href="mailto:{c["email"]}">{pic("btn-contact", "Me contacter", 210)}</a>')
    if c["website"]:
        btns.append(f'<a href="{c["website"]}">{pic("btn-site", "Voir le site", 210)}</a>')
    if c["linkedin"]:
        btns.append(f'<a href="{c["linkedin"]}">{pic("btn-linkedin", "LinkedIn", 210)}</a>')
    if btns:
        parts.append('<p align="center">\n' + "\n&nbsp;\n".join(btns) + "\n</p>")
    parts += ["", "<br><br>", "", pic("terminal", "Présentation : services d'automatisation et outils sur mesure"),
              "", "<br><br>", "", pic("process", "Méthode : audit, prototype, déploiement, suivi"),
              "", "<br>", "", pic("stack", "Stack & outils"), ""]
    if c["projects"]:
        parts += ["<br>", "", "### Réalisations", "", "</div>", "",
                  "| Projet | Ce que ça fait |", "|---|---|"]
        for name, what, link in c["projects"]:
            n = f"[{name}]({link})" if link else name
            parts.append(f"| **{n}** | {what} |")
        parts += ["", '<div align="center">', ""]
    if c["snake"]:
        base = f"https://raw.githubusercontent.com/{u}/{c.get('repo', u)}/output"
        parts += ["<br>", "",
                  '<picture>',
                  f'  <source media="(prefers-color-scheme: dark)" srcset="{base}/github-snake-dark.svg">',
                  f'  <source media="(prefers-color-scheme: light)" srcset="{base}/github-snake.svg">',
                  f'  <img alt="Animation des contributions" src="{base}/github-snake.svg" width="100%">',
                  '</picture>', ""]
    parts += ["<br>", "", pic("footer", "Votre prochain process automatisé commence ici", link=f"mailto:{c['email']}" if c["email"] else None),
              "", "</div>", ""]
    return "\n".join(parts)


SNAKE_YML = """name: Animation des contributions

on:
  schedule:
    - cron: "17 */12 * * *"   # deux fois par jour
  workflow_dispatch:           # bouton "Run workflow" pour lancer à la main
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Générer le serpent
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-snake.svg?color_snake=#3E8C00&color_dots=#ebedf0,#c9f0a6,#8fd65a,#5aae25,#3E8C00
            dist/github-snake-dark.svg?palette=github-dark&color_snake=#B8FF3C&color_dots=#161b22,#2b3d12,#4f7a16,#82c21f,#B8FF3C

      - name: Publier sur la branche output
        uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""


def main():
    ASSETS.mkdir(exist_ok=True)
    for mode, p in PALETTES.items():
        files = {
            "hero": hero(p), "terminal": terminal(p), "process": process(p),
            "stack": stack(p), "footer": footer(p),
            "btn-contact": button(p, "Me contacter", True, "✉"),
            "btn-site": button(p, "Voir le site", False, "↗"),
            "btn-linkedin": button(p, "LinkedIn", False, "in"),
        }
        for name, svg in files.items():
            (ASSETS / f"{name}-{mode}.svg").write_text(svg, encoding="utf-8")
    (OUT / "README.md").write_text(readme(), encoding="utf-8")
    wf = OUT / ".github" / "workflows"
    wf.mkdir(parents=True, exist_ok=True)
    (wf / "snake.yml").write_text(SNAKE_YML, encoding="utf-8")
    print("✓ README.md, assets/ et .github/workflows/snake.yml générés")


if __name__ == "__main__":
    main()
