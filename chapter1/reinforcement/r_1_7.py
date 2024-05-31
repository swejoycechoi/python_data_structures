'''Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function.'''

# Hint: how can you describe the range of integers for the sum?

def sum_of_squares_of_odds(n):
    return sum(i ** 2 for i in range(1, n) if i % 2 != 0)