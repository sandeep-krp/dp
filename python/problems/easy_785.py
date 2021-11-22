"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
"""

def solve_875(arr):
    two_smallest_neg = []
    three_largets_pos = []
    for num in arr:
        if num < 0:
            if len(two_smallest_neg) < 3:
                two_smallest_neg.append(num)
            # Sort the 3 element array
            bubble_sort(2,two_smallest_neg)
            # Remove the last element. We are only intereseted in the two smallest integers
            two_smallest_neg.pop(2)
        else:
            if len(three_largets_pos) < 4:
                three_largets_pos.append(num)
                continue



# Fit the value at idx position to its correct position (in the sub array of positive elements which is already sorted)
def bubble_sort(idx, arr):
    # idx reached at the end of the list
    if idx == len(arr)-1:
        return
    if arr[idx] > arr[idx+1]:
        shuffle_with_next(idx,arr)
        bubble_sort(idx+1, arr)

# Shuffle the value at idx with idx+1
def shuffle_with_next(idx, arr):
    temp = arr[idx]
    arr[idx] = arr[idx+1]
    arr[idx+1] = temp