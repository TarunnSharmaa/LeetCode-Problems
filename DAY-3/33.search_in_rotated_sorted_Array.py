# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # Find the pivot element
            if nums[left] <= nums[mid]:
                # Pivot is in the right half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Pivot is in the left half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Find the pivot element
            # right sorted position
            if nums[mid] < nums[right]:
                # Pivot is in the right half
                if target > nums[right] or nums[mid] > target:
                    # then take one step back from right, mid-1
                    right = mid - 1
                else:
                    # if right is really on the right side, move one step forward,  mid +1
                    left = mid + 1

            # left sorted position
            else:
                # Pivot is in the left half
                if target < nums[left] or nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
