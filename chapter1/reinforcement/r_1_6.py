'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.'''

def sum_of_squares_of_odds(n):
    total = 0
    for i in range (1, n):
        if i % 2 != 0:
            total += i ** 2
    return total