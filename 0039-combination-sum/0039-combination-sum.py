class Solution:
    res = []
    def backTrack(self, candidates, cSum, cPath, ind):
        #Base
        if cSum == 0:
            print(cPath)
            self.res.append(cPath[:])
            return
        if ind >= len(candidates) or cSum < 0:
            return
        
        
        # Logic
        self.backTrack( candidates, cSum, cPath, ind+1)
        
        ele = candidates[ind]
        cPath.append(ele)
        c2 = self.backTrack(candidates, cSum - ele, cPath, ind)
        cPath.pop()
        
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backTrack(candidates, target , [], 0)
        return self.res
        
        