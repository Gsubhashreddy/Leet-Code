class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [len(nums)+1 for i in nums]
        
        res[0] = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            for j in range(1, nums[i]+1):
                if i+j>= len(nums):
                    break
                res[i+j] = min(res[i+j], res[i] + 1)
                
        return res[-1]
        