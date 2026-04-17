class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        set(nums)
        seen = set()
        small = float('inf')
        smaller = float('inf')

        for num in nums:
            if num<=0:
                continue
            if num <small:
                small = num
            if num+1 not in nums:
                seen.add(num)
        if small !=1 :
            return 1
        else:
            for a in seen:
                if a < smaller:
                    smaller = a
            return smaller+1


            
        
                
            

            
                    