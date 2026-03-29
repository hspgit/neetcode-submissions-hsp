class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, val in enumerate(nums):
            check = target - val
            if check in num_to_index:
                return [num_to_index[check], i]
            
            num_to_index[val] = i
        
