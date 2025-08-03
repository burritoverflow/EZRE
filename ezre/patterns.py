import re

PATTERNS = {
    # Match emails (RFC 5322 simplified)
    "email": re.compile(
        r"(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*"
        r"@"
        r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
        r"[a-zA-Z]{2,})"
    ),

    # URL with basic domain/path validation
    "url": re.compile(
        r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:[^\s\)\]\}\>,]*)"
    ),

    # IPv4
    "ipv4": re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
    ),

    # Phone numbers
    "phone": re.compile(
        r"\+?\d{1,3}?[\s\-]?\(?\d{1,4}\)?(?:[\s\-]?\d{2,}){2,}"
    ),

    # Numbers
    "number": re.compile(
        r"(?<![\w.])\d+(?:\.\d+)?(?![\w.])"
    ),

    # Hashtag (letters, digits, underscores)
    "hashtag": re.compile(r"(?<!\w)#\w+"),

    # Mention (@username) but not inside an email
    "mention": re.compile(r"(?<!\w)@\w+"),
}
