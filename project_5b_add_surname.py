# Author: James Harris
# GitHub username: thestackman
# Date: 04292026
# Description: Function that is absurd.


def add_surname(names):
    """Function that adds a surname to all given names that start with K"""

    k_names = [name + " Kardashian" for name in names if name[0] == "K"]
    return k_names

# some_names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
# result = add_surname(some_names)
# print(result)