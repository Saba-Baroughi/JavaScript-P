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