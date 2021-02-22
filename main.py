import math
def sq(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return "No answer"
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    return x1, x2


print(sq(2, 3, 5))