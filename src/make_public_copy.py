# -*- coding: utf-8 -*-
"""Write the public copy of the CV from the private master Word file.

Usage:  python3 src/make_public_copy.py private/CV_DPletta_<date>.docx [OUT]

Writes CV_DPletta_<date>.docx at the repository root (or OUT) with the phone
number and the Trainees and Mentoring section removed; everything else is
left exactly as it is in the master. Requires python-docx.

Fails closed. The written copy is read back part by part, the way Word sees
it: paragraph text (including Word's special characters such as
non-breaking hyphens), every attribute value (alt text, link targets,
metadata) and any non-XML part as raw text. If any phone number or any text
unique to the omitted section is still there, or the master has tracked
changes, comments or embedded objects that cannot be checked, no public
copy is written and the script exits non-zero.
"""
import io
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

import docx
from docx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OMIT_SECTIONS = {'TRAINEES AND MENTORING'}
# The phone number as written in the contact line, with its " | " separator.
PHONE = re.compile(r'\s*\|?\s*\+?1?\s*\(\d{3}\)\s*\d{3}-\d{4}')
# Anything that could be read as a North American phone number.
PHONE_ANY = re.compile(r'(?<!\d)(?:\+?\s*1[\s().\-/]*)?\(?\d{3}\)?[\s().\-/]{0,3}'
                       r'\d{3}[\s.\-/]{0,3}\d{4}(?!\d)')

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
REL = '{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'
TEXT = {W + 't', W + 'delText', W + 'instrText', W + 'delInstrText'}
CHARS = {W + 'noBreakHyphen': '-', W + 'softHyphen': '', W + 'tab': '\t',
         W + 'br': '\n', W + 'cr': '\n'}
BLOCKS = {W + 'p', W + 'tc'}
# Text in revisions and comments is not redacted, so masters with any are refused.
REVISIONS = {W + n for n in ('ins', 'del', 'moveFrom', 'moveTo', 'comment',
                             'commentReference', 'commentRangeStart')}
# Embedded documents and objects cannot be checked from the outside.
EMBEDDED = re.compile(r'/(oleObject|package|aFChunk|subDocument)$')


class Refused(Exception):
    pass


def norm(s):
    return re.sub(r'[^0-9a-z]', '', s.lower())


def digits(s):
    return re.sub(r'\D', '', s)


def text(el):
    return ''.join(t.text or '' for t in el.iter(qn('w:t')))


def is_heading(el):
    t = text(el).strip()
    return el.tag == qn('w:p') and t.isupper() and len(t) > 3


def readable_text(path):
    """Yield (part, text, is_id) for everything in the file a reader could see.

    is_id marks attribute values that are bare integers: Word's internal IDs,
    which can look like phone numbers but are never shown to a reader.
    """
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if len(names) != len(set(names)):
            raise Refused(f'{path} has duplicate parts')
        for name in names:
            data = z.read(name)
            try:
                events = list(ET.iterparse(io.BytesIO(data), events=('start', 'end')))
            except ET.ParseError:
                yield name, data.decode('latin-1'), False
                continue
            paras = []  # paragraphs can nest (text boxes), so keep a stack
            for event, el in events:
                if event == 'start':
                    if el.tag in REVISIONS:
                        raise Refused(f'{name} has tracked changes or comments; '
                                      'accept or reject them in Word and rerun.')
                    if el.tag == REL and EMBEDDED.search(el.get('Type', '')):
                        raise Refused(f'{name} links an embedded object or document, '
                                      'which cannot be checked; remove it in Word and rerun.')
                    for value in el.attrib.values():
                        yield name, value, value.lstrip('-').isdigit()
                    if el.tag in BLOCKS:
                        paras.append([])
                    continue
                if el.tag in TEXT or el.tag in CHARS:
                    piece = el.text or '' if el.tag in TEXT else CHARS[el.tag]
                    if paras:
                        paras[-1].append(piece)
                    else:
                        yield name, piece, False
                elif el.tag in BLOCKS:
                    yield name, ''.join(paras.pop()), False
                elif not el.tag.startswith(W):
                    for s in (el.text, el.tail):
                        if s and s.strip():
                            yield name, s, False


def remove_phone(p):
    """Delete the phone number from paragraph p, even if Word split it across runs."""
    ts = list(p.iter(qn('w:t')))
    m = PHONE.search(''.join(t.text or '' for t in ts))
    if not m:
        return False
    start, end = m.span()
    pos = 0
    for t in ts:
        s = t.text or ''
        a, b = max(start - pos, 0), min(end - pos, len(s))
        if a < b:
            t.text = s[:a] + s[b:]
        pos += len(s)
    return True


def make_public_copy(src, out, tmp):
    # Every phone number in the master, by its digits, so any format is caught.
    numbers = {digits(m)[-10:] for _, s, is_id in readable_text(src) if not is_id
               for m in PHONE_ANY.findall(s)}

    d = docx.Document(src)
    body = d.element.body
    for p in body.iter(qn('w:p')):
        while remove_phone(p):
            pass

    # Drop each omitted section, from its heading up to the next heading.
    dropping = False
    removed = []
    for el in list(body.iterchildren()):
        if is_heading(el):
            dropping = text(el).strip() in OMIT_SECTIONS
        if dropping:
            body.remove(el)
            removed.append(el)
    if not removed:
        raise Refused(f'none of the sections {sorted(OMIT_SECTIONS)} were found in the master; '
                      'if a heading was renamed, update OMIT_SECTIONS here and in check_sync.py.')

    # Text unique to the omitted section: each line up to its first comma or
    # period (a trainee's name, the heading, the note), unless it also appears
    # in the part of the CV that stays (an institution name, for example).
    kept = norm(text(body))
    unique = set()
    for el in removed:
        key = norm(re.split(r'[,.]', text(el), maxsplit=1)[0])
        if len(key) >= 8 and key not in kept:
            unique.add(key)

    d.save(tmp)
    for name, s, is_id in readable_text(tmp):
        if is_id:
            if any(n in s for n in numbers):
                raise Refused(f'{name} still contains a phone number; remove it in Word and rerun.')
            continue
        for line in s.splitlines():
            if PHONE_ANY.search(line) or any(n in digits(line) for n in numbers):
                raise Refused(f'{name} still contains a phone number; remove it in Word and rerun.')
            hit = next((k for k in unique if k in norm(line)), None)
            if hit:
                raise Refused(f'{name} still contains text from an omitted section '
                              f'({line.strip()[:60]!r}); remove it in Word and rerun.')
    os.replace(tmp, out)
    return len(removed)


src = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, os.path.basename(src))
tmp = out + '.tmp'
try:
    removed = make_public_copy(src, out, tmp)
except Refused as e:
    if os.path.exists(tmp):
        os.remove(tmp)
    sys.exit(f'make_public_copy: {e}\nNo public copy was written.')
print(f'wrote {out} ({removed} paragraphs removed; verified that no phone number '
      f'or omitted-section text remains in any part)')
