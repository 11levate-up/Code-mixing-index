"""
lid_model.py
--------------
IndicLID (AI4Bharat) ka wrapper — dictionary lookup ki jagah ab 
trained model use karta hai jo naye/unseen words par bhi kaam karta hai.

Model: IndicLID (FTN + FTR + BERT ensemble)
Paper: Madhani et al., "Bhasha-Abhijnaanam", ACL 2023

NOTE: Project ka scope Hindi-English hai. IndicLID 22 languages train hai,
isliye isolated short words kabhi closely-related language 
(jaise Maithili) predict kar deता hai. Is scope ke andar, 
non-English kisi bhi prediction ko Hindi maana jaata hai.
"""

import sys
sys.path.append('IndicLID/Inference/ai4bharat')
from IndicLID import IndicLID

_model = IndicLID(input_threshold=0.5, roman_lid_threshold=0.6)


def detect_language(word: str) -> str:
    results = _model.batch_predict([word], 1)
    lang_code = results[0][1]

    if lang_code == 'eng_Latn':
        return 'en'
    elif lang_code == 'other':
        return 'other'
    else:
        return 'hi'


def detect_batch(words: list) -> list:
    return [{"word": w, "lang": detect_language(w)} for w in words]
