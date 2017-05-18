"""Three codes that use the fibonacci formula."""

def fibonacci(n):
    """This is a function that finds the nth value in the fibonacci numbers."""
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


def lucas(n):
    """This is a function that will give you the nth value in the Lucas numbers. Online assistance was required. Code not fully our own. Help found at http://stackoverflow.com/questions/3793647/how-to-calculate-lucas-numbers-in-java."""
    if n is 0:
        return 2
    if n is 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """This is code that takes optional parameters and applies fibonacci rules to them."""
    if n is 0:
        return a
    if n is 1:
        return b
    result = a + b
    a = b
    b = result
    n -= 1
    return result if n is 0 else sum_series(n, a, b)

if __name__ == '__main__':
        """This is a function that finds the nth value in the fibonacci numbers."""
        print(fibonacci(5))
        """This is a function that will give you the nth value in the Lucas numbers. Online assistance was required. Code not fully our own. Help found at http://stackoverflow.com/questions/3793647/how-to-calculate-lucas-numbers-in-java."""
    
        print(lucas(15))
         """This is code that takes optional parameters and applies fibonacci rules to them."""
   
        print(sum_series(22,4,7))