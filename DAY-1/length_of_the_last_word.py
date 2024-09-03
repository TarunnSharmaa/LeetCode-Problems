# https://leetcode.com/problems/length-of-last-word/
# python code solution
# Time complexity --> O(n)

class Solution:

    def lengthOfLastWord(self, s: str) -> int:

        # reverse the string
        reverse_Str=s[::-1]
        reverse_Str=reverse_Str.strip()
        last_word=""

        for i in range(len(reverse_Str)):
            # Once you find empty space, it means word has ended, Hence return
            if reverse_Str[i]==" ":
                return len(last_word)
            else:
                last_word+=reverse_Str[i]
        return len(last_word)