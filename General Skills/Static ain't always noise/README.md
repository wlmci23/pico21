# Static ain't always noise

## Problem Description

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static)? This [BASH script](https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/ltdis.sh) might help!

## Hints

(None)

## Solution

By using the `file` command, we see that this file is an executable. But running it (after using chmod to make it executable) doesn't seem to yield anything useful.

We can use the `strings` command to find static strings in an executable. We pipe the output to grep to eliminate useless strings.

```bash
strings static | grep "picoCTF"
```

```
picoCTF{d15a5m_t34s3r_f5aeda17}
```

## Flag

picoCTF{d15a5m_t34s3r_f5aeda17}
