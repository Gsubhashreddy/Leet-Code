class Solution:
    def dfs(self, board, i, j, word, ind, di, dirs, m, n):
        # Base Case
        if ind == len(word):
            return True
        
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        
        temp = (i, j)
        if board[i][j] == word[ind] and di.get(temp, False) == False:
            if ind == len(word) - 1:
                return True
            
            di[temp] = True
            for x, y in dirs:
                if self.dfs(board, i + x, j + y, word, ind + 1, di, dirs, m, n):
                    return True
            di[temp] = False
        
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(row):
            for j in range(col):
                if self.dfs(board, i, j, word, 0, {}, dirs, row, col):
                    return True
        
        return False