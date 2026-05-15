class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        n1 = m+n
        r = m-1
        e2 = len(nums2)-1
        e1 = len(nums1)-1

        while r>=0:
            if e2 <0:
                break
            if nums1[r]> nums2[e2]:
                nums1[e1], nums1[r] = nums1[r], nums1[e1]
                r-=1
                e1-=1
            else:
                nums1[e1] = nums2[e2]
                e2-=1
                e1-=1
        for i in range(e2+1):
            nums1[i] = nums2[i]
        



