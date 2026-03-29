class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = Counter(s)
        t_c = Counter(t)

        return True if s_c == t_c else False