def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def five(numero):
    if numero <= 0:
        return False
    while numero % 5 == 0:
        numero //= 5
    return numero == 1