def is_armstrong_number(number):
    numberOfDigits = len(str(number))
    
    _sum = 0
    for i in str(number):
        _sum += int(i) ** numberOfDigits

    return _sum == number
