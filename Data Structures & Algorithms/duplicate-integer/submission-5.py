class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)

        return False if len(nums) == len(num_set) else True