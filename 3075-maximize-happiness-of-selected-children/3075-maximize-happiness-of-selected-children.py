class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        val = 0
        co = 0
        for i in happiness:
            if k>0:
                i -= co
                if i >=0 :
                    val += i
                co += 1
                k -= 1
            else:
                return val
        return val
        