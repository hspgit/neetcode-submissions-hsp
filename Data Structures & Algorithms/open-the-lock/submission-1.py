class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"

        if start in dead:
            return -1
        if start == target:
            return 0
        
        q = deque()
        q.append((start, 0))
        visited = set()
        visited.add(start)

        while q:
            state, move = q.popleft()

            for i in range(4):
                digit = int(state[i])
                for delta in (-1, 1):
                    new_digit = (digit + delta) % 10
                    new_state =  state[:i] + str(new_digit) + state[i+1:]

                    if new_state == target:
                        return move + 1
                    
                    if new_state not in visited and new_state not in dead:
                      visited.add(new_state)
                      q.append((new_state, move + 1))
        
        return -1

