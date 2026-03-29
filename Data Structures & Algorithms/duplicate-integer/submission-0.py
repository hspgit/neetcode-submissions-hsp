class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counter = Counter(nums)

        for k, v in num_counter.items():
            if v > 1:
                return True
        
        return False