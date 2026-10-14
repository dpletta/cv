# -*- coding: utf-8 -*-
"""Render the CV content model as a standalone GitHub Pages document."""
import html as H
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cv_data as D

OUT = os.path.join(ROOT, 'index.html')
SITE_URL = 'https://dpletta.github.io/cv/'
DOCX_NAME = 'CV_DPletta_10-14-2026.docx'
PDF_NAME = 'CV_DPletta_10-14-2026.pdf'
PHOTO = 'assets/headshot.jpg'

TOKEN = re.compile(r'(\*\*.+?\*\*|\*.+?\*)')


def fmt(text):
    """Escape, then apply **bold** / *italic* markup."""
    out = []
    for tok in TOKEN.split(text):
        if not tok:
            continue
        if tok.startswith('**') and tok.endswith('**'):
            out.append('<strong>' + H.escape(tok[2:-2]) + '</strong>')
        elif tok.startswith('*') and tok.endswith('*'):
            out.append('<em>' + H.escape(tok[1:-1]) + '</em>')
        else:
            out.append(H.escape(tok))
    return ''.join(out)


def linkify_ids(ids):
    """Turn doi:/PMID:/PMCID: tokens into links."""
    if not ids:
        return ''
    s = H.escape(ids)
    s = re.sub(r'doi:(10\.\S+?)(?=[.,]?(?:\s|$))',
               r'<a href="https://doi.org/\1">doi:\1</a>', s)
    s = re.sub(r'PMID:\s*(\d+)',
               r'PMID: <a href="https://pubmed.ncbi.nlm.nih.gov/\1/">\1</a>', s)
    s = re.sub(r'PMCID:\s*(PMC\d+)',
               r'PMCID: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/\1/">\1</a>', s)
    return f'<span class="ids">{s}</span>'


def pub_text(a, t, j, c):
    parts = [a, t]
    if j:
        # Italicise the journal name but not its trailing punctuation.
        parts.append(f"*{j[:-1]}*{j[-1]}" if j[-1] in '.,' else f"*{j}*")
    if c:
        parts.append(c)
    return ' '.join(x for x in parts if x)


B = []
w = B.append

SECTIONS = []


def section(title, sid, short=None):
    SECTIONS.append((short or title, sid))
    w(f'<section id="{sid}"><h2>{H.escape(title)}</h2>')


def endsection():
    w('</section>')


def sub(title):
    w(f'<h3>{H.escape(title)}</h3>')


def row(left, right='', lclass='org'):
    r = f'<span class="date">{fmt(right)}</span>' if right else ''
    w(f'<div class="row"><span class="{lclass}">{fmt(left)}</span>{r}</div>')


# ------------------------------------------------------------------ build ---
section('Education', 'education')
_open = False
for e in D.EDUCATION:
    if e['org']:
        if _open:
            w('</div>')
        w('<div class="entry">')
        _open = True
        row(e['org'], e['loc'])
    row(e['role'], e['date'], 'role')
    for _s in e['sub']:
        w(f'<div class="sub">{fmt(_s)}</div>')
if _open:
    w('</div>')
endsection()

section('Academic Positions', 'positions', 'Positions')
for org, loc, role, date, unit in D.POSITIONS:
    w('<div class="entry">')
    row(org, loc)
    row(role, date, 'role')
    w(f'<div class="sub">{fmt(unit)}</div>')
    w('</div>')
endsection()

section('Extramural Research Support', 'grants', 'Grants')
for _tier_name, _tier in [('Awarded', D.GRANTS_AWARDED),
                          ('Under Review', D.GRANTS_UNDER_REVIEW),
                          ('In Preparation', D.GRANTS_IN_PREP)]:
    if not _tier:
        continue
    sub(_tier_name)
    for g in _tier:
        w('<div class="grant">')
        _date = (f'<span class="date">{fmt(g["date"])}</span>'
                 if g.get('date') else '')
        w(f'<div class="row grant-title"><span class="org">{fmt(g["title"])}</span>'
          f'{_date}</div>')
        w('<dl class="fields">')
        for label, value in list(g['fields']) + [('Aims', g['aims'])]:
            w(f'<dt>{H.escape(label)}</dt><dd>{fmt(value)}</dd>')
        w('</dl></div>')
endsection()

