class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            indegree[pre] += 1
            graph[crs].append(pre)
        
        zeros = [i for i in range(numCourses) if  not indegree[i]]
        if not zeros:
            return False
        q = deque(zeros)
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses



