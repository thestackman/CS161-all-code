# Author: James Harris
# GitHub username: thestackman
# Date: 04102026
# Description:  Get user input for number of integers, get the individual integers, compute and print the min and max.

# Get user input and track min and max values
print("How many integers would you like to enter?")
num_of_int = int(input())
print(f"Please enter {num_of_int} integers.")

int_to_test = int(input())
min_value = int_to_test
max_value = int_to_test

for i in range(2, num_of_int+1):
    int_to_test = int(input())
    if int_to_test > max_value:
        max_value = int_to_test
    if int_to_test < min_value:
        min_value = int_to_test

# Print min/max values
print(f"min: {min_value}")
print(f"max: {max_value}")

