# Obedient Cat

## Problem Description

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/704f877da185904ec3992e7255a15c6c/flag).

## Hints

1. Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/704f877da185904ec3992e7255a15c6c/flag
3. $ man cat

## Solution

After downloading the file (see the second hint above for help), simply run the cat command to get the flag.

```bash
cat flag
```

```
picoCTF{s4n1ty_v3r1f13d_1a94e0f9}
```

## Flag

picoCTF{s4n1ty_v3r1f13d_1a94e0f9}
