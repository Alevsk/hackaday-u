#!/usr/bin/python
xor_me = 0xdeadbeeffacecafe
key = "KeYpress"
index = 0
for c in key:
    print("index: {}".format( (xor_me >> (index << 3 & 0x3f)) + (ord(c)+1) ))
    index += 1
