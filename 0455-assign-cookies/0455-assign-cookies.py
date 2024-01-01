class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        j=len(g)-1
        i=len(s)-1
        ma=0
        while i>=0 and j>=0:
            if s[i]>=g[j]:
                ma+=1
                i-=1
                j-=1
            else:
                j-=1
        return ma