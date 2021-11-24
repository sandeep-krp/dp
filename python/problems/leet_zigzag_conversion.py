# he string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

def solve_leet_zigzag_conversion(s,numRows):
    return solve(s,numRows)

# Faster than 80% of submissions
def solve(inputString,numRows):
    if numRows == 1:
        return inputString
    j = 0
    climbing = False
    rows = [""] * numRows
    inc = 1
    for c in inputString:
        rows[j] += c
        j += inc
        if j == 0 or j == numRows-1:
            inc *= -1
    out = ""
    for k in range(numRows):
        out += rows[k]
    return out
