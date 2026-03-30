class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = [0] * (n+1)
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        q = deque([i for i in range(1, n+1) if indegree[i] == 1])

        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        
        return []
            
        
