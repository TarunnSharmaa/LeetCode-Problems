# https://leetcode.com/problems/find-missing-observations/description/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        # Calculate the total sum of all the dice rolls based on the given mean
        total_dice_rolls = (len(rolls) + n) * mean
        # Calculate the sum of the missing rolls by subtracting the sum of existing rolls
        sum_missing_rolls = total_dice_rolls - sum(rolls)
      
        # If the sum of the missing rolls is not between n and 6n, it's impossible to get such a sequence
        if sum_missing_rolls > n * 6 or sum_missing_rolls < n:
            return []
      
        # Start with an even distribution of the sum across all the missing rolls
        missing_rolls = [sum_missing_rolls // n] * n
      
        # Distribute the remainder among the first (remainder) rolls, adding 1 to each
        for i in range(sum_missing_rolls % n):
            missing_rolls[i] += 1
      
        # Return the final list of missing rolls
        return missing_rolls



