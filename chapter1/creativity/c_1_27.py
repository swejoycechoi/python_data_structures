'''In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementations,
from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance advantages.'''

# Hint: Either buffer the bigger value from each pair of factors, or repeat
# the loop in reverse to avoid the buffer