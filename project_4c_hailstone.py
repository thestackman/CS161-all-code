# Author: James Harris
# GitHub username: thestackman
# Date: 04222026
# Description: Function that returns the number of Hailstone function steps required to reach the value 1 based on user input.


def hailstone(number):
    """Function that returns hailstone steps to reach 1 based on integer user input"""

    steps = 0

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            steps += 1
        else:
            number = number * 3 + 1
            steps += 1

    return steps


# user_int = int(input("Enter int: "))
# hs_pos = hailstone(user_int)
# print(hs_pos)