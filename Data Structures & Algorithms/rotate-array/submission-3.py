from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n 
        if k == 0:
            return
        def h(s:int, e:int):
            while s<e:
                nums[s], nums[e]= nums[e], nums[s]
                s+=1
                e-=1
        
        h(0, n-1)
        h(0, k-1)
        h(k, n-1)

        
       