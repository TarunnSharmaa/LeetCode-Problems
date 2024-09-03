# https://leetcode.com/problems/excel-sheet-column-number/

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        # Initialize the result to 0
        result = 0

        # Iterate through each character in the column title
        for char in columnTitle:
            # Convert the character to a number (A=1, B=2, ..., Z=26)
            character_count = ord(char) - ord("A") + 1

            # shift the previous result by multiplying by 26 (since it's base 26)
            # for example --> AAB --> (0 +1) --> ((1)*26 + 1) --> ((27)*26 + 2)
            result = result * 26 + character_count

        # Return the final numerical result
        return result


