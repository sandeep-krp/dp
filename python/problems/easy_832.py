"""
    Given an array of elements, return the length of the longest subarray where all, 
    its elements are distinct.

    For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest 
    subarray of distinct elements is [5, 2, 3, 4, 1]

"""

def solve_easy_832(arr):
    full_size = len(arr)
    window_size = full_size
    while(window_size != 1):
        for j in range(0,full_size-(window_size-1)):
            sub_arr = arr[j:window_size+j]
            if is_array_unique(sub_arr) == True:
                return sub_arr
        window_size-=1
    print("All elements are the same")
    return arr[0]


def is_array_unique(arr):
    if len(arr) == len(set(arr)):
        return True
    return False

