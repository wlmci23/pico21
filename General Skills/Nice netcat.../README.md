# Nice netcat...

## Problem Description

There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 7449, but it doesn't speak English...

## Hints

1. You can practice using netcat with this picoGym problem: what's a netcat?
2. You can practice reading and writing ASCII with this picoGym problem: Let's Warm Up

## Solution

Use netcat to connect to the server. It will give you a lot of numbers, which is ASCII code. 

```bash
nc mercury.picoctf.net 7449
```

```
112
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
102
50
100
55
99
97
102
97
125
10
```

We can use an [online decoder](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html) or write a Python script to decode this. If you are using the online decoder, make sure to paste the numbers in the "Decimal (bytes)" field.

## Flag

picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}
