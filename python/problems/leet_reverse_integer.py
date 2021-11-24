# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:

# Input: x = 123
# Output: 321

# Runtime: 16 ms, faster than 89.22% of Python online submissions for Reverse Integer.
def solve_leet_reverse_integer(input):
    quotient = input
    out = 0
    if input < 0:
        quotient *= -1
    while(quotient != 0):
        quotient, remainder = divmod(quotient, 10)
        out = (out * 10) + remainder
    if input < 0:
        out *= -1
    ran = pow(2,31)
    if out < ran * -1 or out > ran-1:
        return 0
    return out


