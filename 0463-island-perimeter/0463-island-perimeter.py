class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0
        for i in range(r):
            for j in range(c):
                
                if grid[i][j] == 1:
                    co = 0
                    for x,y in dirs:
                        x += i
                        y+= j
                        if x>=0 and x<r and y>=0 and y<c and grid[x][y] == 1:
                            co+=1
                    res += (4-co)
        return res
                            
                    
                    
        