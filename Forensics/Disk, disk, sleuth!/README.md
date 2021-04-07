# Disk, disk, sleuth!

## Problem Description

Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/ac394d24f88e51a09cc909687cf6d853/dds1-alpine.flag.img.gz)

## Hints

1. Have you ever used `file` to determine what a file was?
2. Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85
3. Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48
4. Using your own computer, you could use qemu to boot from this disk!

## Solution

After downloading and unzipping the file, we see that it is a DOS/MBR boot sector. Following the suggestion in the problem description, we run srch_strings on the file to get a list of strings. Then, we grep the output to find the flag.

```bash
srch_strings dds1-alpine.flag.img | grep pico
```

## Flag

picoCTF{f0r3ns1c4t0r_n30phyt3_dcbf5942}
