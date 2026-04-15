class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        s = []
        n = len(t)
        output = [0]*n
        for i in range(n):
            while s and t[i]> t[s[-1]]:
                d = s.pop()
                output[d]= i-d
            s.append(i)
        return output
        
                