class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l,r = 0, n-1

        while l<=r:
            mid = (l+r)//2
            ans = nums[mid]

            if ans == target:
                return mid
            
            elif ans< target:
                l = mid+1
            else:
                r = mid - 1
        if nums[mid]< target:
            return mid+1
        else:
            return mid
        

        