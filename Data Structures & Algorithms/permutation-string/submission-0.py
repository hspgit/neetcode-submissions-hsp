class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        s1_c = Counter(s1)

        l, r = 0, n1-1

        while r < len(s2):
            s2_c = Counter(s2[l:r+1])
            if s1_c == s2_c:
                return True
            l += 1
            r += 1
        
        return False
        