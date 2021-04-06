# ARMssembly 1

## Problem Description

For what argument does this program print `win` with variables 58, 2 and 3? File: [chall_1.S](https://mercury.picoctf.net/static/1c8d50e39cf00d144e6a72119f68c16c/chall_1.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Hints

1. Shifts

## Solution

Here is the function of interest.

```arm
func:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 58
	str	w0, [sp, 16]
	mov	w0, 2
	str	w0, [sp, 20]
	mov	w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 20]
	ldr	w1, [sp, 16]
	lsl	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 24]
	sdiv	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	sub	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w0, [sp, 28]
	add	sp, sp, 32
	ret
```

As well, we see that we win when the return value of the function is 0.

```arm
bl	func
cmp	w0, 0
bne	.L4
```

Notes:
- Generally, an instruction that performs arithmetic will be of the form `op r1, r2, r3`, where `r1` is the register to store the result in and `r2` and `r3` are the operands
- `lsl` performs a bitwise left shit
- `sub` performs subtraction
- `sdiv` performs signed division

Here is the simplified pseudocode of the function (Python).

```python
def func(var1):
    # [sp, 12] - var1 (arg)
    # [sp, 16] - var2
    # [sp, 20] - var3
    # [sp, 24] - var4
    # [sp, 28] - var5
    var2 = 58
    var3 = 2
    var4 = 3
    # lsl	w0, w1, w0
    var5 = var2 << var3
    # sdiv	w0, w1, w0
    var5 = var5 / var4
    # sub	w0, w1, w0
    var5 = var5 - var1
    return var5 
```

The return value of the function is 0 when var1 = var5 at the end. So, the answer is simply the value of var5 at the end of the function, which is (58 << 2) / 3 = 77 or hex 4d.

## Flag

picoCTF{0000004d}
