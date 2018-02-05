import math

def f_prime_exponentiation(f_val, x):
    """ (number) -> number

    formular to calculate the derivative from function value and input value.
    The derivative of e to the x is e to the x
    >>> f_prime_exponentiation(1, 0)
    1
    """
    return f_val

def euler_approx(f_val, f_prime, x_val, h, times_to_repeat):
    """ (number, function, number, number, int) -> number

    approximate the value of f(x_val+h) using euler method, given intial value
    f_val of the function and initial input x_val. Repeat linear approximation
    times_to_repeat times in the interval h.
    >>> euler_approx(1, f_prime_exponentiation, 0, 1, 1)
    2.0
    >>> euler_approx(1, f_prime_exponentiation, 0, 1, 2)
    2.25
    >>> euler_approx(1, f_prime_exponentiation, 0, 1, 3)
    2.3703703703
    >>> euler_approx(1, f_prime_exponentiation, 0, 1, 4)
    2.44140625
    >>> euler_approx(1, f_prime_exponentiation, 0, 1, 10)
    2.5937424601
    """
    from decimal import Decimal, getcontext
    getcontext().prec = 11
    step = Decimal(h)/Decimal(times_to_repeat)
    f = Decimal(f_val)
    x = Decimal(x_val)
    for i in range(times_to_repeat):
        f = f + Decimal(f_prime(f,x_val)) * step
        x = x + step

    return float(f)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
        
