class Solution:
    nums = []
    multipliers = []
    m = 0
    def helper(self, i, le):
        if i == self.m:
            return 0
        ri = self.n-1-(i-le)
        mul = self.multipliers[i]
        if (i,le) not in self.di:
            self.di[(i,le)] = max((mul*self.nums[le] + self.helper(i+1,le+1)),(mul*self.nums[ri]+self.helper(i+1,le)))
        return self.di[(i,le)]
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        self.di = {}
        self.nums = nums
        self.multipliers = multipliers
        self.m = len(multipliers)
        self.n = len(self.nums)
        return self.helper(0,0)
        
        