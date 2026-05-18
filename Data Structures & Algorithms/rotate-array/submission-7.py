from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        if k >= n:
            k = k%n
        p1 = 0 
        p2 = n-1

        while p1<=p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1
            p2-=1
        p1 = 0
        p2 = k-1

        while p1<=p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1
            p2-=1
        p1 = k
        p2 = n-1
        while p1<=p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1
            p2-=1
