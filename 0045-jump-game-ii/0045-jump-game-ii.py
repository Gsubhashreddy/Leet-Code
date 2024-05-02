class Solution:
    def jump(self, nums: List[int]) -> int:
        le = len(nums)
        res = [float(inf) for i in range(le)]
        res[-1] = 0
        for i in range(le-2, -1,-1):
            mi = float(inf)
            fur = min(le-1, i+nums[i])
            # if fur == le -1:
            #     res[i] = 1
            #     continue
            for pos in range(i+1,fur+1):
                mi = min(mi, res[pos])
            res[i] = 1+ mi
        print(res)
        return res[0]
            
        