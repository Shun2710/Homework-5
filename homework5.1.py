# Task 5.1

import string
import keyword

s = input()

is_valid = True

if s[0].isdigit():
    is_valid = False

if any(c.isupper() for c in s):
    is_valid = False

allowed_punctuation = "_"
for c in s:
    if c in string.punctuation and c not in allowed_punctuation:
        is_valid = False
    if c.isspace():
        is_valid = False

if s in keyword.kwlist:
    is_valid = False

if "__" in s:
    is_valid = False

print(is_valid)