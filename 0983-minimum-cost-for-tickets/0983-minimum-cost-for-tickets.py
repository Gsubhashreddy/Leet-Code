class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        dp = [0 for i in range(lastDay+1)]
        i = 0
        for day in range(1, lastDay +1):
            if day < days[i]:
                dp[day] = dp[day-1]
            else:
                i+=1
                dp[day] = min(dp[day-1]+costs[0], dp[max(0, day-7)]+ costs[1], dp[max(0, day-30)]+ costs[2])
        return dp [-1]