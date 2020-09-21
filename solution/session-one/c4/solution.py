#!/usr/bin/python

key="hackaday-u"
result = ""
for c in key:
    result += chr(ord(c)+2)
print(result)

