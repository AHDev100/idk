class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mp_row = defaultdict(set)
        mp_col = defaultdict(set)
        mp_grid = defaultdict(set)
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    continue
                if ch in mp_row[i] or ch in mp_col[j] or ch in mp_grid[(i // 3 * 3 + j // 3)]:
                    return False
                mp_row[i].add(ch)
                mp_col[j].add(ch)
                mp_grid[(i // 3 * 3 + j // 3)].add(ch)
        return True