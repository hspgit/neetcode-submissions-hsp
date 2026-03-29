# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         count = Counter(tasks)
#         maxHeap = [ -cnt for cnt in count.values()]
#         heapq.heapify(maxHeap)

#         time = 0
#         q = deque() # pait of [-cnt, idleTime]

#         while maxHeap or q:
#             time += 1

#             if maxHeap:
#                 cnt = 1 + heapq.heappop(maxHeap)
#                 if cnt:
#                     q.append([cnt, time + n])
            
#             if q and q[0][1] == time:

#                 heapq.heappush(maxHeap, q.popleft()[0])
        
#         return time

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort()
        maxf = count[25]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle -= min(maxf - 1, count[i])
        return max(0, idle) + len(tasks)