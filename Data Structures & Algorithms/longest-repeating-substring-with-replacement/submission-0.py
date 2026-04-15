class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        mf = 0
        result = 0
        n = len(s)
        for right in range(n):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            mf = max(mf, count[char])
            while (right-left+1)-mf > k:
                count[s[left]]-=1
                left+=1
            result = max(mf, right-left+1)
        return result


    

        