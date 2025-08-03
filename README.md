#**EZRE – Easy Regex for Python**
EZRE is a lightweight Python library that makes common regex tasks simple, readable, and extensible.
It provides validators, extractors, replacers, and a registry for custom patterns.

Honestly, I'm just tired of keeping track of different expressions. The expressions here are not _great_, but work well enough for my purposes at the moment. I plan to update them as I use the library.

##**Installation**
Not on pip!

Install from source:
```
git clone https://github.com/burritoverflow/EZRE.git
cd ezre
pip install .
```

##**Quick Usage**
```
import ezre

# Validation
ezre.validate.email("foo@bar.com")   # True
ezre.validate.url("https://x.com")   # True

# Extraction
text = "Contact me at foo@bar.com or visit https://x.com"
ezre.extract.emails(text)  # ['foo@bar.com']
ezre.extract.urls(text)    # ['https://x.com']

# Redaction
msg = "Send to foo@bar.com"
ezre.replace.redact_emails(msg)  # "Send to [REDACTED]"

# Custom Patterns
ezre.registry.register("hex", r"\b0x[a-fA-F0-9]+\b")
ezre.registry.find("hex", "Found 0xDEADBEEF and 0x1234")
# ['0xDEADBEEF', '0x1234']
```

##**Overview**
###Validators (ezre.validate)
```
email(text)	    Validate email address
url(text)	    Validate URL
ipv4(text)	    Validate IPv4 address
phone(text)	    Validate phone number
number(text)	Validate integer/float number
```

###Extractors (ezre.extract)
```
emails(text)	     Extract all emails
urls(text)	         Extract all URLs
ipv4s(text)	         Extract all IPv4 addresses
phone_numbers(text)	 Extract all phone numbers
numbers(text)	     Extract all numbers
hashtags(text)	     Extract hashtags (#tag)
mentions(text)	     Extract mentions (@user)
```

###Replacers (ezre.replace)
```
redact_emails(text, repl="[REDACTED]")	        Replace all emails
redact_urls(text, repl="[REDACTED]")	        Replace all URLs
redact_phone_numbers(text, repl="[REDACTED]")	Replace all phone numbers
replace(pattern, repl, text)	                Replace all matches for a custom pattern
```

###Core Helpers (ezre.core)
```
match(pattern, text)	            Check if text matches pattern
find_all(pattern, text)	            Return all matches
replace_all(pattern, repl, text)	Replace matches with repl
search(pattern, text)	            Return first match object
```

###Registry (ezre.registry)
```
register(name, pattern)	    Register a custom pattern
get(name)	                Get a registered pattern
find(name, text)	        Find matches using registered pattern
validate(name, text)	    Validate text using registered pattern
replace(name, repl, text)	Replace matches of registered pattern
```

##**Testing**
A simple test_all.py script has been included. Simply run with:
```
python test_all.py
```