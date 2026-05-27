class Solution:
    def decodeString(self, s: str) -> str:
        curr = ""
        stack = []
        num = 0
        n = len(s)
        i = 0

        while i< n:
            while i<n and s[i]== ']':
                stuff, times = stack.pop()
                curr = stuff + curr*times
                i+=1
            if i ==n:
                return curr
            if not s[i].isdigit():
                curr+= s[i]
                i+=1
            else:
                while i<n and s[i]!= '[' :
                    num = num *10 + int (s[i])
                    i+=1
                stack.append((curr, num))
                num = 0
                curr = ""
                i+=1
        return curr