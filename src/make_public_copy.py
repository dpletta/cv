# -*- coding: utf-8 -*-
"""Write the public copy of the CV from the private master Word file.

Usage:  python3 src/make_public_copy.py private/CV_DPletta_<date>.docx

Writes CV_DPletta_<date>.docx at the repository root with the phone number
and the Trainees and Mentoring section removed; everything else is left
exactly as it is in the master. Requires python-docx.
"""
import os
import re
import sys

import docx
from docx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OMIT_SECTIONS = {'TRAINEES AND MENTORING'}
PHONE = re.compile(r'\s*\|?\s*\+?1?\s*\(\d{3}\)\s*\d{3}-\d{4}')


def text(el):
    return ''.join(t.text or '' for t in el.iter(qn('w:t')))


def is_heading(el):
    t = text(el).strip()
    return el.tag == qn('w:p') and t.isupper() and len(t) > 3


src = sys.argv[1]
out = os.path.join(ROOT, os.path.basename(src))
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

d.save(out)
print(f'wrote {out} ({removed} paragraphs removed)')
