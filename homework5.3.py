# Task 5.3

import string

s = input()

for c in string.punctuation:
    s = s.replace(c, "")

words = s.split()

words = [word.capitalize() for word in words]

hashtag = "#" + "".join(words)

hashtag = hashtag[:140]
print(hashtag)