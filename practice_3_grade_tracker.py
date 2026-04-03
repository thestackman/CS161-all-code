# Author: James Harris
# GitHub username: thestackman
# Date: 20260403
# Description:  Calculates average and running total of test scores,
#               then prints report against target score.

# Constants
NUMBER_OF_SCORES = 3

# Initialize
score_total = 0.0

# Get user input
score_1 = float(input("Enter score 1: "))
score_total += score_1
score_2 = float(input("Enter score 2: "))
score_total += score_2
score_3 = float(input("Enter score 3: "))
score_total += score_3
score_target = float(input("Enter target score: "))

# Compute values
score_avg = score_total/NUMBER_OF_SCORES
score_distance = abs(score_target - score_avg)

# Print output
print()
print("--- Grade Report ---")
print(f"Scores entered: {score_1}, {score_2}, {score_3}")
print("Running total: " + str(score_total))
print(f"Average: {score_avg:,.2f}")
print(f"Distance from target: {score_distance:,.2f}")
print("Data type of average: " + str(type(score_avg)))