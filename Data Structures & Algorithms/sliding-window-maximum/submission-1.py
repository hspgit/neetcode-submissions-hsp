class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     res = []

    #     l, r = 0, k-1

    #     while r < n:
    #         res.append(max(nums[l:r+1]))
    #         l += 1
    #         r += 1
        
    #     return res # O(m*k)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output # O(nlogn)