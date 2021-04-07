# Transformation

## Problem Description

I wonder what this really is... [enc](https://mercury.picoctf.net/static/77a2b202236aa741e988581e78d277a6/enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Hints

1. You may find some decoders online

## Solution

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

From the code given, we see that the encoded flag is such that each character represents two characters in the original flag. The first one is represented by the upper 8 bits and the second one is represented by the lower 8 bits. This is easily reversed using a simple Python program ([solve.py](./solve.py)).

## Flag

picoCTF{16_bits_inst34d_of_8_75d4898b}
