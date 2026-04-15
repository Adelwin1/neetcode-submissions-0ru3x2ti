from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def sorter(nums, low, high):
            if low < high:
                mid = (low + high) // 2
                sorter(nums, low, mid)
                sorter(nums, mid + 1, high)
                mainsort(nums, low, mid, high)

        def mainsort(nums, low, mid, high):
            leftones = nums[low:mid+1]
            rightones = nums[mid+1:high+1]

            a = 0
            b = 0
            k = low

            while a < len(leftones) and b < len(rightones):
                if leftones[a] <= rightones[b]:
                    nums[k] = leftones[a]
                    a += 1
                else:
                    nums[k] = rightones[b]
                    b += 1
                k += 1

            while a < len(leftones):
                nums[k] = leftones[a]
                a += 1
                k += 1

            while b < len(rightones):
                nums[k] = rightones[b]
                b += 1
                k += 1

        sorter(nums, 0, len(nums) - 1)
