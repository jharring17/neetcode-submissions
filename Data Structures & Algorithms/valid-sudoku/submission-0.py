class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(0, len(board[0])):
            for j in range(0, len(board)):
                curr = board[i][j]
                if curr == '.':
                    continue
                if curr in rows[j] or curr in cols[i] or curr in boxes[(j // 3) * 3 + (i // 3)]:
                    return False
                rows[j].add(board[i][j])
                cols[i].add(board[i][j])
                boxes[(j // 3) * 3 + (i // 3)].add(board[i][j])
        return True