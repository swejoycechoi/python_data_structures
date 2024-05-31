'''Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.'''

# Hint: how can you describe the range of integers for the sum?
# [ expression for value in iterable if condition ]

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n))
