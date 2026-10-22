class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        mc = 0
        for num in  n:
            if num-1 in n:
                continue 
        
            count= 1
            start = num
            while start+1 in n:
                start = start+1
                count+=1

            mc = max(mc, count )

        return mc