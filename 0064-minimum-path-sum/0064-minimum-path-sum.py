class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        curr_sum = grid[0][0]
        for i in range(1, col):
            curr_sum += grid[0][i]
            grid[0][i] = curr_sum
        curr_sum = grid[0][0]
        for i in range(1,row):
            curr_sum += grid[i][0]
            grid[i][0] = curr_sum
        for i in range(1, row):
            for j in range(1, col):
                temp = min(grid[i-1][j], grid[i][j-1])
                grid[i][j] = temp + grid[i][j]
        # print(grid)
        return grid[-1][-1]
            
            
        