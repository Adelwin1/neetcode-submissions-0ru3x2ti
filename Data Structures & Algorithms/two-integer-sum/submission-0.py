class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        some = {}
        for i, num in enumerate(nums):
            compliment = target-num
            if compliment in some:
                return [some[compliment], i]
            some[num] = i
        return []

        