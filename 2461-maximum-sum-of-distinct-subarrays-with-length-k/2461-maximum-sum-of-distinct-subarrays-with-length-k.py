class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        di = {}
        st = 0
        ma = 0
        for i in range(len(nums)):
            res += nums[i]
            di[nums[i]] = di.get(nums[i],0) +1
            if i-st+1 > k:
                res -= nums[st]
                di[nums[st]] = di.get(nums[st],0) -1
                if di[nums[st]] == 0:
                    del di[nums[st]]
                st+=1
            while di[nums[i]] > 1:
                res-= nums[st]
                di[nums[st]] = di.get(nums[st],0) -1
                if di[nums[st]] == 0:
                    del di[nums[st]]
                st += 1
            if i-st+1 == k:
                ma = max(res, ma)
        return ma
            
        