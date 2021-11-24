# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Runtime: 96 ms, faster than 31.62% of Python online submissions for Longest Substring Without Repeating Characters.
def leet_longest_substring_without_repeating_characters(s):
    longest_substring = ""
    longest_substring_len = 0
    for i in range(len(s)):
        x = s[i]
        if x in longest_substring:
            longest_substring = longest_substring[longest_substring.find(x)+1:]
        longest_substring += x
        longest_substring_len = max(len(longest_substring),longest_substring_len)
    return longest_substring_len


