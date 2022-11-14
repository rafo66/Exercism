def leap_year(year):
    isDivisibleBy4 = (year % 4 == 0)
    isDivisibleBy100 = (year % 100 == 0)
    isDivisibleBy400 = (year % 400 == 0)
    return isDivisibleBy4 and (not isDivisibleBy100 or isDivisibleBy400)
