# Author: James Harris
# GitHub username: thestackman
# Date: 04292026
# Description: Returns list without duplicates


def without_duplicates(list_of_stuff):
    """Function that removes duplicates from a list and returns it"""

    stuff_deduped = []

    for stuff in list_of_stuff:
        if stuff not in stuff_deduped:
            stuff_deduped = stuff_deduped + [stuff]

    return stuff_deduped

# stuff = [8, 'hello', 8, True, -1000000.4, 'hello', 8]
# result = without_duplicates(stuff)
# print(result)