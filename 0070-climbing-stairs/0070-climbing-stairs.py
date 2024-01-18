class Solution:
    # def helper(self,n,s):
    #     if s==n:
    #         self.res+=1
    #         return
    #     if s>n:
    #         return
    #     self.helper(n,s+1)
    #     self.helper(n,s+2)
        
        
    def climbStairs(self, n: int) -> int:
        res=[1,2]
        if n ==1:
            return 1
        elif n==2:
            return 2
        c1,c2=1,2
        for i in range(2,n):
            temp = c1+c2
            res.append(temp)
            c1 = c2
            c2 = temp
            
            # res.append(res[i-1]+res[i-2])
            # res[i-1] = max(res[i-2],0)
        return res[-1]