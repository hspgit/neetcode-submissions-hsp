class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n+1):
            var = bin(i).count('1')
            output.append(var)
        
        return output
    