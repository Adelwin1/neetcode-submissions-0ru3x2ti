class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        kofi = set(nums)

        for num in kofi:
            if num-1 not in kofi:
                current = num
                length = 1

                while current+ 1 in kofi:
                    current+=1
                    length+=1
                longest = max(longest, length)
        return longest
        