# Tab, Tab, Attack

## Problem Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/72712e82413e78cc8aa8d553ffea42b0/Addadshashanammu.zip)

## Hints

1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Solution

We use the `unzip` command to unzip the zip file. It will extract a directory called "Addadshashanammu", which contains a few subdirectories, all with long names.

To make your life easier when traversing the directories, use the tab key to autocomplete the directory name when using `cd`. At the end of the directory chain, you will find an executable file called "fang-of-haynekhtnamet" which will output the flag when executed.

## Flag

picoCTF{l3v3l_up!_t4k3_4_r35t!_6f332f10}
