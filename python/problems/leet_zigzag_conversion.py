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

def solve(s,numRows):
    r = get_no_of_row(s,numRows)


def get_no_of_row(s,numRows):
    print('Lengh of input [{}]'.format(len(s)))
    noOfMidCols = (numRows-2)
    divider = numRows + noOfMidCols
    div_out = len(s)/divider
    rem = len(s)% divider
    no_of_grid_cols = (div_out * (noOfMidCols+1))+ rem/numRows + (rem % numRows if rem >= numRows else (1 if rem > 0 else 0))
    print('No of grid_columns [{}]'.format(no_of_grid_cols))
# WIP FIXME
solve('ABCDEFGHIJK',4)




