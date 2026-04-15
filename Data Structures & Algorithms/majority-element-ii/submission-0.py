from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        count = Counter(nums)

        for k, v in count.items():
            if v > n/3:
                result.append(k)
        return result

        