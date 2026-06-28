class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            if not self.isValidUnit(row):
                return False

        # Check columns
        for col in range(9):
            if not self.isValidUnit([board[row][col] for row in range(9)]):
                return False

        # Check 3x3 sub-boxes
        for box_row in range(3):
            for box_col in range(3):
                if not self.isValidUnit([board[row][col] for row in range(box_row * 3, (box_row + 1) * 3) for col in range(box_col * 3, (box_col + 1) * 3)]):
                    return False

        return True
    
    def isValidUnit(self, unit: List[str]) -> bool:
        seen = set()
        for num in unit:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True