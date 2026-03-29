# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         strs.sort(key = lambda x: len(x))
#         prefix = strs[0]

#         for i in range(1, len(strs)):
#             loop = min(len(prefix), len(strs[i]))
#             if loop == 0:
#                 return ""
            
#             for j in range(loop):  
#                 if prefix[j] != strs[i][j]:
#                     prefix = prefix[:j]
#                     break
        
#         return prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]