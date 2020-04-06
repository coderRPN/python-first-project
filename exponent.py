def exponent(x, y):
    result = 1
    for i in range(y):
        result = result * x
    return result


print(exponent(2, 90000))
