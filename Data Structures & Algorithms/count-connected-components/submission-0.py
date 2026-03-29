class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        count = 0
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count