#!/usr/bin/pyhon

# Generate key
key=['0']*16
index=0
for i in range(16):
    if index+1 >= 16:
        break
    key[index+1] = chr(ord(key[index])+1)
    index += 2
print("key: " + "".join(key))

# Validate key
index=0
while index < len(key):
    if ord(key[index]) - ord(key[index+1]) != -1:
        print("invalid")
    index += 2
