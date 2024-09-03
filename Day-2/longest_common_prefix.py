#  https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        lcp = ""

        # prepare a string to compare each characters from
        stc = strs[0]

        for i in range(0, len(stc)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or stc[i] != strs[j][i]:
                    return lcp
            lcp += stc[i]
        
        return lcp