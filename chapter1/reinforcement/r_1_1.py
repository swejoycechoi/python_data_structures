'''Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.'''

# Hint: the modulo operator could be useful here
def is_multiple(n,m):
    '''check if n is a multiple of m.
    n(int): the number to check
    m(int): the number to divide by

    returns a bool
    true if n is a multiple of m
    false otherwise'''
    return n % m == 0
