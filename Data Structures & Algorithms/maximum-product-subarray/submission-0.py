class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far , min_so_far, result = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            prod1, prod2 = nums[i] * max_so_far, nums[i] * min_so_far
            max_so_far = max(prod1, prod2, nums[i])
            min_so_far = min(prod1, prod2, nums[i])
            
            result = max(max_so_far, result)

        return result