class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board) # 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        sqrs = [set() for _ in range(N)]

        for i in range(N):
            for j in range(N):
                val = board[i][j]

                if val == '.':
                    continue
                
                if val in rows[i]:
                    return False
                rows[i].add(val)

                if val in cols[j]:
                    return False
                cols[j].add(val)

                sqr_idx = (i // 3) * 3 + j // 3

                if val in sqrs[sqr_idx]:
                    return False
                sqrs[sqr_idx].add(val)
        
        return True
                
                
