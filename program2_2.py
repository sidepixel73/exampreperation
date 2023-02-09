def converter(number):
    alphabet = '01234567'
    result = ''
    while number > 0:
        print(result)
        result = alphabet[number % 8] + result
        number //= 8
    return result
for n in range(1000,10000):
    if ((n // 1000) / 4 == 1) or ((n // 1000) / 4 == 2):
        r = n % 1000 + 9000
        print(converter(r))
