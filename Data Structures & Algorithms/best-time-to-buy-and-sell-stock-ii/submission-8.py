from typing import List
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        profit=0

        for i in range(n-1):
            if nums[i+1]> nums[i]:
                profit+= nums[i+1]-nums[i]
            else:
                continue 
        return profit
