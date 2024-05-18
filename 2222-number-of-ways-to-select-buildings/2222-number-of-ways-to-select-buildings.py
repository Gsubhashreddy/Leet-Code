class Solution:
    def numberOfWays(self, s: str) -> int:
        totZero = 0
        for i in s:
            if i == '0':
                totZero += 1
        totOne = len(s) - totZero
        curZero = 0
        curOne = 0
        if s[0] == '0':
            curZero+=1
        else:
            curOne += 1
        res = 0
        for i in range(1,len(s)):
            if s[i] == '1':
                res += (curZero * (totZero - curZero))
                curOne += 1
            else:
                res += (curOne * (totOne-curOne))
                curZero += 1
        return res