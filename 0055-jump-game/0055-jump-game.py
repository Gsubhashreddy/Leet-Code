class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = False
        i = 0
        le = len(nums)-1
        while i < le:
            if nums[i] == 0:
                return False
            ma = 0
            mai = i
            for j in range(1,nums[i]+1):
                if i+j >= le:
                    return True
                if nums[i+j] + i+j > ma:
                    ma = nums[i+j] + i+j
                    mai = i+j
            i = mai
        return True
                
        