
class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        smallest = float('inf')
        n = len(nums)
        profit = 0

        for i in range(n):
            if nums[i]< smallest:
                smallest = nums[i]
                ind = i
            new = nums[i]- nums[ind]
            profit = max(new, profit)

        return profit 
        