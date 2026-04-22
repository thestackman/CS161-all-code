# Author: James Harris
# GitHub username: thestackman
# Date: 04222026
# Description: Function that returns a number at a given position of the Fibonacci sequence.


def fib(pos):
    """Returns the Fibonacci value at position pos"""

    if pos == 1:
        fib_val = 1
    else:
        back_two = 0
        back_one = 1

        for i in range(2, pos + 1):
            fib_val = back_one + back_two
            back_two = back_one
            back_one = fib_val

    return fib_val


# user_int = int(input("Enter int: "))
# fib_at_pos = fib(user_int)
# print(fib_at_pos)