# -*- coding: utf-8 -*-
"""Check that index.html and the Word CV contain the same text.

Usage:  python3 src/check_sync.py CV_DPletta_<date>.docx

Compares letters and digits only, so formatting, punctuation, tabs and
en-dash vs hyphen differences are ignored. Lists every Word paragraph
fragment missing from the web page, and every web text node missing from
the Word file. The phone number and the Trainees and Mentoring section are
kept off the public page on purpose and are not reported. Requires
python-docx.
"""
import os
import re
import sys
from html.parser import HTMLParser

import docx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'index.html')


def norm(s):
    return re.sub(r'[^0-9a-z]', '', s.lower())


def docx_lines(path):
    d = docx.Document(path)
    for block in d.element.body.iterchildren():
        tag = block.tag.rsplit('}', 1)[-1]
        if tag == 'p':
            yield docx.text.paragraph.Paragraph(block, d).text
        elif tag == 'tbl':
            for r in docx.table.Table(block, d).rows:
                for c in r.cells:
                    yield c.text


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.chunks = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        self._skip = tag in ('style', 'script')

    def handle_endtag(self, tag):
        self._skip = False

    def handle_data(self, data):
        if data.strip() and not self._skip:
            self.chunks.append(data)


page = open(PAGE, encoding='utf-8').read()
main = page[page.index('<main>'):page.index('<footer>')]
parser = Text()
parser.feed(page)
web = norm(''.join(parser.chunks))
body = Text()
body.feed(main)

lines = [l for l in docx_lines(sys.argv[1]) if l.strip()]
word = norm(''.join(lines))
# The signature block and running header are print-only.
ignore = {'signature', 'davidrplettaphdmph'}
# Kept in the Word file but deliberately left off the public web page.
OMIT_SECTIONS = {'TRAINEES AND MENTORING'}
PHONE = re.compile(r'\s*\|?\s*\+?1?\s*\(\d{3}\)\s*\d{3}-\d{4}')

missing_web = []
skipping = False
for line in lines:
    if line.isupper():  # section heading
        skipping = line.strip() in OMIT_SECTIONS
    if skipping:
        continue
    line = PHONE.sub('', line)
    line = re.sub(r'^\d+\.\t', '', line)
    for frag in re.split(r'\t+', line):
        f = norm(frag)
        if f and f not in ignore and f not in web:
            missing_web.append(frag.strip())
missing_word = [c.strip() for c in body.chunks if norm(c) not in word]

for f in missing_web:
    print('In Word, not on web:', f[:150])
for c in missing_word:
    print('On web, not in Word:', c[:150])
print(f'{len(missing_web)} Word fragments missing from web; '
      f'{len(missing_word)} web fragments missing from Word.')
sys.exit(1 if missing_web or missing_word else 0)
