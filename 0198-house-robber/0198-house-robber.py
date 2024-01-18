class Solution:
#     def helper(self, ind, su, nums, le):
#         if ind >=le :
#             # All houses covered
#             return su
#         if ind == le-1:
#             return su + nums[-1]
        
#         # Logic
        
#         c1 = self.helper(ind+1, su, nums, le)
        
#         c2 = self.helper(ind+2, su+ nums[ind], nums, le)
        
#         return max(c1,c2)
    
    def rob(self, nums: List[int]) -> int:
        
        le = len(nums)
        
        if le ==1 :
            return nums[0]
        elif le == 2:
            return max(nums)
        fi,se = nums[0], max(nums[0], nums[1]) 
        res = 0
        for i in range(2,le):
            temp = max(se, fi + nums[i])
            res = temp
            fi = se
            se = temp
        return res

        