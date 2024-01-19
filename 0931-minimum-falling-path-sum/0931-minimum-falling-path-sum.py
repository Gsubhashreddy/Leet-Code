class Solution:
    # def helper(self, matrix, rows, currentSum, currRow, currCol):
    #     # Base Case
    #     if currRow >= rows:
    #         return currentSum

    #     # Logic
    #     if currCol == 0:
    #         case1 = self.helper(matrix, rows, currentSum + matrix[currRow][currCol], currRow+1, currCol )
    #         case2 = self.helper(matrix, rows, currentSum + matrix[currRow][currCol], currRow+1, currCol+1)
    #         return min(case1,case2)
    #     elif currCol == rows-1:
    #         case1 = self.helper(matrix, rows, currentSum + matrix[currRow][currCol], currRow+1, currCol)
    #         case2 = self.helper(matrix, rows, currentSum + matrix[currRow][currCol], currRow+1, currCol-1)
    #         return min(case1,case2)
    #     else:
    #         case1 = self.helper(matrix, rows, currentSum + matrix[currRow][currCol], currRow+1, currCol)
    #         case2 = self.helper(matrix, rows, currentSum + matrix[currRow][currCol], currRow+1, currCol-1)
    #         case3 = self.helper(matrix, rows, currentSum + matrix[currRow][currCol], currRow+1, currCol+1)
    #         return min(case1,case2,case3)


    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        # Recursion Solution 
        # res = math.inf
        # print(res)
        # for i in range(length):
        #     temp =  self.helper(matrix, length, 0, 0, i)
        #     if temp< res:
        #         res = temp
        # return res

        # Dp Solution
        if length ==1 :
            return matrix[0][0]
        res = matrix[-1]
        for row in range(length-2,-1,-1):
            temp=[]
            for col in range(length):
                minimumElement = 0
                if col ==0:
                    minimumElement = min(res[0], res[1])                    
                elif col == length-1:
                    minimumElement = min(res[-1], res[-2])
                else:
                    minimumElement = min(res[col-1], res[col], res[col+1])
                temp.append(matrix[row][col] + minimumElement)
            res = temp
        return min(res)
            