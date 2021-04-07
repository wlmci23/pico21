# Matryoshka doll

## Problem Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/2978e1270538613cd8181c7b0dabe9bd/dolls.jpg)

## Hints

1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as picoCTF{XXXXX}

## Solution

The problem suggests that there may be hidden files inside the image file. We use binwalk to find and extract these hidden files.

```bash
binwalk -e dolls.jpg
```

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378942, uncompressed size: 383937, name: base_images/2_c.jpg
651600        0x9F150         End of Zip archive, footer length: 22
```

Now, there is another image called 2_c.jpg! But we can do the same thing again. We continue doing this a few times, and eventually find flag.txt, which contains our flag.

## Flag

picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}
