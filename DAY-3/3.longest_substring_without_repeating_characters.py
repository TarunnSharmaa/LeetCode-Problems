# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # intuitive approach

        # if not s:
        #     return 0

        # longest_length = 1
        # index = 0

        # while index <= len(s)-1:
        #     char = s[index]
        #     substring = [char]
        #     for j in range(index+1, len(s)):
        #         if char == s[j] or s[j] in substring:
        #             break
                
        #         substring.append(s[j])
        #         longest_length = max(longest_length, len(substring))

        #     index += 1

        # # return the longest length
        # return longest_length


        # optimized approach
        visited = {}
        i = 0
        result = 0
        for j in range(len(s)):
            # If s[j] is already in the visited dictionary,
            # it means we've seen this character before. 
            # Update i to be the maximum of its current value and the index where we last saw s[j].
            # This ensures we don't count the repeated character in our current substring.
            if s[j] in visited:
                i = max(visited[s[j]], i)
            
            # update result to be the maximum of its current value and the length of the current substring
            # without repeating characters (j - i + 1).
            result = max(result, j - i + 1)
            visited[s[j]] = j + 1
        return result