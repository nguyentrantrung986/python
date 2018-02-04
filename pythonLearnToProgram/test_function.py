def square(x):
    return x**2

def cube(x):
    cube = x*square(x)
    return cube

cube(2)

def sumFirstN():
    digits = '0123456789'
    result = 0

    for digit in digits:
        result = result + int(digit)

    print(result)

def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that     appear at leastonce in s2. The characters in the result        will appear in the same order asthey appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a' 
    >>> common_chars('abb', 'ab')
    'abb' 
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''


    res = ''

    for ch in s1:
        if ch in s2:
            res = ch + res
    
    return res

def happy():
    message = 'Happy 29th!'
    new_message = ''

    for char in message:
        if char.isdigit():
            new_message = new_message + str((int(char) + 1) % 10)
        else:
            new_message = new_message + char

    print(new_message)
