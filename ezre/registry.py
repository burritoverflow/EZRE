import re

CUSTOM_PATTERNS: dict[str, re.Pattern] = {}

def register(name: str, pattern: str):
    CUSTOM_PATTERNS[name] = re.compile(pattern)

def get(name: str):
    return CUSTOM_PATTERNS.get(name)

def find(name: str, text: str):
    pat = get(name)
    return pat.findall(text) if pat else []

def validate(name: str, text: str) -> bool:
    pat = get(name)
    return bool(pat.match(text)) if pat else False

def replace(name: str, repl: str, text: str) -> str:
    pat = get(name)
    return pat.sub(repl, text) if pat else text
