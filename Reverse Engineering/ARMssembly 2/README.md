# ARMssembly 2

## Problem Description

What integer does this program print with argument 1748687564? File: [chall_2.S](https://mercury.picoctf.net/static/225b8846edf2234e9ce85aaab176b062/chall_2.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Hints

1. Loops

## Solution

Once again, here is the function of interest.

```arm
func1:
    sub sp, sp, #32
    str w0, [sp, 12]
    str wzr, [sp, 24]
    str wzr, [sp, 28]
    b   .L2
.L3:
    ldr w0, [sp, 24]
    add w0, w0, 3
    str w0, [sp, 24]
    ldr w0, [sp, 28]
    add w0, w0, 1
    str w0, [sp, 28]
.L2:
    ldr w1, [sp, 28]
    ldr w0, [sp, 12]
    cmp w1, w0
    bcc .L3
    ldr w0, [sp, 24]
    add sp, sp, 32
    ret
```

Notes:
- `wzr` simply stores the value 0
- `bcc` branches if the carry flag is clear (in this case, the same as branch on lower)

Here is the simplified pseudocode of the function (Python). We also used goto and labels in this code, which is not a part of the Python grammar.

```python
def func(var1):
    # [sp, 12] - var1 (arg)
    # [sp, 24] - var2
    # [sp, 28] - var3
    # str   wzr, [sp, 24]
    var2 = 0
    # str   wzr, [sp, 28]
    var3 = 0
    goto L2
    L3:
        # add   w0, w0, 3
        var2 = var2 + 3
        # add   w0, w0, 1
        var3 = var3 + 1
    L2:
        # cmp   w1, w0
        if var3 < var1:
            # bcc   .L3
            goto L3
    return var2
```

We see that this structure seems to emulate a while loop (the loop condition being var3 < var1). So, we can simplify this function further. We also rename var3 to i since it seems to be an iterator.

```python
def func(var1):
    # [sp, 12] - var1 (arg)
    # [sp, 24] - var2
    # [sp, 28] - i
    # str   wzr, [sp, 24]
    var2 = 0
    # str   wzr, [sp, 28]
    i = 0
    while i < var1:
        var2 = var2 + 3
        i = i + 1
    return var2
```

Now, it is clear that the value returned is just the input multiplied by 3. In this case, the input is 1748687564, which is 5246062692 after being multiplied by 3, or hex 138b09064. Note that we have to truncate this hex value since it's too long.

## Flag

picoCTF{38b09064}
