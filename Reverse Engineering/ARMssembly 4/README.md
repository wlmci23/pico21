# ARMssembly 4

## Problem Description

What integer does this program print with argument 1151828495? File: [chall_4.S](https://mercury.picoctf.net/static/0a6c557375c9131dd67cb19beabd7d0c/chall_4.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Hints

1. Switching things up

## Solution

We're going to take a different approach with this problem. Since registers can be mutated through function calls, it becomes hard to track local variables. So, we implement these registers in pseudocode as global variables. Still, this problem is not trivial.

We have eight functions that we need to reverse engineer, so let's get to work. The register we really care about is w0, which typically stores the return value.

Notes:
- The variables stored in [x29, 28] in func1 and [x29, 28] in func2 are not the same variables because func2 decrements the stack pointer (same thing applies for the other functions)
- `bhi` branches on higher
- `udiv` is unsigned division and `mul` is multiplication


```python
w0 = 1151828495
# any starting value in w1 and w2 will do
w1 = 0
w2 = 0

def func1():
    # [x29, 28] - var1
    var1 = w0
    if w0 <= 100:
        goto L2
    w0 = w0 + 100
    func2()
    goto L3
    L2:
        w0 = var1
        func3()
    L3:
        return

def func2():
    # [x29, 28] - var2
    var2 = w0
    if w0 > 499:
        goto L5
    w0 = var2
    w0 = w0 - 86
    func4()
    goto L6
    L5:
        w0 = var2
        w0 = w0 + 13
        func5()
    L6:
        return

def func3():
    # [x29, 28] - var3
    var3 = w0
    func7()

def func4():
    # [x29, 27] - var4 
    # [x29 44] - var5
    var4 = w0
    w0 = 17
    var5 = w0
    func1()
    var5 = w0

def func5():
    # [x29, 28] - var6
    var6 = w0
    func8()
    var6 = w0

def func6():
    # [sp, 12] - var7
    # [sp, 24] - var8
    # [sp, 28] - var9
    # [sp, 20] - var10
    var7 = w0
    var8 = 314
    w0 = 1932
    var9 = w0
    var10 = 0
    goto L14
    L15:
        w1 = var9
        w0 = 800
        w0 = w1 * w0
        w1 = var8
        w2 = w0 / 21
        w1 = var8
        w1 = w2 * w1
        w0 = w0 - w1
        var7 = w0
        w0 = var10
        w0 = w0 + 1
        var10 = w0
    L14:
        w0 = var10
        if w0 <= 899:
            goto L15
        w0 = var7

def func7():
    # [sp, 12] - var11
    var11 = w0
    if w0 <= 100:
        goto L18
    w0 = var11
    goto L19
    L18:
        w0 = 7
    L19:
        return

def func8():
    # [sp, 12] - var12
    var12 = w0
    w0 = w0 + 2
```

Now we have more readable code, but it's still quite obfuscated. We're going to simplify this code further through the following.

1. Replace func3, func4, and func5, which just call other functions.
2. Replace func8, which just increments w0 by 2.
3. func6 isn't actually called at all, so we can just remove it.
4. The goto and labels in func1, func2, and func7 are just if else structures, which we can replace them with.
5. After step 4, we can see that all func7 does is set w0 to 7 if w0 is smaller than or equal to 100, so we can replace it
6. Simplify func2 by concatenating some of the expressions.

If all goes right, we now have the following, much shorter code.

```python
w0 = 1151828495
w1 = 0
w2 = 0

def func1():
    if w0 <= 100:
        if w0 <= 100:
            w0 = 7
    else:
        w0 += 100
        func2()

def func2():
    if w0 > 499:
        w0 = w0 + 15
    else:
        w0 = 17
        func1()
```

Now, we can just following the logical structure of the code. Since w0 > 100, func1 will execute its else block, making w0 1151828495 + 100 = 1151828595. Then, func2 executes the if block since w0 > 499, making w0 1151828595 + 15 = 1151828610, which is our answer. The hex form is 44a78282.

## Flag

picoCTF{44a78282}
