"""This is a function that finds the nth value in the fibonacci numbers."""

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

"""This is a function that will give you the nth value in the Lucas numbers."""

def lucas(n):
    a = 2
    b = 1
    if n < 2:
        return n
    while n > 0:
        result = a + b
        a = b
        b = result
        n -= 1
    return result