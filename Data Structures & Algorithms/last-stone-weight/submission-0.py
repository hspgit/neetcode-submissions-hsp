class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max-heap by negating values
        # heapq is a min-heap, so we store negative values to simulate a max-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Get the two heaviest stones (most negative values)
            s1 = -heapq.heappop(max_heap) # Convert back to positive for calculation
            s2 = -heapq.heappop(max_heap) # Convert back to positive for calculation

            if s1 == s2:
                continue # Both stones are destroyed
            else:
                remaining_weight = abs(s1 - s2) # The problem implies larger - smaller
                # Push the remaining weight back into the heap as a negative value
                heapq.heappush(max_heap, -remaining_weight)
        
        # After the loop, if there's one stone left, return its positive weight.
        # Otherwise, if the heap is empty, return 0.
        return -max_heap[0] if max_heap else 0