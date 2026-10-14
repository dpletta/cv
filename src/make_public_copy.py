# -*- coding: utf-8 -*-
"""Write the public copy of the CV from the private master Word file.

Usage:  python3 src/make_public_copy.py private/CV_DPletta_<date>.docx

Writes CV_DPletta_<date>.docx at the repository root with the phone number
and the Trainees and Mentoring section removed; everything else is left
exactly as it is in the master. Requires python-docx.

Fails closed: the copy is checked part by part after it is written, and if
anything that should have been removed is still there (or the master has
tracked changes or comments, whose text is not redacted), no public file is
written and the script exits non-zero.
"""
import html
import os
import re
import sys
import zipfile

import docx
from docx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OMIT_SECTIONS = {'TRAINEES AND MENTORING'}
# The phone number as written in the contact line, with its " | " separator.
PHONE = re.compile(r'\s*\|?\s*\+?1?\s*\(\d{3}\)\s*\d{3}-\d{4}')
# Any North American phone number, however it is formatted.
PHONE_ANY = re.compile(r'(?<!\d)(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]\d{4}(?!\d)')


def text(el):
    return ''.join(t.text or '' for t in el.iter(qn('w:t')))


def is_heading(el):
    t = text(el).strip()
    return el.tag == qn('w:p') and t.isupper() and len(t) > 3


def part_texts(path):
    """Yield (part name, plain text) for every XML part, one line per paragraph."""
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if name.endswith(('.xml', '.rels')):
                raw = z.read(name).decode('utf-8', 'replace')
                raw = re.sub(r'</w:p>|</w:tr>', '\n', raw)
                yield name, html.unescape(re.sub(r'<[^>]+>', '', raw)), raw


def digits(s):
    return re.sub(r'\D', '', s)


def fail(msg, tmp=None):
    if tmp and os.path.exists(tmp):
        os.remove(tmp)
    sys.exit(f'make_public_copy: {msg}\nNo public copy was written.')


src = sys.argv[1]
out = os.path.join(ROOT, os.path.basename(src))
tmp = out + '.tmp'

# Text inside tracked changes and comments is not redacted below, so refuse
# masters that have any; accept or reject them in Word first.
for name, _, raw in part_texts(src):
    if re.search(r'<w:(del|ins|moveFrom|moveTo)\b', raw) or name == 'word/comments.xml':
        fail(f'{name} has tracked changes or comments; resolve them in Word and rerun.')

# Every phone number in the master, by its digits, so other formats are caught.
secret_numbers = {digits(m)[-10:] for _, t, _ in part_texts(src)
                  for m in PHONE_ANY.findall(t)}

d = docx.Document(src)

# Drop the phone number, and the " | " that separated it from the email.
for t in d.element.body.iter(qn('w:t')):
    if t.text and PHONE.search(t.text):
        t.text = PHONE.sub('', t.text)

# Drop each omitted section, from its heading up to the next heading.
body = d.element.body
dropping = False
removed = 0
for el in list(body.iterchildren()):
    if is_heading(el):
        dropping = text(el).strip() in OMIT_SECTIONS
    if dropping:
        body.remove(el)
        removed += 1
if not removed:
    fail(f'none of the sections {sorted(OMIT_SECTIONS)} were found in the master; '
         'if a heading was renamed, update OMIT_SECTIONS here and in check_sync.py.')

d.save(tmp)

# Verify the saved copy, every part (headers, footers, footnotes, metadata).
for name, t, _ in part_texts(tmp):
    for line in t.splitlines():
        if any(number in digits(line) for number in secret_numbers):
            fail(f'a phone number from the master is still in {name}; '
                 'remove it in Word and rerun.', tmp)
        if PHONE_ANY.search(line):
            fail(f'{name} still contains a phone number: {line.strip()[:80]!r}', tmp)
        if line.strip() in OMIT_SECTIONS:
            fail(f'{name} still contains the heading {line.strip()!r}', tmp)

os.replace(tmp, out)
print(f'wrote {out} ({removed} paragraphs removed; verified no phone number '
      f'or omitted section remains in any part)')
