class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack = []
        result = [0]* len(nums)

        for i, temp in enumerate(nums):
            while stack and stack[-1][0] < temp:
                rtemp, rindex = stack.pop()
                result[rindex] = i - rindex
            stack.append((temp, i))
        return result
        

            