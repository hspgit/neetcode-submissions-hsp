class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, curr_surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            curr_surplus += gas[i] - cost[i]
            if curr_surplus < 0:
                curr_surplus = 0
                start = i + 1
        return start if (total_surplus >= 0) else -1