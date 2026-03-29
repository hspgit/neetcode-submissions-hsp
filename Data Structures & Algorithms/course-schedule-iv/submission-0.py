from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 1. Standard Adjacency List: Prereq -> Course
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[pre].append(crs)
        
        # 2. isReached[u] will store ALL courses that have 'u' as a prerequisite
        isReached = [set() for _ in range(numCourses)]
        
        # 3. DFS to propagate prerequisites forward
        memo = [False] * numCourses
        
        def dfs(curr):
            if memo[curr]:
                return isReached[curr]
            
            for neighbor in adj[curr]:
                # The neighbor is a direct descendant
                isReached[curr].add(neighbor)
                # All descendants of the neighbor are also descendants of curr
                isReached[curr].update(dfs(neighbor))
                
            memo[curr] = True
            return isReached[curr]

        # Pre-calculate for all nodes
        for i in range(numCourses):
            dfs(i)
            
        # 4. Answer queries in O(1)
        return [v in isReached[u] for u, v in queries]