#!/usr/bin/python

key=list("skeletor")
key2=[8,9,10,11,12,13,14,15,16]

print(key)
print(key2)

key3=""
for i in range(len(key)):
    key3 += chr(ord(key[i]) ^ key2[i])

print("key: {}".format(key3))
