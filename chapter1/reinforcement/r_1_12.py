'''Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.'''

import random

def custom_choice(data):
    if not data:
        raise ValueError("Cannot choose from an empty sequence")
    random_index = random.randrange(len(data))
    return data[random_index]

# Example usage:
sample_data = [10, 20, 30, 40, 50]
print(custom_choice(sample_data))  # This will print a random element from sample_data