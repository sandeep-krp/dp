"""
Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3
"""


def solve_easy_714(head):
    to_return = head.next
    if (head.next is None):
        return head
    else:
        solve(head)
    return to_return

def solve(head):
    if head.next is None:
        return
    elif head.next.next is None:
        swap_with_next(head)
        return
    next_to_swap = head.next.next
    swap_with_next(head)
    solve(next_to_swap)

def swap_with_next(head):
    if head.next.next is None:
        second = head.next
        second.next = head
        second.next.next = None
    else:
        third = head.next.next
        temp = head.next
        temp.next = head
        temp.next.next = third
        a = head
