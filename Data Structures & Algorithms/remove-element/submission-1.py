class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        for num in nums:
            if num != val:
                res.append(num)
        
        for i in range(len(res)):
            nums[i] = res[i]
        return len(res)