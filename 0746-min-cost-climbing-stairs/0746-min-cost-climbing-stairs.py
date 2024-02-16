class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0 for i in cost]
        # res[0], res[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            res[i] = min(res[i-2] + cost[i-2], res[i-1]+ cost[i-1])
        return min(res[-1] + cost[-1] , res[-2]+ cost[-2])
        return 0
        