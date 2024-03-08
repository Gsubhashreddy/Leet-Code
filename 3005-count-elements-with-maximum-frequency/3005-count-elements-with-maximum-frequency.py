class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        di = {}
        ma = -1
        for i in nums:
            di[i] = di.get(i,0)+1
            ma = max(ma, di[i])
        co = 0
        for i in di:
            if di[i] == ma:
                co+=1
        return co * ma
        