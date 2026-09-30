# Code-Mixing Index (CMI) Calculator + Dataset Curator

A research-oriented toolkit for measuring code-mixing and curating Hindi-English code-switched language datasets.

## Problem
Low-resource code-switched languages (like Hindi-English / Hinglish) lack standardized 
tools to quantify how much a piece of text is "mixed." This makes it hard to build 
consistent datasets for training and evaluating multilingual NLP/speech models.

## Approach
This tool computes the Code-Mixing Index (CMI) of a given text/dataset, and helps curate 
and label Hindi-English code-switched samples for downstream research use.

## Features
- CMI score calculation for input text
- Dataset curation utilities for code-switched samples
- (aur jo bhi features banaoge, yahan add karte jaana)

## How to Run
```bash
git clone https://github.com/yourusername/Code-mixing-index.git
cd Code-mixing-index
pip install -r requirements.txt
python src/main.py
```

## Results
(jab test karoge apne data pe, yahan numbers/examples daalna)

## License
MIT


## Approach (Updated)
Word-level language detection now uses IndicLID (AI4Bharat) — a trained 
language identification model — instead of a fixed dictionary. This 
generalizes to unseen words, unlike a static word list.

## Known Limitations
IndicLID is trained across 22 Indian languages, so isolated short Hindi 
words sometimes get misclassified as closely related languages (e.g. 
Maithili), since single words give limited context. This project 
constrains predictions to its Hindi-English bilingual scope: any 
non-English prediction is treated as Hindi.
