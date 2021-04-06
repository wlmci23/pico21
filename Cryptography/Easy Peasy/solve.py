#!/usr/bin/python3

from pwn import *

r = remote('mercury.picoctf.net', 41934)

# read the encrypted flag
r.recvuntil('flag!\n')
encrypted = r.readline().decode('utf-8')[:-1]

# each character is encoded into two hex characters
length = len(encrypted) // 2

log.info(f'Encrypted flag: {encrypted}')

# send characters to overflow the key size
r.recvuntil('? ')
r.writeline('a' * (50000 - length))

# send the same amount of characters as the flag size
r.recvuntil('? ')
r.writeline('a' * length)

# read the data
r.recvuntil('!\n')
data = r.readline().decode('utf-8')[:-1]

log.info(f'Second pad: {data}')

r.close()

key = ''

# find the key used on the flag by xoring with 'a'
for x in range(0, len(data), 2):
    val = int(data[x] + data[x + 1], 16)
    chval = val ^ ord('a')
    key += chr(chval)

log.info(f'Flag key: {key}')

res = ''

# find the flag itself from the encrypted flag and the key
for x in range(0, len(encrypted), 2):
    val = int(encrypted[x] + encrypted[x + 1], 16)
    chval = val ^ ord(key[x // 2])
    res += chr(chval)

log.info(f'Flag: {res}')
