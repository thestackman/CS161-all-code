# Author: James Harris
# GitHub username: thestackman
# Date: 20260326
# Description:  Get a temp input in Celsius from user, convert to Fahrenheit and print.

# Get user input
print("Please enter a Celsius temperature.")
temp_c = float(input())

# Calculate Celsius to Fahrenheit
temp_f = temp_c * 9 / 5 + 32

# Print Fahrenheit
print("The equivalent Fahrenheit temperature is:")
print(temp_f)