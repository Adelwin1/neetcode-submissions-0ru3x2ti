class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        sm = float('inf')
        bp = 0

        for i in range(len(nums)):
            r = nums[i]
            if r < sm:
                sm = r
            bp = max(bp, (nums[i] - sm))

        return bp