class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        some = deque()
        step = 0

        if "0000" in deadends:
            return -1

        some.append("0000")
        visited.add("0000")

        while some:

            # number of states in THIS BFS level
            level_size = len(some)

            for _ in range(level_size):
                d = some.popleft()

                if d == target:
                    return step

                for i in range(len(d)):
                    up = d[:i] + str((int(d[i]) + 1) % 10) + d[i+1:]
                    down = d[:i] + str((int(d[i]) - 1) % 10) + d[i+1:]

                    if up not in visited and up not in deadends:
                        visited.add(up)
                        some.append(up)

                    if down not in visited and down not in deadends:
                        visited.add(down)
                        some.append(down)

            # only after ALL states at this distance are processed
            step += 1

        return -1