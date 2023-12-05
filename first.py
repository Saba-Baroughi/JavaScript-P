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
