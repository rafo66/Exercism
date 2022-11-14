def processNumber(n):
    if n % 2 == 0:
        return n / 2
    return 3 * n + 1

def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    etapes = 0
    while number != 1:
        etapes += 1
        number = processNumber(number)
    return etapes
