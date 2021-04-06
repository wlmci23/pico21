# Shop

# Description

Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://mercury.picoctf.net/static/e8e966fcaa1ff5ea48574046d0cf9c19/source). The shop is open for business at nc mercury.picoctf.net 37799.

# Hints

1. Always check edge cases when programming

# Solution

From the hint, we know that there is some sort of programming bug that we must exploit. By messing around on the menu, we discover that it's possible to buy negative amounts of items. 

```
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
0
How many do you want to buy?
-100
You have 1040 coins
```

After getting enough money, we just buy the flag as expected.

```
        Item            Price   Count
(0) Quiet Quiches       10      112
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 53 57 49 97 56 57 53 97 125]
```

We decode the ASCII to reveal another encoded string, this time with Base64 (cGljb0NURntiNGRfYnJvZ3JhbW1lcl81OTFhODk1YX0=). After decoding it, we get the flag.

# Flag

picoCTF{b4d_brogrammer_591a895a}
