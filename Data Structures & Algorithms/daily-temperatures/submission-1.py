class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n):
            j = i+1
            k = 0
            while j<n:
                if nums[j]<= nums[i]:
                    k+=1
                    j+=1
                else:
                    result.append(k+1)
                    break
            if j ==n and nums[j-1]<= nums[i]:
                result.append(0)
        return result
            
                
            
        