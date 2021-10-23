"""
A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False
"""


def solve_easy_821(arr):
    for x in arr:
        if x >=0 and x < len(arr) and arr[x] == x:
            return x
    return False