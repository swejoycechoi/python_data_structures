'''Exercise R-2.12 uses the mul method to support multiplying a Vector
by a number, while Exercise R-2.14 uses the __mul__ method to support
computing a dot product of two vectors. Give a single implementation of
Vector. __mul__ that uses run-time type checking to support both syntaxes
u*v and u*k, where u and v designate vector instances and k represents
a number'''

# Hint: Use the isinstance function to determine the operand type