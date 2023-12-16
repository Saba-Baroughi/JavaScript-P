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
#output=10




######## Examples
def add_many_integers(*integers):
	# The *integers syntax indicates that the function can accept any number of arguments,
    #  and these arguments will be packed into a tuple named integers.
    #  This allows you to pass a variable number of integers to the function when calling it.
	total = 0
	for x in integers:
		# As it is a tuple you can use the in keyword to iterate 
		total += x
	return total

print(add_many_integers(1,2,3,4,5,6,7,8,9))
#45 the sum of numbers

######## Examples
def concatenate_words(**words):
	result = ""
	# In your function definition, you are using **words as a parameter, which indicates
    #  that the function can accept any number of keyword arguments (kwargs). 
    # The ** syntax is used for unpacking keyword arguments into a dictionary.
	for arg in words.values():
		result += arg
		result += " "
	return result

print(concatenate_words(a='This', b="is", c="a", d="useful", e="feature"))
#output: This is a useful feature



#Functions - *args & **kwargs Challenge
#In the *args and **kwargs lesson, you learned how to pass multiple values to functions
#  where the length of the data sent to the function may vary each time the function is called,
#  allowing for much more flexibility when working with functions.
 
#If you want to pass a function a list of values, you add the * operator before 
# the parameter in the function definition.
 
#If you want to pass a function a number of key-value pairs,
#  you add the ** operator before the parameter in the function definition. 
# When you do this, the key-value pairs sent to the function can be accessed
#  in the same way you would access keys and values in a dictionary.
#### Quizz
def make_string(*strings):
    """
    Concatenates the values in the tuple and separates them by a space.

    Parameters:
    *strings (str): Any number of strings to be joined.

    Returns:
    str: The concatenated string with values separated by a space.
    """
    return " ".join(strings)

# Call the make_string function
my_string = make_string("Alderaan", "Coruscant", "Dagobah", "Endor", "Hoth")
print(my_string)

def get_age(**data):
    """
    Returns the age value from the dictionary or "no age provided" if not present.

    Parameters:
    **data (dict): A dictionary containing key-value pairs.

    Returns:
    int/str: The age value or "no age provided".
    """
    return data.get("age", "no age provided")

# Call the get_age function
pats_age = get_age(name="pat", level=4, age=33, occupation="postman")
print(pats_age)