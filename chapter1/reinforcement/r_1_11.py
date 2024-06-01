'''Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].'''

# Hint: those look like powers of two

powers_of_two = [2**i for i in range(9)]
print(powers_of_two)