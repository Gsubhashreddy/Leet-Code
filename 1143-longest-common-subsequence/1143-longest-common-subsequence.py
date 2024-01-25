class Solution:
    
    # def helper(self, t1, t2, i1, i2,res):
    #     # Base
    #     if i1>= len(t1) or i2>=len(t2):
    #         return res
    #     # Logic
    #     if t1[i1] == t2[i2]:
    #         c1 = self.helper(t1,t2,i1+1,i2+1, res+1)
    #         return c1
    #     else:
    #         c1 = self.helper(t1,t2,i1+1,i2, res)
    #         c2 = self.helper(t1,t2,i1,i2+1, res)
    #         return max(c1,c2)
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        # print(dp)
        for i in range(len(text2)):
            for j in range(len(text1)):
                k,l = i+1, j+1
                # print(k,l)
                if text2[i]==text1[j]:
                    
                    dp[k][l] = 1+ dp[k-1][l-1]
                else:
                    dp[k][l] = max(dp[k-1][l],dp[k][l-1])
        
        return dp[-1][-1]
        