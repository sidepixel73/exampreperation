print ("x,y,f")
for x in range(2):
    for y in range(2):
        f = not(x or y)
        print(x, y, f)