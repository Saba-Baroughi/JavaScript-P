numbers=[1,2,23,4,5]
numbers.append(6)
print(numbers)
print('Hello, World!' == 'Hello, World!')
print(2!=2)
print([1,2]<[1,2,3])
print(float(2)>=int(2))
print('a'<'A') #This is False as 'a' is Unicode 97 where 'A' is 65
my_string = "HELLO WORLD"
my_string_lower_case = my_string.lower()

print(my_string_lower_case)

my_string_2 = "hElLo WorLD"
my_string_2_upper_case = my_string_2.upper()

print (my_string_2_upper_case)
print (my_string.isalpha())

greetings = my_string.replace("WORLD", "Dave")
print(greetings)

motion = ("jump", "walk", "run")
new_string = 'ing '.join(motion)
print(new_string)

print(my_string_2.split(" "))

spaced_string = "     42       "
print(spaced_string.strip())


#another Example
# Assign values to variables
a = []        # List (Falsy)
b = ""        # Empty string (Falsy)
c = "Hello"   # Non-empty string (Truthy)
d = 0.0       # Float with value 0.0 (Falsy)
e = 42        # Integer with a non-zero value (Truthy)

# Print truthy/falsy values
print(bool(a))  # Falsy
print(bool(b))  # Falsy
print(bool(c))  # Truthy
print(bool(d))  # Falsy
print(bool(e))  # Truthy

#Another Example
a=1
b=1.0
print(a==b)
print(a is b)
print(id(a))# they have different ids
print(id(b))
# a and b have the same numeric value but a different type
c=b
print(b==c)
print(b is c)
print(id(b))
print(id(c))
# b and c are equal in value and identity


#Another Example
list_a = [10, 20, 30,]
list_b = [10, 20, 30,]
list_c = list_a


# Check if list_a is the same list as list_b
print( list_a is list_b)

# Check if list_a is equal to list_b
print( list_a == list_b)

# Check if list_a is the same list as list_c
print( list_a is list_c)

#Example
print('Program' in 'Programming')# True
print('spam' in ['spam', 'egg'])#True
print('sausage' not in ['spam', 'egg'])#True
print("robbie" in ["gary", "howard", "mark", "jason"]) #False
#Example
menu = ['eggs', 'bacon', 'spam', 'spam']
print(menu)
print(menu.count('spam'))
print(menu.count('eggs'))
print(menu.index('eggs'))
print(menu.reverse())
print(menu)
print(menu.append('lobster thermidor'))
print(menu)
print(menu.sort())
print(menu)
print(menu.pop())

#Example
# Create a tuple variable named cars
cars = ("Tesla", "BMW", "Ferrari")

# Print the cars variable
print("Cars:", cars)

# Create a variable named get_car and use tuple indexing to pull out the "BMW" value
get_car = cars[1]

# Print the get_car variable
print("Selected Car:", get_car)

# Unpack the cars tuple and assign its values to variables
car_one, car_two, car_three = cars

# Print the unpacked variables
print("Car One:", car_one)
print("Car Two:", car_two)
print("Car Three:", car_three)

######Example
user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
#Returns a list containing a tuple for each key:value pair
#####If we needed access to both keys and values, 
# we’d have to use a dictionary method called .items()
print(user.items())
print(user.get('age', 0))
user.update({'home': 'Withywindle, Middle-Earth'})
print(user)
print(user.popitem())
print(user)
user.clear()
print(user)

##Example
challenger = {
	"name": "Katniss Everdeen",
	"age": 16,
	"district": 12,
	"weapon": "Bow and Arrow", 
	"status": "Victor"
}
# Use the update() method to add a new key-value pair
challenger.update({"occupation": "Hunter"})

# Use the get() method to get the value stored at the "occupation" key
occupation = challenger.get("occupation")

# Print the value of the occupation variable to the terminal
print("Occupation:", occupation)

# Use the update() method to update the value stored at the "age" key
challenger.update({"age": 17})

# Use the pop() method to remove the key-value pair for "status"
challenger.pop("status")

# Print the updated challenger dictionary to the terminal
print(challenger)

#####Example######################## For Dictionary
user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

for key, value in user.items():
    #Returns a list containing a tuple for each key:value pair
#####If we needed access to both keys and values, 
# we’d have to use a dictionary method called .items()
    print(f"Key: {key}")
    print(f"Value: {value}")
    print("------------------")
###Example############################# for set
# Create a set
directions = set(['north', 'south', 'east', 'west'])

# Print its members
for direction in directions:
    print(direction)

# Add an item to the set:
directions.add('northwest')

print()
# Print the members again
# Notice the order cannot be relied upon!
for direction in directions:
    print(direction)