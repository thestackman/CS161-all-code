# Author: James Harris
# GitHub username: thestackman
# Date: 04292026
# Description: Function that takes a list of numbers and returns median.


def find_median(nums):
    """Function that returns the median of parameter nums"""

    nums_len = len(nums)
    sorted_nums = sorted(nums)

    # List length is even
    if nums_len % 2 == 0:
        term1 = sorted_nums[nums_len // 2 - 1]
        term2 = sorted_nums[nums_len // 2]
        median = (term1 + term2) / 2
        return median

    # List length is odd
    else:
        median = sorted_nums[nums_len // 2]
        return median

some_nums = [1, 2]
result = find_median(some_nums)
print(result)