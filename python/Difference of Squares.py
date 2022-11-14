def square_of_sum(number):
    _sum = 0
    for i in range(1, number + 1):
        _sum += i
    return _sum ** 2


def sum_of_squares(number):
    _sum = 0
    for i in range(1, number + 1):
        _sum += i**2
    return _sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
