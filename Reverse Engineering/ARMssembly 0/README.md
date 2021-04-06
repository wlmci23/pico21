# ARMssembly 0

## Description

What integer does this program print with arguments 3854998744 and 915131509? File: [chall.S](https://mercury.picoctf.net/static/b3b17204c7ce77f184a397c4fae4a35b/chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Hints

1. Simple compare

## Solution

Here is the code of the function we are interested in.

```arm
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
```

Notes:
- `w0` and `w1` are general purpose registers
- `str` stores its first operand at the address given by its second operand
- `ldr` loads into its first operand the data at the address given by its second operand
- `bls` jumps to a label if the last compare was either less or the same
- `b` is an unconditional jump

After some simplifying, we have the following pseudocode (Python).

```python
def func1(var1, var2):
    # [sp, 12] - var1 (w0)
    # [sp, 8] - var2 (w1)
    if var2 <= var1:            # cmp w1, w0
        var1 = var1             # ldr w0, [sp, 12]
    else:
        var1 = var2             # ldr w0, [sp, 8]
    return var1
```

It is now clear that the function simply returns the greater of the two operands. Since our operands are 3854998744 and 915131509, we get our answer as hex e5c69cd8.

## Flag

picoCTF{e5c69cd8}
