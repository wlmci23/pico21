#!/usr/bin/python3

import string
import base64

encrypted = 'ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih'

LOWERCASE_OFFSET = ord('a')
ALPHABET = string.ascii_lowercase[:16]

def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]

def find(c):
    return ord(c) - LOWERCASE_OFFSET

def b16_decode(enc):
    plain = ''
    for i in range(0, len(enc), 2):
        first = enc[i]
        second = enc[i + 1]
        bf = find(first)
        bs = find(second)
        a = "{0:04b}".format(bf)
        b = "{0:04b}".format(bs)
        chval = int(a + b, 2)
        plain += chr(chval)
    return plain

for i in range(0, len(ALPHABET)):
    b16 = ''
    for c in encrypted:
        b16 += shift(c, chr(ord('a') + i))
    try:
        print(b16_decode(b16))
    except:
        # decoding failed, this is not the flag
        pass
