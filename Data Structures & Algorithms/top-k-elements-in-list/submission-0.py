class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        
        top = []

        for num, freq in num_count.items():
            heapq.heappush(top, [freq, num])
            if len(top) > k:
                heapq.heappop(top)
        
        res = [item[1] for item in top]

        return res

