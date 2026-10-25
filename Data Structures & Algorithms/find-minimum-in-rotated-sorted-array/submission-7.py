class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        before =nums[l]
        


        while l<r:
            if nums[l]>=nums[r]:
                before = nums[r]
                r-=1  
            else:
                return before
        return before
        