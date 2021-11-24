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

def solve(inputString,numRows):
    if numRows == 1:
        return inputString
    m = {}
    i = j = 0
    climbing = False
    for c in inputString:
        m[str(i)+','+str(j)] = c
        if not climbing:
            if j == numRows -1 :
                climbing = True
                i = i+1
                j -= 1
            else:
                j += 1
        else:
            if j == 0:
                climbing = False
                j = j+1
            else:
                i += 1
                j -= 1

                # i does not change
    out = ""
    for y in range(numRows):
        for x in range(i+1):
            key = str(x)+','+str(y)
            if key in m:
                out = out + m[key]
    return out
