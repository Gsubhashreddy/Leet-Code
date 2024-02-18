class Solution:
    res = []
    
    def backTrack(self, candidates, ind, path, target, le):
        #Base
        if target == 0:
            self.res.append(path[:])
            return
        if ind > le or target < 0:
            return
        
        #Logic
        curr_sum = target
        for i in range(ind, le):
            path.append(candidates[i])
            self.backTrack(candidates, i, path, target - candidates[i], le)
            path.pop()
            
            
            
            
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backTrack(candidates, 0 , [], target, len(candidates))
        return self.res