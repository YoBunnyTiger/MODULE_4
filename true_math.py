from math import inf


def divide(first, second):
    num1 = int(first)
    num2 = int(second)
    if num2 == 0:
        return inf
    else:
        res = (num1/num2)
        return res
