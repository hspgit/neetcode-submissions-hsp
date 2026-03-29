class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            dp[i] represent the min number of coins needed to for amount 'i'
            so for each coin we have amounts form coin -to- amount where each one has a choice to chose coin of not
            dp[i] is min of dp[i-coin] + 1(we chose the coin) and dp[i] we did not choses the coin 
        '''
      
        dp = [math.inf] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], 1 + dp[i-coin])
        
        # dp[amount] will be some number if we found a valid combination
        print(dp)
        if dp[amount] != math.inf:
            return dp[amount]
        else:
            return -1

    
