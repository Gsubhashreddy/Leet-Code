class Solution:
    r1,c1,r2,c2 = 0,0,0,0
    def dfs(self, land, i,j,r,c):
        if(i<0 or j<0 or i>=r or j>=c or land[i][j]==0):
            return
        if self.r2<i:
            self.r2 = i
        if self.c2 < j:
            self.c2 = j
        land[i][j] = 0
        self.dfs(land,i+1,j,r,c)
        self.dfs(land,i-1,j,r,c)
        self.dfs(land,i,j+1,r,c)
        self.dfs(land,i,j-1,r,c)
        
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        r=len(land)
        c= len(land[0])
        self.r1,self.r2,self.c1,self.c2= 0,0,0,0
        res=[]
        for i in range(r):
            for j in range(c):
                if land[i][j]==1:
                    self.r1,self.r2,self.c1,self.c2= i,i,j,j
                    self.dfs(land,i,j,r,c)
                    res.append([self.r1,self.c1,self.r2,self.c2])
        return res
                    
        