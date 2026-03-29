class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9  # Size of the Sudoku board (9x9)

        # Use sets to keep track of seen numbers in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(N)]
        columns = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        # Iterate through each cell in the board
        for row in range(N):
            for col in range(N):
                value = board[row][col]

                # Skip empty cells
                if value == ".":
                    continue

                # Check if the value already exists in the current row
                if value in rows[row]:
                    return False
                rows[row].add(value)

                # Check if the value already exists in the current column
                if value in columns[col]:
                    return False
                columns[col].add(value)

                # Determine the index of the 3x3 box
                box_index = (row // 3) * 3 + col // 3

                # Check if the value already exists in the current 3x3 box
                if value in boxes[box_index]:
                    return False
                boxes[box_index].add(value)

        # If no duplicates are found, the Sudoku board is valid
        return True
