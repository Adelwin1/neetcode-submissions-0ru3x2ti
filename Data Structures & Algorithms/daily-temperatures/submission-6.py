class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        result = [0]* len(nums)
        stack = []

        for i, temp in enumerate(nums):
            while stack and stack[-1][0] < temp:
                rtemp, rindex = stack.pop()
                result[rindex] = i - rindex
            stack.append((temp, i))
        return result
        

            
                
            
        