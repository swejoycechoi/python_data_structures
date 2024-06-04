'''Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.'''

''' pseudo-code
function reverse_list(input_list)
	left_index = 0
	right_index = length(input_list) - 1
	
	while left_index < right_index:
		swap input_list[left_index] with input_list[right_index]
		increment left_index
		decrement right_index
	
	return input_list'''

# python equivalent
def reverse_list(input_list):
	left_index = 0
	right_index = len(input_list) - 1
	
	while left_index < right_index:
		input_list[left_index], input_list[right_index] = input_list[right_index], input_list[left_index]
		left_index += 1
		right_index -= 1
	
	return input_list