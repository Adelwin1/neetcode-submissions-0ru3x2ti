class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count =0
        freq = {0:1}
        total = 0

        for num in nums:
            total+= num
            after = total - k
            
            count+= freq.get(after, 0)
            freq[total] = freq.get(total, 0)+1
        return count 

        