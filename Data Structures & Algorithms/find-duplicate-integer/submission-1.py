class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for i, v in counts.items():
            if v > 1:
                return i
        
        # n = len(nums)
        
        # sorted_nums = sorted(nums)

        # print(sorted_nums)

        # for i in range(len(sorted_nums)):
        #     if sorted_nums[i] != i + 1:
        #         return i