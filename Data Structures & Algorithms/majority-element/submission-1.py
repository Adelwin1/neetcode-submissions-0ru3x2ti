from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        
        for num in nums:

            if num in count:
                count[num]+=1
            else:
                count[num] = 1

        mc = 0
        big = None

        for num in count:
            if count[num]> mc:
                mc = count[num]
                big = num
        return big
       