''' Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n. '''

def sum_of_squares(n):
	# initialize the sum to 0
	total = 0
	
	# loop through all positive integers smaller than n
	for i in range(1, n):
		# add the square of the current integer to the total
		total += i ** 2
	return total