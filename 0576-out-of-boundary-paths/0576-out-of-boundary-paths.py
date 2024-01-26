class Solution:
#     res=0
#     def dfs(self,m,n,x,y,maxMove,dirs):
#         # Problems to solve
#             #1 How to calculate no of ways to boundary
#                 # Give position we can calculate (x,y) and (m,n)
#                 # x-1 <0 , y-1 <0 , x+1>=m, y+1 >=n, calculate steps
#             # Now, we need to know how many ways to go
#                 #Can use DFS for this
#             # Continue till the maxMOve >0
        
#         #Base
#         print(x,y,maxMove)
#         if x <0 or y <0 or x>=m or y>=n:
#             self.res+=1
#             return
#         if maxMove<=0:
#             return
#         maxMove-=1
        
#         #Logic
#         for direction in dirs:
#             self.dfs(m,n,x+direction[0],y+direction[1],maxMove,dirs)



    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # self.res=0
        # dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        # self.dfs(m,n,startRow,startColumn,maxMove,dirs)
        # return self.res
        M = 1000000000 + 7
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[startRow][startColumn] =1
        count = 0 
        for c in range(1,maxMove+1):
            temp = [[0 for i in range(n)] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m - 1: count = (count + dp[i][j]) % M
                    if j == n - 1: count = (count + dp[i][j]) % M
                    if i == 0:     count = (count + dp[i][j]) % M
                    if j == 0:     count = (count + dp[i][j]) % M
                    temp[i][j] = (((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) % M + 
              ((dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0)) % M) % M
            dp = temp
        return count
                    