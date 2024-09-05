# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Time Complexity --> O(n)
# python code

class Solution:

    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.''
        """

        start = 0
        end = len(s)-1

        while start <= end :
            tmp = s[start]
            s[start] = s[end]
            s[end]= tmp
            start+=1
            end-=1