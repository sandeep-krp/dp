"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81]
"""



def solve_easy_825(in_arr):
    # arr becomes the squared array where all elements are squared
    arr = list(map(lambda x: x**2,in_arr))
    max_neg_idx = find_local_min(arr,0,len(arr)-1)
    while max_neg_idx >= 0:
        bubble_sort(max_neg_idx,arr)
        max_neg_idx -=1
    return arr

# Find the index of the element having value < 0
def find_local_min(arr,start,end):
    if (start+end) % 2 == 0:
        mid_idx = (start+end)//2
    else:
        mid_idx = (start+end+1)//2
    if arr[mid_idx-1] > arr[mid_idx] and arr[mid_idx+1] > arr[mid_idx]:
        # Found local minimum
        return mid_idx
    elif arr[mid_idx-1] < arr[mid_idx] and arr[mid_idx+1] > arr[mid_idx]:
        # The current, last and next values are in increasing order. Move left.
        return find_local_min(arr,start,mid_idx)
    else:
        # The current, last and next values are in decreasing order. Move right.
        return find_local_min(arr,mid_idx,end)

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