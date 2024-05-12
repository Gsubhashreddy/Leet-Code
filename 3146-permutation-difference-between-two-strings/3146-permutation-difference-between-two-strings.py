class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        di = {}
        for i in range(len(s)):
            di[s[i]] = i
        re = 0
        for i in range(len(t)):
            re += abs(i-di[t[i]])
        return re
        