# New Caesar

## Problem Description

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih [new_caesar.py](https://mercury.picoctf.net/static/2fc43dd1a3718df7debf367b0e092831/new_caesar.py)

## Hints

1. How does the cipher work if the alphabet isn't 26 letters?
2. Even though the letters are split up, the same paradigms still apply

## Solution

Here is the section of the program that actually encodes the flag.

```python
b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
```

We see that the flag is first Base16-encoded, and then a Caesar cipher is applied. Since the program asserts `len(key) == 1`, we know `key[i % len(key)]` will always be the same character.

We can uncipher the ciphertext by simply brute forcing each possible shift (with only 16 total). In this case, we also have to write a function to reverse the Base16 encoding.

The code can be found in [solve.py](./solve.py). After running it, it's clear which of the decoded strings is the flag.

## Flag

picoCTF{et_tu?_0797f143e2da9dd3e7555d7372ee1bbe}
