import math
class Solution:
    res = set()
    li = []
    def generate(self,n):
        nu = math.floor(math.sqrt(n))
        for i in range(1, nu+1):
            self.res.add(i**2)
            self.li.append(i**2)
        

#     def helper(self,ind, n, result, le):

#         if n ==0:
#             return result
#         if n<0 or ind>=le:
#             return float("inf")

#         currSum = n - self.res[ind]
#         t1 = self.helper(ind, currSum, result+1,le)
#         t2 = self.helper(ind+1, currSum, result+1, le)
#         t3 = self.helper(ind+1, n, result, le)

#         return min(t1,t2,t3)
        
    def numSquares(self, n: int) -> int:
        self. res = set()
        self.li = []
        self.generate(n)
        # return self.helper(0, n, 0, len(self.res))
        # return 0
        result = [1]
        index = 0
        for i in range(2, n+1):
            if i in self.res:
                result.append(1)
                index+=1
            else:
                mini = float('inf')
                for ind in range(index+1):
                    # print(index,i)
                    # print(result)
                    mini = min(mini, result[i - self.li[ind]-1]+1)
                result.append(mini)
        return result[-1]
                    
            