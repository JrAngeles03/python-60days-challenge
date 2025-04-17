# Create an empty list
my_list = []

# Ask the user how many items they want to input
num_items = int(input("How many items do you want to add to the list? "))

# Use a loop to input values
for i in range(num_items):
    value = input(f"Enter item {i + 1}: ")  # Take input for each item
    my_list.append(value)  # Add each input value to the list

# Print the resulting list
print("Your list:", my_list)
