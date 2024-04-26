class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ma = 0
        di = defaultdict(int)
        for i in nums:
            di[i] += 1
            ma = max(ma,i)
        if len(di)==1:
            for k in di:
                return di[k]*k
        res = [0 for i in range(ma+1)]
        for i in range(1,ma+1):
            # if i in di:
            res[i] = max(res[i-1], (di[i]*i + res[i-2]))
        return res[-1]
        