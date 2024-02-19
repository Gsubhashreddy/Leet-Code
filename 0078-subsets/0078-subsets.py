class Solution:
    res = []
    
    def helper(self,nums, ind, path):
        
        # Base
        self.res.append(path[:])
        if ind >= len(nums):
            return

        # Logic
        for i in range(ind, len(nums)):                
            path.append(nums[i])
            self.helper(nums, i+1, path)
            path.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res =[]
        self.helper(nums, 0, [])
        return self.res