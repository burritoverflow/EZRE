import ezre

print("=== VALIDATION TESTS ===")
print("Valid Email:", ezre.validate.email("foo@bar.com"))       # True
print("Invalid Email:", ezre.validate.email("foo@bar"))         # False
print("Valid URL:", ezre.validate.url("https://example.com"))   # True
print("Invalid URL:", ezre.validate.url("htp:/example"))        # False
print("Valid IPv4:", ezre.validate.ipv4("192.168.0.1"))         # True
print("Invalid IPv4:", ezre.validate.ipv4("999.999.999.999"))   # False
print("Valid Phone:", ezre.validate.phone("+1 800 555 1234"))   # True
print("Invalid Phone:", ezre.validate.phone("abc-123"))         # False
print("Valid Number:", ezre.validate.number("42.5"))            # True
print("Invalid Number:", ezre.validate.number("abc"))           # False

print("\n=== EXTRACTION TESTS ===")
text = """
Email me at foo@bar.com or baz@example.org. Don't email qux@a!
Visit https://site.com and http://foo.org, but not htp:/baz.com
My IPs are 10.0.0.1 and 8.8.8.8 and 999.999.999.999. Call +44 123 456 789 or 3325568462, but not 911! Price: 199.99 USD.
#dev #python @user1 @user_two
"""
print("Emails:", ezre.extract.emails(text))
print("URLs:", ezre.extract.urls(text))
print("IPv4s:", ezre.extract.ipv4s(text))
print("Phone numbers:", ezre.extract.phone_numbers(text))
print("Numbers:", ezre.extract.numbers(text))
print("Hashtags:", ezre.extract.hashtags(text))
print("Mentions:", ezre.extract.mentions(text))

print("\n=== REPLACER TESTS ===")
msg = "Contact foo@bar.com or visit https://x.com"
print("Redacted emails:", ezre.replace.redact_emails(msg))
print("Redacted URLs:", ezre.replace.redact_urls(msg))
print("Custom replace digits:", ezre.replace.replace(r"\d", "X", "My number is 12345"))

print("\n=== CORE HELPERS TESTS ===")
pattern = r"\b\w{4}\b"  # Match any 4-letter word
sample = "This text has some four word code test data."
print("match():", ezre.core.match(pattern, "This"))
print("find_all():", ezre.core.find_all(pattern, sample))
print("replace_all():", ezre.core.replace_all(pattern, "[****]", sample))
print("search():", ezre.core.search(pattern, sample).group())

print("\n=== REGISTRY TESTS ===")
ezre.registry.register("hex", r"\b0x[a-fA-F0-9]+\b")
test_hex = "Found 0xDEADBEEF and 0x1234"
print("Registry find:", ezre.registry.find("hex", test_hex))
print("Registry validate:", ezre.registry.validate("hex", "0x123ABC"))
print("Registry replace:", ezre.registry.replace("hex", "[HEX]", test_hex))

# Demonstrating missing pattern behavior
print("Registry find (missing):", ezre.registry.find("unknown", "test"))
print("Registry validate (missing):", ezre.registry.validate("unknown", "test"))
print("Registry replace (missing):", ezre.registry.replace("unknown", "[X]", "test"))

print("\n=== ALL TESTS COMPLETE ===")
