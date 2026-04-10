# Author: James Harris
# GitHub username: thestackman
# Date: 04102026
# Description:  Compute and return all values that factor into a user inputted integer.

# Get user input for starting int
starting_int = int(input("Please enter a positive integer: "))

# Calculate and print all factors
print(f"The factors of {starting_int} are:")

max_factor = starting_int // 2

for i in range(1, max_factor + 1):
    if starting_int%i == 0:
        print(i)

print(starting_int) #An integer will always be a factor of itself