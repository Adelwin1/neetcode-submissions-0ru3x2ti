class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen ={}
        for i, num in enumerate(nums):
            c = target - nums[i]
            if c in seen:
                return [seen[c], i]
            seen[num]= i