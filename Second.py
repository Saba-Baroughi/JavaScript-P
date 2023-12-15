# Provided data
data = {
    "first_name": "brian",
    "last_name": "johnson",
    "occupation": "student"
}

scores = [6, 9, 8, 7, 8, 9]

#Enter your code

# Loop through each key and value in the data dictionary
for key, value in data.items():
    # Check if the value is NOT equal to "student"
    if value != "student":
        # Update the string values for all strings that are not "student"
        data[key] = value.capitalize()

# Print the updated data
print("Updated Data:", data)

# Loop through the scores list using range() and len()
#In each iteration, i takes on the values 0, 1, 2, ..., up to len(scores) - 1.
# This allows you to use i as an index to access elements in the scores list.

for i in range(len(scores)):
    # Increase each value in the scores list by 1
    scores[i] += 1

# Print the updated scores
print("Updated Scores:", scores)
####################################################################

####List Comprehensions
## before we learned
numbers = []
for x in range(10):
    numbers.append(x)

###This same code could be written as a list comprehension.
numbers = [x for x in range(10)]

###Another Example
#his code returns [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)] 
# which is a list of tuples.
combination = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combination.append((x,y))

####Another examples
# 1. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i for i in range(10)])

# 2. [0, 2, 4, 6, 8, 10]
print([i for i in range(0,11,2)])

# 3. [0, 1, 4, 9, 16, 25, 36, 49]
print([x**2 for x in range(0,8)])

# 4. [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print([((i,(i+1))) for i in range(5)])

# 5. ['woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo']
print(['woohoo' for i in range(7)])

# 6. ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
hw = 'hello world'
print([i for i in hw])

# 7. [('A', 'D'), ('A', 'E'), ('A', 'F'), ('B', 'D'), 
# ('B', 'E'), ('B', 'F'), ('C', 'D'), ('C', 'E'), ('C', 'F')]
ab = 'ABCDEF'
print([(ab[i],ab[j]) for i in range(0,3) for j in range(3,6)])

######################################## Example
#Using list comprehension, add each letter from the string "Marvin" to a 
# list and assign it to a variable named letters.
letters = [letter for letter in "Marvin"]

# Print the value of the letters list
print("Letters:", letters)

# Task 2: Define a variable named numbers and assign it a list of values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension, extract the even numbers from the numbers list
evens = [number for number in numbers if number % 2 == 0]

# Print the value of the evens list
print("Evens:", evens)

#####################################################################

#Dictionary Comprehensions
#what we learned in the past
squares = {}
for x in (2, 4, 6):
    squares[x] = x**2
#This same code could be written as a dict comprehension.
squares = {x: x**2 for x in (2, 4, 6)}

# 1. {'apple': 5, 'mango': 5, 'banana': 6, 'cherry': 6}
fruits = ['apple', 'mango', 'banana','cherry']
print({f:len(f) for f in fruits})

# 2. {0: '', 1: '*', 2: '**', 3: '***', 4: '****'}
print({i:(i*'*') for i in range(0,5)})

# 3. {0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
print({i:(True if i%2==0 else False) for i in range(10)})

# 4. {(0, 0): True, (0, 1): False, (0, 2): False, (0, 3): False, (1, 0): False, (1, 1): True, (1, 2): False,
# (1, 3): False, (2, 0): False, (2, 1): False, (2, 2): True, (2, 3): False, (3, 0): False, (3, 1): False,
# (3, 2): False, (3, 3): True}
print({(i,j): (True if i==j else False) for i in range(4) for j in range(4)})