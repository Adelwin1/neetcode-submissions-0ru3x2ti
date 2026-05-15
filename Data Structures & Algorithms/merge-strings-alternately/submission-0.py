class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1, n2)
        p1 =0
        p2 =0
        result = ""
        for i in range (n):
            result+= word1[p1]
            p1+=1
            result+= word2[p2]
            p2+=1
        while p1 < n1:
            result+= word1[p1]
            p1+=1
        while p2 <n2:
            result+= word2[p2]
            p2+=1
        return result
