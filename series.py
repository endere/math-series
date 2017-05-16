"""Constring."""


def fibonacci(n):
    a = 0
    b = 0
    if n < 2:
        return n
    while n > 0:
        result = a + b
        a = b
        b = result
        n -= 1
        if b is 0:
            b = 1
    return result

