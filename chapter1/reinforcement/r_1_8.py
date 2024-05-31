'''Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
the same element?'''

# Hint: give your answer in terms of n and k

# For a string ss of length nn, the equivalent non-negative index jj for a negative index kk (where −n≤k<0−n≤k<0) is given by:
# j = n + k