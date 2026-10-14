# Curriculum Vitae — David R. Pletta, PhD, MPH

Live: **https://dpletta.github.io/cv/**

Quantitative epidemiologist, Department of Epidemiology, University of Michigan
School of Public Health.

| File | Description |
| --- | --- |
| [`index.html`](index.html) | Web CV published via GitHub Pages (responsive, print-friendly, light/dark) |
| [`CV_DPletta_10-14-2026.docx`](CV_DPletta_10-14-2026.docx) | Public Word copy |
| [`CV_DPletta_10-14-2026.pdf`](CV_DPletta_10-14-2026.pdf) | Public PDF, converted from the public Word copy |
| `assets/headshot.jpg` | Web headshot (400 × 400) |
| `src/` | Web content model, page generator, public-copy and sync scripts, original headshot |
| `private/` | Full master CV and earlier versions — git-ignored, never published |

The public copies and the web page leave out the phone number and the
Trainees and Mentoring section. Both stay in the master copy in `private/`.

## How to update

The full Word document in `private/` is the master copy. The web page is
generated from `src/cv_data.py`, which mirrors it minus the omitted items.

1. Edit the master in Word and save it as
   `private/CV_DPletta_<MM-DD-YYYY>.docx`. Move the previous master into
   `private/archive/`, and delete the previous public `.docx` and `.pdf` at the
   repository root.
2. Make the same changes in `src/cv_data.py`, and set `LAST_UPDATED`. Inline
   `**bold**` and `*italic*` markup is supported in text fields.
3. Point `DOCX_NAME` and `PDF_NAME` in `src/build_html.py` at the new files.
4. Regenerate and check:

   ```bash
   uv run --with python-docx python src/make_public_copy.py private/CV_DPletta_<date>.docx
   soffice --headless --convert-to pdf CV_DPletta_<date>.docx   # public .pdf
   python3 src/build_html.py                                    # -> index.html
   uv run --with python-docx python src/check_sync.py CV_DPletta_<date>.docx
   ```

   `make_public_copy.py` reads its output back the way Word does (text, alt
   text, links and metadata in every part) and refuses to write a public copy
   if any phone number or text from the omitted section is still there, if
   the section heading isn't found, or if the master has tracked changes,
   comments or embedded objects (resolve or remove them in Word first).
   `check_sync.py` lists any text that appears in the Word file but not on the
   web page, or vice versa, and exits non-zero if the two have drifted.
   (`soffice` lives at `/Applications/LibreOffice.app/Contents/MacOS/soffice`.)
5. Commit and push to `main`; GitHub Pages republishes within a minute or two.

To replace the photo, export a square image and run
`sips -s format jpeg -s formatOptions 82 -Z 400 <photo> --out assets/headshot.jpg`.

## Conventions

- Publications and presentations are numbered.
- Every published article carries a DOI, PMID and PMCID where one exists; all
  identifiers are live links on the web page.
- Author name is bold in every reference.
