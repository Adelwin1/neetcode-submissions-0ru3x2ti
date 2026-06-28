class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1= len(nums1)
        n2 = len(nums2)
        ans = [0]* (n1+n2)
        p1 = 0
        p2 = 0
        i = 0
        while p1< n1 and p2<n2:
            if nums1[p1]< nums2[p2]:
                ans[i] = nums1[p1]
                i+=1
                p1+=1
            elif nums1[p1]== nums2[p2]:
                ans[i] = nums1[p1]
                ans[i+1] = nums2[p2]
                i+=2
                p1+=1
                p2+=1
            else:
                ans[i] = nums2[p2]
                i+=1
                p2+=1
        while p1 < n1:
            ans[i]= nums1[p1]
            i+=1
            p1+=1
        while p2<n2:
            ans[i] = nums2[p2]
            i+=1
            p2+=1
        
        c = len(ans)
        if c %2 ==0:
            o = (c-1)//2
            v = c//2
            return (ans[o]+ ans[v])/2
        else:
            o = c//2
            return ans[o]

            




        