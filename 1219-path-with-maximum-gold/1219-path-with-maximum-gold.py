class Solution:
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        di = {}
        m = len(grid)
        n = len(grid[0])
        ma = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j,cu):
            nonlocal ma
            if (i,j) in di:
                return ma
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0:
                return ma
            cu += grid[i][j]
            # print(cu)
            di[(i,j)] = True
            ma = max(cu,ma)
            for x,y in dirs:
                dfs(i+x,y+j, cu)
            del di[(i,j)]
            cu -= grid[i][j]
        for i in range(m):
            for j in range(n):
                dfs(i,j,0)
        return ma
        
            
        