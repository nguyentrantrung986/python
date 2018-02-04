def sink_sort(L):
    """ (list) -> NoneType

    Sort L using bubble sort in reverse, move the smallest item to the beginning
    of the list
    >>> L = [5, 7, 2, 8]
    >>> sink_sort(L)
    >>> L
    [2, 5, 7, 8]
    >>> L = [4]
    >>> sink_sort(L)
    >>> L
    [4]
    >>> L = []
    >>> sink_sort(L)
    >>> L
    []
    >>> L = [5, 7, 2, 8, -7]
    >>> sink_sort(L)
    >>> L
    [-7, 2, 5, 7, 8]
    
    """
    b = 0
    length = len(L)
    i = length - 1

    while b < length -1:
        for i in range(length-1, b, -1):
            if L[i] < L[i-1]:
                L[i], L[i-1] = L[i-1], L[i]
        b = b + 1

def selection_sort(L):
    """ (list) -> NoneType

    Sort L using bubble sort in reverse, move the smallest item to the beginning
    of the list
    >>> L = [5, 7, 2, 8, -7]
    >>> selection_sort(L)
    >>> L
    [-7, 2, 5, 7, 8]
    >>> L = [12, 6, 1, 4, 100, 2.1]
    >>> selection_sort(L)
    >>> L
    [1, 2.1, 4, 6, 12, 100]
    
    """
    length = len(L)
    for i in range(length-1):
        min_index = i
        for j in range(i+1,length,1):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
        
def insertion_sort(L):
    """ (list) -> NoneType

    insert the item at index i to the correct position in the sorted part of the list
    >>> L = [5, 7, 2, 8, -7]
    >>> selection_sort(L)
    >>> L
    [-7, 2, 5, 7, 8]
    >>> L = [12, 6, 1, 4, 100, 2.1]
    >>> insertion_sort(L)
    >>> L
    [1, 2.1, 4, 6, 12, 100]
    
    """
    length = len(L)
    for e in range(1,length):
        for i in range(0,e):
            if L[i] > L[e]:
                #shift items greater than L[e] to the right, insert L[e] at correct position
                value = L[e]
                for j in range(e,i-1,-1):
                    L[j] = L[j-1]
                L[i] = value
                break

def insertion_sort_v2(L):
    """ (list) -> NoneType

    insert the item at index i to the correct position in the sorted part of the list
    >>> L = [5, 7, 2, 8, -7]
    >>> selection_sort(L)
    >>> L
    [-7, 2, 5, 7, 8]
    >>> L = [12, 6, 1, 4, 100, 2.1]
    >>> insertion_sort(L)
    >>> L
    [1, 2.1, 4, 6, 12, 100]
    """
    for e in range(len(L)):
        i = e
        value = L[e]
        #shift greater items to the right
        while i > 0 and L[i-1] > value:
            L[i] = L[i-1]
            i = i-1
        L[i] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()


        
