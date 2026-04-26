print("PII module loaded")
import re

def mask_dob(text):
    dob_pattern = re.compile(
        r'\b('
        r'\d{1,2}(?:st|nd|rd|th)?\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}'
        r'|\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'
        r'|\d{4}-\d{1,2}-\d{1,2}'
        r'|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{1,2},\s\d{4}'
        r')\b',
        re.IGNORECASE
    )
    return dob_pattern.sub("[DOB]", text)


def mask_pii(text):
    if not text:
        return text

    text = re.sub(r"\S+@\S+", "[EMAIL]", text)
    text = re.sub(r"\+?\d{10,15}", "[PHONE]", text)
    text = mask_dob(text)

    return text