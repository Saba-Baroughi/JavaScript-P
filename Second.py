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
