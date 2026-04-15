from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # handle k > n
        if k == 0:
            return
        
        # Helper function to reverse a segment in-place
        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Step 1: reverse the whole array
        reverse(0, n - 1)
        
        # Step 2: reverse the first k elements
        reverse(0, k - 1)
        
        # Step 3: reverse the remaining n-k elements
        reverse(k, n - 1)
