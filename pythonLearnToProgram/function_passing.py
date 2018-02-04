def function_runner(f):
    """ (function) -> NoneType

    Call f.
    """

    f()


def function_1():
    print("function_1 was called.")


def function_2():
    print("function_2 was called.")

def select(f,L):
    """ (function, list) -> list
    apply the selective function to L and return the result
    >>> L = [0,1,2,3,4,5,6]
    >>> L2 = select(every_third_index,L)
    >>> L2
    [0, 3, 6]

    """
    return f(L)

def every_third_index(L):
    """ (list) -> list
    return a list containing every third index item of the original list L
    >>> L = [0,1,2,3,4,5,6]
    >>> L2 = every_third_index(L)
    >>> L2
    [0, 3, 6]
    
    """
    lis = []
    for i in range(0,len(L),3):
        lis.append(L[i])
    return lis

def apply(f,L):
    """ (function, list of str) -> NoneType
    apply the function to the list
    >>> L = ['a','b','c']
    >>> apply(padLeft,L)
    >>> L
    ['   a', '   b', '   c']
    """
    padLeft(L,3)

def padLeft(L, size):
    """ (list of str, int) -> NoneType
    pad size space characters to the left of all str in L
    >>> L = ['a','b','c']
    >>> padLeft(L,3)
    >>> L
    ['   a', '   b', '   c']
    
    """
    for i in range(len(L)):
        formatter = '{0:>'+str(size+len(L[i]))+'}'
        L[i] = formatter.format(L[i])

if __name__ == '__main__':
    function_runner(function_1)
    function_runner(function_2)
    import doctest
    doctest.testmod()
