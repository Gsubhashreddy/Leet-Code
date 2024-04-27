class Solution:
    ma = 0
    def d(self, i , j, t1,t2, m,n,co):
        if i>=m or j >=n:
            return 0
        if (i,j) not in self.di:
            if t1[i] == t2[j]:
                self.di[(i,j)]  = 1 + self.d(i+1,j+1,t1,t2,m,n,co)
                # self.ma = max(self.ma, co)
            else:
                self.di[(i,j)] = max(self.d(i+1,j,t1,t2,m,n,co), self.d(i,j+1,t1,t2,m,n,co))
        return self.di[(i,j)]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.di = {}
        return self.d(0,0,text1, text2,len(text1),len(text2), 0)
        