class Solution:
    def carFleet(self, target: int, p: List[int], s: List[int]) -> int:
        n = len(p)
        ps = []
        stack = []

        for i in range(n):
            time = (target- p[i])/ s[i]
            ps.append((p[i], time))
        
        ps.sort(reverse = True)

        for stuff in ps:
            if not stack:
                stack.append(stuff[1])
            if stuff[1] <= stack[-1]:
                continue
            else:
                stack.append(stuff[1])
        return len(stack)



        