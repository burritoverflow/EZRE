from .patterns import PATTERNS

def emails(text: str) -> list[str]:
    return PATTERNS["email"].findall(text)

def urls(text: str) -> list[str]:
    return PATTERNS["url"].findall(text)

def ipv4s(text: str) -> list[str]:
    return PATTERNS["ipv4"].findall(text)

def phone_numbers(text: str) -> list[str]:
    return PATTERNS["phone"].findall(text)

def numbers(text: str) -> list[str]:
    return PATTERNS["number"].findall(text)

def hashtags(text: str) -> list[str]:
    return PATTERNS["hashtag"].findall(text)

def mentions(text: str) -> list[str]:
    return PATTERNS["mention"].findall(text)
