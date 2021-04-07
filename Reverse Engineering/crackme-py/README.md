# crackme-py

## Description

File: [crackme.py](https://mercury.picoctf.net/static/db4b9e7a2862c320aa6b40e3551406bd/crackme.py)

## Hints

(None)

## Solution

By reading the comments, we see that there is a "really important number" hiding in this code. We can see that there is a variable called bezos_cc_secret, which is a jumble of text:

```python
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"
```

We also notice there is a decode function that is never used:

```python
def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)
```
Putting two and two together, we add this line to the end of the code and run it. It will ask for two numbers, then show you the flag:

```python
decode_secret(bezos_cc_secret);
```

## Flag

picoCTF{1|\/|_4_p34|\|ut_502b984b}
