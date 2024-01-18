class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        res = 0
        l1,l2=0,0
        for i in range(2, len(cost)+1):
            temp = min(l1 + cost[i-1], l2 + cost[i-2])
            res = temp
            l2 = l1
            l1 = temp
        return res
        