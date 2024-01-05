class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[nums[0]]
        i=1
        le=len(nums)
        while i<le:
            if nums[i]>res[-1]:
                res.append(nums[i])
            else:
                k = 0
                while nums[i] > res[k]:
                    k += 1
                res[k] = nums[i]
            i+=1
        return len(res)
                        
                
         
        