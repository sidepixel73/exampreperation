for i in range(100, 0, -1):
    s = bin(i)[2:] # перевод в двоичную систему
    s = str(s)
    if i % 2 == 0:
        s += "10"
    else:
        s += "01"
    r = int(s, 2) # перевод в десятичную систему
    if r < 109:
        print(r)
        break