encoded = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'

flag = ''

for char in encoded:
    chval = ord(char)
    char1 = chr(chval >> 8) # upper 8 bits
    char2 = chr(chval & 0xFF) # lower 8 bits
    flag += char1 + char2

print(flag)