section('Scholarships & Fellowships', 'fellowships', 'Fellowships')
for org, loc, role, date, subs in D.FELLOWSHIPS:
    w('<div class="entry">')
    row(org, loc)
    row(role, date, 'role')
    for s in subs:
        w(f'<div class="sub">{fmt(s)}</div>')
    w('</div>')
endsection()

section('Honors & Recognition', 'honors', 'Honors')
for title, date, details, org, loc in D.HONORS:
    w('<div class="entry">')
    row(title, date)
    for s in details:
        w(f'<div class="sub">{fmt(s)}</div>')
    row(org, loc, 'sub')
    w('</div>')
endsection()

section('Publications', 'publications')
for title, items in [
    ('Peer-Reviewed Journal Articles — Published', D.PUBLISHED),
    ('Peer-Reviewed Journal Articles — Under Review', D.UNDER_REVIEW),
    ('Manuscripts in Preparation', D.IN_PREPARATION),
]:
    if not items:
        continue
    sub(title)
    w('<ol class="refs">')
    for a, t, j, c, ids in items:
        w(f'<li>{fmt(pub_text(a, t, j, c))} {linkify_ids(ids)}</li>')
    w('</ol>')
endsection()

section('Scientific Presentations', 'presentations', 'Presentations')
for title, items in [('Oral Presentations', D.ORAL),
                     ('Round Tables & Symposia', D.ROUNDTABLES),
                     ('Poster Presentations', D.POSTERS)]:
    sub(title)
    w('<ol class="refs">')
    for s in items:
        w(f'<li>{fmt(s)}</li>')
    w('</ol>')
endsection()

section('Teaching Experience', 'teaching', 'Teaching')
sub('Courses & Instructional Appointments')
for org, loc, role, date, subs in D.TEACHING:
    w('<div class="entry">')
    row(org, loc)
    row(role, date, 'role')
    for s in subs:
        w(f'<div class="sub">{fmt(s)}</div>')
    w('</div>')
sub('Invited Presentations & Lectures')
w('<ol class="refs">')
for s in D.INVITED_TEACHING:
    w(f'<li>{fmt(s)}</li>')
w('</ol>')
endsection()

section('Local, National, and International Service', 'service', 'Service')
for heading, loc, line, date, org in D.SERVICE:
    w('<div class="entry">')
    row(heading, loc)
    row(line, date, 'role')
    if org:
        w(f'<div class="sub">{fmt(org)}</div>')
    w('</div>')
endsection()

section('Editorial Activities', 'editorial', 'Editorial')
sub('Ad Hoc Peer Reviewer')
w('<ul class="journals">')
for j in D.AD_HOC_JOURNALS:
    w(f'<li>{H.escape(j)}</li>')
w('</ul>')
endsection()

section('Professional Societies & Organizations', 'societies', 'Societies')
for name, date in D.SOCIETIES:
    w('<div class="entry">')
    row(name, date, 'role')
    w('</div>')
endsection()

section('Scientific Trainings', 'trainings', 'Trainings')
for title, loc, host, date in D.TRAININGS:
    w('<div class="entry">')
    row(title, loc)
    row(host, date, 'role')
    w('</div>')
endsection()

nav = '\n'.join(
    f'<a href="#{sid}">{H.escape(t)}</a>' for t, sid in SECTIONS)

