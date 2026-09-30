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
## Results

### Example
Input: "hi BROH KESA HAI TU SALE MUJHE MILNE NAHI AYA TUUU BHAI BAHAN KE DAALE I AM BROH OF YOURS"

CMI Score: 68.4
Hindi words: 12 | English words: 5

### Dictionary-based approach (v1)
- Works well for common, pre-listed words (hai, tu, mujhe, bhai, bahan)
- Fails on unseen/slang words (e.g. "BROH", "DAALE" misclassified as English)
- Cannot generalize beyond its fixed word list

### Model-based approach (v2 — IndicLID)
Tested on isolated words:

| Word | Dictionary v1 | IndicLID v2 |
|------|---------------|-------------|
| mujhe | Hindi ✅ | Hindi ✅ |
| kaisa | Hindi ✅ | Hindi ✅ |
| hello | English ✅ | English ✅ |
| BROH | English ❌ (not real Hindi anyway) | Hindi (edge case) |

IndicLID generalizes to unseen words without needing a manually maintained 
list, at the cost of occasional confusion with closely related languages 
on short, context-free inputs (see Known Limitations).

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
