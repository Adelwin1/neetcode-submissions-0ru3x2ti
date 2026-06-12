class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        ans = 0
        lo = 0

        for a in s:
            if a not in seen:
                seen.add(a)
                lo = len(seen)
            else:
                while a in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(a)
                lo = len(seen)

            ans = max(ans, lo)
        
        return ans 


        
                