class Solution:
    res = []
    def dfs(self, i,j, s, n):
        if len(s) == n*2:
            self.res.append(s)
            return
        if i<n:
            self.dfs(i+1,j,s+"(",n)
        if j<i:
            self.dfs(i,j+1,s+")",n)
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.dfs(0,0,'',n)
        return self.res
        