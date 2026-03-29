class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = int(n*(n+1)/2)
        su = sum(nums)
        return expected - su