'''Our Range class, from Section 2.3.5, relies on the formula
max(0, (stop − start + step − 1) // step)
to compute the number of elements in the range. It is not immediately evident
why this formula provides the correct calculation, even if assuming
a positive step size. Justify this formula, in your own words'''

# Hint: If we were to increase the stop value, one at a time, at what point
# would a new value appear in the range?