class Solution:
    def minOperations(self, nums: List[int]) -> int:
        di={}
        for i in nums:
            di[i]=di.get(i,0)+1
        res=0
        for i in di:
            co=di[i]
            if co == 1: 
                return -1
            res += ceil(co / 3)
        return res
        