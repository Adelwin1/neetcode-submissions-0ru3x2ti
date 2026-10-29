class Solution:
    def validPalindrome(self, s: str) -> bool:
        def h(left, right):
            while left <right:
                while left<right and not s[l].isalnum():
                    left+=1
                while left<r and not s[right].isalnum():
                    right-=1
                if s[left].lower()!= s[right].lower():
                    return False
                left+=1
                right-=1
            return True 

        n = len(s)
        l, r = 0, n-1
        k = 1

        while l <r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()!= s[r].lower():
                return (h(l+1, r) or h(l, r-1))
            l+=1
            r-=1
        return True 

                

        