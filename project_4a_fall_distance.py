# Author: James Harris
# GitHub username: thestackman
# Date: 04222026
# Description: Function that returns fall distance based on a given time.

GRAVITY = 9.8


def fall_distance(time):
    """Function returns the distance in meters an object falls based on the parameter time in seconds"""
    distance = 0.5 * GRAVITY * time ** 2
    return distance

# # Get user input
# fall_time = float(input("Enter the time to fall distance: "))
#
# # Call function and print result
# final_distance = fall_distance(fall_time)
# print(final_distance)