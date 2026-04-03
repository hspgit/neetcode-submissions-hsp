class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = true if the substring s[i..j] is a palindrome
        n = len(s)
        res_len, res_id = 0, 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > res_len:
                        res_len = j-i+1
                        res_id = i
        
        return s[res_id:res_id+res_len]