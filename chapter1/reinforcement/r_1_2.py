'''Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.'''

# Hint: use bit operations
def is_even(k):
    """
    Check if an integer k is even using bit operations.

    Parameters:
    k (int): The integer to check.

    Returns:
    bool: True if k is even, False otherwise.
    """
    return (k & 1) == 0
