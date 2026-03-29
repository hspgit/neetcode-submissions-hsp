class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Use a regular dictionary

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        return [] # Should not reach here based on typical Two Sum problem constraints