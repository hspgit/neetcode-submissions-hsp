class Solution:
    def isValid(self, s: str) -> bool:
        bd = {'{': '}', '(':')', '[':']'}
        heap = []

        for c in s:
            if c in bd:
                heap.append(c)
            else:
                if not len(heap):
                    return False
                val = heap.pop()
                if c != bd[val]:
                    return False
        
        return True if not len(heap) else False