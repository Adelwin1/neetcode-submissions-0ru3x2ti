class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ml = 300
        idx = 0
        i = 0

        for a in strs:
            if len(a)<= ml:
                ml = len(a)
                idx = i
            i+=1
        for i in range(ml):
            ch = strs[idx][i]
            for b in strs:
                if ch == b[i]:
                    continue
                elif i ==0:
                    return ""
                else:
                    return b[:i]
        return strs[idx]