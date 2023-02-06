i = 49**7+7**20-28
def converter_to_seven(number):
    digits = '0123456'
    result = ''
    while number > 0:
        print(result)
        result = digits[number % 7] + result
        number //= 7
    return result

f = str(converter_to_seven(i))
