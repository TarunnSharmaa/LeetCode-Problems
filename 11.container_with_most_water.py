# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # brute force method
        # from each line calculate the area by moving over each line
        # update max area for each iteration

        # max_area = 0
        # n = len(height)
        
        # for i in range(n):
        #     for j in range(n, i, -1):
        #         h = height[i] if height[i] < height[j] else height[j]
        #         w = j - i
        #         area = h * w
                
        #         if area > max_area:
        #             max_area = area
        
        # return max_area


        # use two pointer technique to optimize the solution

        p1 = 0
        p2 = len(height) - 1
        max_area = 0

        while (p1 < p2):
            curr_height = height[p1] if height[p1] < height[p2] else height[p2]
            width = p2 - p1

            area = width * curr_height

            if area > max_area:
                max_area = area
            else:
                if height[p1] < height[p2]:
                    p1 += 1
                else:
                    p2 -= 1
        
        return max_area


        