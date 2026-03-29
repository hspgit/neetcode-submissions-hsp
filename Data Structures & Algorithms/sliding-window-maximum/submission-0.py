class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        l, r = 0, k-1

        while r < n:
            res.append(max(nums[l:r+1]))
            l += 1
            r += 1
        
        return res