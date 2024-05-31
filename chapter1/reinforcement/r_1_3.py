'''Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.'''

# Hint: keep track of the smallest and largest value while looping
def minmax(data):
    """
    Find the smallest and largest numbers in a sequence.

    Parameters:
    data (sequence): A sequence of one or more numbers.

    Returns:
    tuple: A tuple containing the smallest and largest numbers.
    """
    if not data:
        raise ValueError("The data sequence cannot be empty")
    
    # Initialize min and max with the first element of the data sequence
    smallest = largest = data[0]
    
    # Loop through the data sequence to find the min and max values
    for num in data[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    
    return (smallest, largest)