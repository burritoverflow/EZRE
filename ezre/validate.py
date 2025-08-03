from .patterns import PATTERNS

def email(text: str) -> bool:
    return bool(PATTERNS["email"].match(text))

def url(text: str) -> bool:
    return bool(PATTERNS["url"].match(text))

def ipv4(text: str) -> bool:
    return bool(PATTERNS["ipv4"].match(text))

def phone(text: str) -> bool:
    return bool(PATTERNS["phone"].match(text))

def number(text: str) -> bool:
    return bool(PATTERNS["number"].match(text))
