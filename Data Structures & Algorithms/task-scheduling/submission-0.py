import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task = Counter(tasks)
        heap = [-man for man in task.values()]
        heapq.heapify(heap)
        cooldown = deque()
        time = 0

        while heap or cooldown:
            time+=1

            if heap:
                cnt = heapq.heappop(heap)+1
                
                if cnt!=0:
                    cooldown.append((time+n, cnt))

            if cooldown and cooldown[0][0]==time:
                l, cnt = cooldown.popleft()
                heapq.heappush(heap, cnt)
        return time 

                

        
        