CSS = """
:root{color-scheme:light;
  --bg:#fbfaf8; --panel:#ffffff; --ink:#15161a; --muted:#5d6069;
  --faint:#8a8d96; --rule:#dedbd4; --accent:#5a2d2d; --accent-soft:#f2ece6;
  --shadow:0 1px 2px rgba(20,20,25,.05), 0 8px 28px rgba(20,20,25,.05);
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,"Times New Roman",serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){color-scheme:dark;
    --bg:#111214; --panel:#17181b; --ink:#e9e7e3; --muted:#a4a7b0;
    --faint:#7e828c; --rule:#2c2e33; --accent:#d9a3a3; --accent-soft:#232022;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 28px rgba(0,0,0,.35);
  }
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:var(--serif);font-size:16px;line-height:1.5;
  -webkit-text-size-adjust:100%;}
a{color:var(--accent);text-underline-offset:2px}
a:hover{text-decoration:none}

.masthead{background:var(--panel);border-bottom:1px solid var(--rule)}
.wrap{max-width:54rem;margin:0 auto;padding:0 1.5rem}
.masthead .wrap{padding-top:2.6rem;padding-bottom:2rem;display:grid;
  grid-template-columns:auto 1fr;gap:2rem;align-items:center}
.portrait{display:block;width:152px;height:152px;border-radius:50%;
  object-fit:cover;padding:4px;background:var(--bg);
  border:1px solid var(--rule);box-shadow:var(--shadow)}
h1{font-size:1.72rem;line-height:1.2;letter-spacing:.05em;
   margin:0 0 .55rem;font-weight:600}
.contact{font-size:.86rem;color:var(--muted);margin:.12rem 0;
  font-family:var(--sans);letter-spacing:.005em}
.contact a{color:inherit}
.updated{font-size:.76rem;color:var(--faint);font-family:var(--sans);
  margin:.75rem 0 0;letter-spacing:.03em;text-transform:uppercase}
.downloads{margin-top:1.05rem;display:flex;gap:.55rem;flex-wrap:wrap}
.downloads a{display:inline-block;font-family:var(--sans);font-size:.79rem;
  letter-spacing:.05em;text-transform:uppercase;text-decoration:none;
  padding:.5rem .95rem;border:1px solid var(--rule);border-radius:2px;
  color:var(--muted);background:var(--bg);transition:.15s}
.downloads a:hover{border-color:var(--accent);color:var(--accent);
  background:var(--accent-soft)}

nav.toc{position:sticky;top:0;z-index:10;background:var(--panel);
  border-bottom:1px solid var(--rule)}
nav.toc .wrap{max-width:72rem;display:flex;gap:.1rem;flex-wrap:wrap;justify-content:center;
  padding-top:.4rem;padding-bottom:.4rem}
@media (max-width:640px){nav.toc .wrap{flex-wrap:nowrap;overflow-x:auto;
  justify-content:flex-start;scrollbar-width:thin}}
nav.toc a{font-family:var(--sans);font-size:.735rem;letter-spacing:.035em;
  white-space:nowrap;text-decoration:none;color:var(--muted);
  padding:.32rem .5rem;border-radius:3px}
nav.toc a:hover{color:var(--accent);background:var(--accent-soft)}

main{padding:1.6rem 0 4rem}
section{margin-bottom:.6rem;scroll-margin-top:5.6rem}
h2{font-size:.94rem;letter-spacing:.13em;text-transform:uppercase;font-weight:700;
   margin:2.1rem 0 .1rem;padding-bottom:.34rem;border-bottom:1.5px solid var(--ink)}
h3{font-size:.9rem;font-style:italic;font-weight:600;color:var(--ink);
   margin:1.15rem 0 .35rem}

.entry{margin:.62rem 0}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:1.2rem}
.org{font-weight:600}
.role{}
.date{font-family:var(--sans);font-size:.79rem;color:var(--muted);
  white-space:nowrap;flex-shrink:0;letter-spacing:.02em}
.sub{font-size:.87rem;color:var(--muted);margin-left:1rem}

.grant{margin:1.1rem 0}
.grant-title{margin-bottom:.5rem}
dl.fields{display:grid;grid-template-columns:max-content 1fr;
  gap:.3rem .95rem;margin:0;padding:.7rem .9rem;border-left:2px solid var(--rule);
  background:var(--panel);border-radius:0 3px 3px 0}
dl.fields dt{font-family:var(--sans);font-size:.7rem;letter-spacing:.07em;
  text-transform:uppercase;color:var(--faint);padding-top:.18rem}
dl.fields dd{margin:0;font-size:.93rem}

ol.refs{list-style:decimal;padding-left:2.1rem;margin:.3rem 0}
ol.refs>li{margin:.44rem 0;padding-left:.25rem;font-size:.93rem;line-height:1.46}
ol.refs>li::marker{font-family:var(--sans);font-size:.78rem;color:var(--faint)}
.ids{font-family:var(--sans);font-size:.74rem;color:var(--faint);
  display:inline-block;margin-top:.1rem}
.ids a{color:var(--faint);text-decoration:underline;text-decoration-color:var(--rule)}
.ids a:hover{color:var(--accent)}

ul.journals{columns:2;column-gap:2rem;list-style:none;padding-left:0;
  margin:.3rem 0;font-size:.9rem}
ul.journals>li{margin:.16rem 0;break-inside:avoid}

footer{border-top:1px solid var(--rule);margin-top:2.5rem;padding-top:1.1rem;
  font-family:var(--sans);font-size:.75rem;color:var(--faint);text-align:center}

@media (max-width:640px){
  body{font-size:15px}
  .wrap{padding:0 1rem}
  .masthead .wrap{grid-template-columns:1fr;justify-items:center;
    text-align:center;gap:1.1rem;padding-top:2rem;padding-bottom:1.6rem}
  .portrait{width:120px;height:120px}
  .downloads{justify-content:center}
  h1{font-size:1.4rem}
  .row{flex-direction:column;gap:.05rem}
  .date{font-size:.75rem}
  dl.fields{grid-template-columns:1fr;gap:.05rem .5rem;padding:.6rem .7rem}
  dl.fields dd{margin-bottom:.4rem}
  ul.journals{columns:1}
  ol.refs{padding-left:1.5rem}
  section{scroll-margin-top:3.2rem}
}

@media print{
  :root{--bg:#fff;--panel:#fff;--ink:#000;--muted:#333;--faint:#555;
        --rule:#bbb;--accent:#000;--accent-soft:#fff}
  nav.toc,.downloads,.portrait{display:none!important}
  body{font-size:10.5pt;background:#fff}
  .wrap{max-width:none;padding:0}
  .masthead{border-bottom:none}
  .masthead .wrap{display:block;padding-top:0;text-align:center}
  h1{font-size:16pt}
  h2{font-size:11pt;margin-top:14pt;break-after:avoid}
  h3{font-size:10.5pt;break-after:avoid}
  dl.fields{background:#fff}
  a{color:#000;text-decoration:none}
  .entry,.grant,ol.refs>li{break-inside:avoid}
  @page{margin:.75in}
}
"""

