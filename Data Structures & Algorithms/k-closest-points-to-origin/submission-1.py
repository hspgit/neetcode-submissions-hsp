class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        maxHeap = []

        for i, v in enumerate(points):
            dist = v[0]**2 + v[1]**2
            heapq.heappush(maxHeap, [-dist, i])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        for some in maxHeap:
            res.append(points[some[1]])
        
        return res
