class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a = score[:]
        a.sort(reverse = True)
        re = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = []
        di = {}
        for i in range(len(a)):
            if i<=2:
                di[a[i]] = re[i]
            else:
                di[a[i]] = str(i+1)
        for i in score:
            res.append(di[i])
        return res
        return []
        