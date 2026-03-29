class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        
        # 1. Map dependencies
        for crs, pre in prerequisites:
            adj[pre].append(crs) # pre unlocks crs
            indegree[crs] += 1
            
        # 2. Queue the "Free" courses
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    
        return True if len(order) == numCourses else False


