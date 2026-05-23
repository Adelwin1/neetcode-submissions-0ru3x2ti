class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack = []

        for x in a:
            alive = True

            while alive and x < 0 and stack and stack[-1] > 0:
                if abs(stack[-1]) < abs(x):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(x):
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(x)

        return stack