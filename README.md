# AnkiMedRef — Medical Quick Reference for Anki

An Anki add-on (v8.26) that shows a quick-reference tooltip when you hover over a medical term on a card during review. It covers abbreviations, drugs and drug classes, lab ranges, diseases, microbiology, scoring systems, anatomy, ECG, genetics, radiology, pathology, signs and symptoms, OB/GYN, primary care, and more.

Lookups are tried in this order:

1. Built-in dictionaries (`data/*.py`): instant and offline.
2. A local MeSH/UMLS database (`med_terms.db`) with 1.2M+ terms: about 5 ms and offline.
3. Optional online sources: RxNorm, openFDA, MedlinePlus, Wikipedia, and UMLS/OMIM if you add an API key.

## Installation

1. **Download the repo.** On GitHub, click **Code → Download ZIP** and extract it, or run:
   ```bash
   git clone https://github.com/vishaljjohn/AnkiMedRef.git
   ```
2. **Unzip the database.** It's stored compressed because GitHub doesn't allow files over 100 MB. Inside the folder, run:
   ```bash
   gunzip -k med_terms.db.gz
   ```
   That gives you `med_terms.db` (about 458 MB). On Windows, use 7-Zip, or any tool that opens `.gz` files. The add-on still works without the database, but it only has the built-in dictionaries and online lookups.
3. **Find your add-ons folder.** In Anki, go to **Tools → Add-ons → View Files**.
4. **Copy the add-on in.** Copy the whole folder into the add-ons folder, and give it a simple name such as `AnkiMedRef`. These files need to be directly inside it:
   ```
   AnkiMedRef/
   ├── __init__.py
   ├── formatters.py
   ├── config.json
   ├── meta.json
   ├── med_terms.db
   └── data/
   ```
   You can delete `med_terms.db.gz` once you've unzipped it.
5. **Restart Anki.**

## Usage

- Start reviewing and hover over a medical term. A tooltip pops up after a short delay, which you can change.
- To change settings, go to **Tools → Medical Quick Reference Settings…**. You can turn each source on or off, change the hover delay, the tooltip size and theme, and the search engine, and add an optional UMLS or OMIM API key.

## API keys (optional)

None are needed. The UMLS and OMIM fields in `config.json` are empty by default. If you want those lookups, enter your own keys in the Settings dialog. Don't commit your keys to this repo.

## Reference guide

`Medical_Quick_Reference_Guide.docx` gives an overview of the add-on and what it covers.

## Disclaimer

This add-on is a study aid for medical education. It is not a substitute for clinical judgment or authoritative references, and it must not be used for patient care decisions.
