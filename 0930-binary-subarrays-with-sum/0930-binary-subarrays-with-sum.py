class Solution:
    def numSubarraysWithSum(self, nums: List[int], goals: int) -> int:
        su = 0
        di = {}
        co = 0
        for i in nums:
            su += i
            if su == goals:
                co += 1
            if su - goals in di:
                co += di[su - goals]
            di[su] = di.get(su,0) + 1
        return co
            