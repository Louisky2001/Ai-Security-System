import re

def detect_prompt_injection(text):
    patterns = [
        r"ignore previous instructions",
        r"bypass security",
        r"act as",
        r"reveal system prompt"
    ]

    for p in patterns:
        if re.search(p, text.lower()):
            return True
    return False

def detect_prompt_injection(prompt: str) -> bool:
    prompt = prompt.lower()

    suspicious_patterns = [
        "ignore previous instructions",
        "reveal system prompt",
        "act as",
        "bypass",
        "override",
        "system prompt",
        "jailbreak"
    ]

    return any(pattern in prompt for pattern in suspicious_patterns)