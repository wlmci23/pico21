# Easy Peasy

## Problem Description

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 41934 [otp.py](https://mercury.picoctf.net/static/1f148e5cdf8bd2c9f752b14d46a3f2f2/otp.py)

## Hints

1. Maybe there's a way to make this a 2x pad.

## Solution

Here is the section of interest in the program.

```python
def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1
	start = key_location
	stop = key_location + len(ui)
	kf = open(KEY_FILE, "rb").read()
	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop
	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))
	print("Here ya go!\n{}\n".format("".join(result)))
	return key_location
```

This is a one-time pad, which is unbreakable under certain conditions. As stated in the hint, if we were allowed to encrypt some data of our choosing with the same key as the flag, we would be able to decrypt the flag. However, it doesn't look like this is the case since the location in the key is changed each time something is encrypted.

```python
if stop >= KEY_LEN:
	stop = stop % KEY_LEN
```

The key here (no pun intended) is that if the key runs out, the index is reset back to the start, where the flag is encrypted. We know the length of the flag as well as the length of the key. Therefore, if we send exactly the right amount of data, we can achieve a 2-time pad.

This is demonstrated in [solve.py](./solve.py).

## Flag

picoCTF{abf2f7d5edf082028076bfd7a4cfe9a9}
