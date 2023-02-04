'''
F(1)= 1
F(n) = 2*F(n-1) +1 при n > 1
'''
def fun(n):
    if n == 1:
        return 1
    else:
        n = 2 * fun(n-1) + 1
        return n

print(fun(6))