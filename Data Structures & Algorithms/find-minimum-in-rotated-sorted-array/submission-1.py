class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left<=right:
            small = min(nums[left], nums[right])

            if small == nums[left]:
                right-=1
            else:
                left+=1
        return small 


            
            

