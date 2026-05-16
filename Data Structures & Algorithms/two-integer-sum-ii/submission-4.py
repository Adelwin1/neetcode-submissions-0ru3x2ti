
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        p1 = 0
        n = len(nums)

        while p1< n:
            p2 = p1+1
            while p2<n:
                got = nums[p1]+nums[p2]
                if got == target:
                    result.append(p1+1)
                    result.append(p2+1)
                    return result
                else:
                    p2+=1
            p1+=1
        return result

            
        