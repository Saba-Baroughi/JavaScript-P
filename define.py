# Define a function named add_numbers
def add_numbers(nums_tuple, min_value):
    # Return the sum of values in nums_tuple that are greater or equal to min_value
    return sum(value for value in nums_tuple if value >= min_value)

# Outside of the function
# Create a variable named total and assign it the return value from calling add_numbers
total = add_numbers((21, 4, 7, 19, 1), 15)

# Print the total
print("Total:", total)


######## Examples
def addition(a, b):
    return a + b

print(addition(2,2))

def add_integers(list_integers):
	total = 0
	for x in list_integers:
		total += x
	return total

list_integers = [1, 2, 3, 4]
print(add_integers(list_integers))

######## Examples
def add_many_integers(*integers):
	# Rename *args to something suitable
	total = 0
	for x in integers:
		# As it is a tuple you can use the in keyword to iterate 
		total += x
	return total

print(add_many_integers(1,2,3,4,5,6,7,8,9))

######## Examples
def concatenate_words(**words):
	result = ""
	# As **kwargs is a dict you need to iterate over .values()
	for arg in words.values():
		result += arg
		result += " "
	return result

print(concatenate_words(a='This', b="is", c="a", d="useful", e="feature"))