class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, h = 0, len(nums)-1
        co = 0
        while l<h:
            if nums[l] + nums[h] == k:
                l+=1
                h-=1
                co+=1
            elif nums[l] + nums[h] > k:
                h-=1
            else:
                l+=1
        return co
        