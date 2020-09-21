#!/usr/bin/python

words=["hackadayu", "software", "reverse", "engineering", "ghidra"]
for word in words:
    c1 = ""
    c2 = ""
    new_word = ""
    for i, c in enumerate(word):
        c1 = c
        if i == (len(word) - 1):
            c2 = word[0]
        else:
            c2 = word[i + 1]
        if ord(c1) > ord(c2):
            c1 = ord(c1) - ord(c2)
        else:
            c1 = ord(c2) - ord(c1)
        c1 = chr(c1 + ord('`'))
        new_word += c1
    print("original: {} .. new: {}".format(word, new_word))
