# ARMssembly 3

## Problem Description

What integer does this program print with argument 597130609? File: [chall_3.S](https://mercury.picoctf.net/static/853a1bc2eb2edbfa6651814cddd75a3b/chall_3.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Hints

1. beep boop beep boop...

## Solution

This time, we have two functions to analyze. Luckily, the second function is very simple.

```arm
func1:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	wzr, [x29, 44]
	b	.L2
.L4:
	ldr	w0, [x29, 28]
	and	w0, w0, 1
	cmp	w0, 0
	beq	.L3
	ldr	w0, [x29, 44]
	bl	func2
	str	w0, [x29, 44]
.L3:
	ldr	w0, [x29, 28]
	lsr	w0, w0, 1
	str	w0, [x29, 28]
.L2:
	ldr	w0, [x29, 28]
	cmp	w0, 0
	bne	.L4
	ldr	w0, [x29, 44]
	ldp	x29, x30, [sp], 48
	ret
```

```arm
func2:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	add	w0, w0, 3
	add	sp, sp, 16
	ret
```

Notes:
- `and` is a bitwise and
- `beq` and `bne` jump on equal and not equal respectively
- `bl` calls a function (registeres can be mutated inside a function)
- `lsr` is a bitwise right shift

We convert this into a pseudocode form as before. Again, we start by using goto and labels.

```python
def func1(var1):
    # [x29, 28] - var1 (arg)
    # [x29, 44] - var2
    var2 = 0
    goto L2
    L4:
        # and	w0, w0, 1
	    # cmp	w0, 0
        # beq	.L3
        if var1 & 1 == 0:
            goto L3
        # bl	func2
        # str	w0, [x29, 44]
        var2 = func2(var2)
    L3:
        # lsr	w0, w0, 1
        var1 = var1 >> 1
    L2:
        # cmp	w0, 0
	    # bne	.L4
        if var1 != 0:
            goto L4
    return var2

def func2(var3):
    # [sp, 12] - var3 (arg)
    return var3 + 3
```

Next, we see that this seems to be a while loop. We can also simplify the goto inside the loop by simply changing the if condition.

```python
def func1(var1):
    var2 = 0
    while var1 != 0:
        if var1 & 1 != 0:
            var2 = func2(var2)
        var1 = var1 >> 1
    return var2

def func2(var3):
    return var3 + 3
```

This program just counts the number of set bits in the binary representation of its argument, and multiplies it by 3. We can calculate this manually.

```python
>>> hex(bin(597130609).count('1') * 3)
'0x36'
```

So, our hex value is 36.

## Flag

picoCTF{00000036}
