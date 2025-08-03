from .patterns import PATTERNS
import re

def redact_emails(text: str, repl: str = "[REDACTED]") -> str:
    return PATTERNS["email"].sub(repl, text)

def redact_urls(text: str, repl: str = "[REDACTED]") -> str:
    return PATTERNS["url"].sub(repl, text)

def redact_phone_numbers(text: str, repl: str = "[REDACTED]") -> str:
    return PATTERNS["phone"].sub(repl, text)

def replace(pattern: str, repl: str, text: str) -> str:
    return re.sub(pattern, repl, text)