TITLE = 'David R. Pletta, PhD, MPH — Curriculum Vitae'

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="Curriculum vitae of David R. Pletta, PhD, MPH — quantitative epidemiologist, Department of Epidemiology, University of Michigan School of Public Health.">
<meta name="author" content="David R. Pletta">
<link rel="canonical" href="{SITE_URL}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="Quantitative epidemiologist, University of Michigan School of Public Health.">
<meta property="og:type" content="profile">
<meta property="og:url" content="{SITE_URL}">
<meta property="og:image" content="{SITE_URL}{PHOTO}">
<meta property="og:image:alt" content="Headshot of David R. Pletta">
<meta name="twitter:card" content="summary">
<link rel="icon" href="data:,">
<style>{CSS}</style>
</head>
<body>

<header class="masthead">
  <div class="wrap">
    <img class="portrait" src="{PHOTO}" width="152" height="152" alt="Headshot of David R. Pletta">
    <div class="ident">
      <h1>DAVID R. PLETTA, PhD, MPH</h1>
      <p class="contact">Department of Epidemiology, University of Michigan School of Public Health, Ann Arbor, MI</p>
      <p class="contact"><a href="mailto:dpletta@umich.edu">dpletta@umich.edu</a></p>
      <p class="contact">ORCID: <a href="{D.ORCID_URL}">{D.ORCID_URL}</a></p>
      <div class="downloads">
        <a href="{PDF_NAME}" download>Download PDF</a>
        <a href="{DOCX_NAME}" download>Download DOCX</a>
        <a href="#" onclick="window.print();return false;">Print</a>
      </div>
      <p class="updated">Last updated {D.LAST_UPDATED}</p>
    </div>
  </div>
</header>

<nav class="toc" aria-label="Sections"><div class="wrap">
{nav}
</div></nav>

<main><div class="wrap">
{chr(10).join(B)}
<footer>
  <p>David R. Pletta, PhD, MPH &nbsp;·&nbsp; Last updated {D.LAST_UPDATED}<br>
  <a href="{PDF_NAME}">PDF</a> &nbsp;·&nbsp; <a href="{DOCX_NAME}">DOCX</a> &nbsp;·&nbsp;
  <a href="https://github.com/dpletta/cv">Source</a></p>
</footer>
</div></main>

</body>
</html>
"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(doc)
print('wrote', OUT, len(doc), 'bytes')
