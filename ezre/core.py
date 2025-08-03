import re

def match(pattern: str, text: str) -> bool:
    return bool(re.match(pattern, text))

def find_all(pattern: str, text: str) -> list[str]:
    return re.findall(pattern, text)

def replace_all(pattern: str, repl: str, text: str) -> str:
    return re.sub(pattern, repl, text)

def search(pattern: str, text: str):
    return re.search(pattern, text)
