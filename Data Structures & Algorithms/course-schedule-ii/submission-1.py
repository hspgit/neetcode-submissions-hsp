class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Build the graph correctly: pre -> crs
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs) # pre points to the course it unlocks
            indegree[crs] += 1     # crs now has one more dependency
        
        # 2. Find all courses with NO prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            
            # 3. "Take" the course and reduce indegree of its neighbors
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        # 4. If we couldn't take all courses, there's a cycle
        return res if len(res) == numCourses else []