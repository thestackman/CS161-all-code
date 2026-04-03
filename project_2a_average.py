# Author: James Harris
# GitHub username: thestackman
# Date: 3/31/2026
# Description: Ask the user for five numbers then display the average.

# Constant
NUM_OF_INPUTS = 5

# Init
user_input_total = 0

# Get user input
print("Please enter five numbers.")
user_input_total += float(input())
user_input_total += float(input())
user_input_total += float(input())
user_input_total += float(input())
user_input_total += float(input())

# Calculate the average
user_input_avg = user_input_total / NUM_OF_INPUTS

print("The average of those numbers is:")
print(user_input_avg)