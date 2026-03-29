class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         res = max(res, prices[j]- prices[i])
        
        # return res

        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] < prices[r]: # profitable condition
                curr =  prices[r] - prices[l]
                res = max(res, curr)
            else:
                l = r
            r += 1
        
        return res