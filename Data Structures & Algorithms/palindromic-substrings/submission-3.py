class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):

            for j in range(2):
                l, r = i, i + j
                while l >=0 and r < n and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1    
            # odd len
            # l, r = i, i
            # while l >=0 and r < n and s[l] == s[r]:
            #     res += 1
            #     l -= 1
            #     r += 1
            
            # # even len
            # l, r = i, i + 1
            # while l >=0 and r < n and s[l] == s[r]:
            #     res += 1
            #     l -= 1
            #     r += 1
            
        return res