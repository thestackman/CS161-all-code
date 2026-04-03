# Author: James Harris
# GitHub username: thestackman
# Date: 20260326
# Description:  Calculates distance and temp conversions,
#               then prints results.

# Constants
KM_PER_MILE = 1.60934 #km per Mile
FEET_PER_MILE = 5280
INCH_PER_FOOT = 12 #inches per foot

# Get user input
distance_miles = float(input("Enter a distance in miles: "))
temp_f = float(input("Enter a temperature in Fahrenheit: "))

# Compute values
distance_km = distance_miles * KM_PER_MILE
feet_total = distance_miles * FEET_PER_MILE
inches_total = feet_total * INCH_PER_FOOT
temp_c = (temp_f - 32) * 5/9

# Print user output
print("--- Distance Conversions ---")
print(f"Miles: {distance_miles:,.2f}")
print(f"Kilometers: {distance_km:,.2f}")
print(f"Feet: {feet_total:,.2f}")
print(f"Inches: {inches_total:,.2f}")
print("--- Temperature Conversion ---")
print(f"Fahrenheit: {temp_f:,.1f}")
print(f"Celsius: {temp_c:,.1f}")