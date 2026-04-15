from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        left = [1]*n
        l = 1

        for i in range(n):
            left[i] = l
            l*= nums[i]

        r = 1
        for i in range(n-1, -1, -1):
            left[i]*= r
            r*= nums[i]

        return left
            

