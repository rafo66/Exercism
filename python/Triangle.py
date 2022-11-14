def isTriangle(a, b, c):
    return (a + b >= c) and (b + c >= a) and (a + c >= b) and (a > 0) and (b > 0) and (c > 0)
def equilateral(sides):
    return isTriangle(sides[0], sides[1], sides[2]) and (sides[0] == sides[1] == sides[2])
def isosceles(sides):
    return isTriangle(sides[0], sides[1], sides[2]) and (int(sides[0] == sides[1]) + int(sides[0] == sides[2]) + int(sides[1] == sides[2]) >= 1)
def scalene(sides):
    return isTriangle(sides[0], sides[1], sides[2]) and (int(sides[0] == sides[1]) + int(sides[0] == sides[2]) + int(sides[1] == sides[2]) == 0)
